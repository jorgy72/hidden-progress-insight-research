"""Cache a declared primary corpus; current state and append-only attempts are separate.
Python 3.9+, requests; pypdf is optional. No credentials or paywall bypass.
"""
import argparse, datetime, hashlib, json, re
from pathlib import Path
import requests

def digest(data):
    return hashlib.sha256(data).hexdigest()

def run(root, selected=None, refresh=False, retry_failed=False, fetch=None):
    root = Path(root)
    declarations = json.loads((root / 'SOURCE_LIST.json').read_text())
    ids = [s['id'] for s in declarations]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate declared source ID')
    if selected and not set(selected).issubset(ids):
        raise ValueError('Unknown requested source ID')
    manifest_path = root / 'source_manifest.json'
    current = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    before = json.dumps(current, sort_keys=True)
    attempts = []
    (root / 'sources').mkdir(exist_ok=True)
    for source in declarations:
        sid, url = source['id'], source['url']
        if selected and sid not in selected:
            continue
        previous = current.get(sid, {})
        cache = root / previous.get('path', '__missing__')
        same_url = previous.get('requested_url') == url
        valid = (same_url and previous.get('status') == 'saved' and cache.is_file()
                 and digest(cache.read_bytes()) == previous.get('sha256'))
        if valid and not refresh:
            print(sid, 'cached')
            continue
        if same_url and previous.get('status') == 'failed' and not (retry_failed or refresh):
            print(sid, 'previous failure; use --retry-failed')
            continue
        record = dict(id=sid, requested_url=url,
                      retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        try:
            response = (fetch or requests.get)(url, headers={'User-Agent': 'ResearchLab/2.0'}, timeout=35)
            response.raise_for_status()
            data = response.content
            if not data:
                raise ValueError('Empty response')
            content_type = response.headers.get('content-type', '')
            ext = 'pdf' if data.startswith(b'%PDF') else 'xml' if 'xml' in content_type else 'html'
            if ext == 'html' and any(x in response.text[:6000].lower() for x in
                    ('checking your browser', 'captcha', 'enable javascript to proceed', 'client challenge')):
                raise ValueError('Access challenge; response is not article content')
            # Content-addressed files preserve older bytes when --refresh changes a source.
            sha = digest(data)
            path = Path('sources') / (sid + '-' + sha[:12] + '.' + ext)
            (root / path).write_bytes(data)
            record.update(status='saved', final_url=response.url, content_type=content_type,
                          bytes=len(data), sha256=sha, path=path.as_posix())
            if ext == 'pdf':
                try:
                    from pypdf import PdfReader
                    pdf = PdfReader(root / path)
                    extracted = '\n\n'.join(f'=== PDF PAGE {i+1} ===\n' + (p.extract_text() or '')
                                             for i, p in enumerate(pdf.pages))
                    record.update(pages=len(pdf.pages), extraction='pypdf; reading order may vary',
                                  substantive_text_extracted=len(re.sub(r'=== PDF PAGE \d+ ===', '', extracted).strip()) > 500)
                    if not record['substantive_text_extracted']:
                        record['inspection_required'] = 'Render pages; empty text is not evidence of reading.'
                    (root / path).with_suffix('.txt').write_text(extracted)
                except Exception as error:
                    record['extraction_error'] = str(error)
            else:
                # This is a navigation aid, not an article-content verifier.
                extracted = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', response.text))
                (root / path).with_suffix('.txt').write_text(extracted)
                record['extraction'] = 'tag-stripped navigation aid; verify article content separately'
        except Exception as error:
            record.update(status='failed', error=str(error))
            if valid:
                # A failed refresh must not erase a valid previously cached source.
                record['previous_valid_cache_retained'] = True
        attempts.append(record)
        if record['status'] == 'saved' or not valid:
            current[sid] = record
        print(sid, record['status'], record.get('bytes', record.get('error')))
    if before != json.dumps(current, sort_keys=True):
        temp = manifest_path.with_suffix('.tmp')
        temp.write_text(json.dumps(current, indent=2, sort_keys=True) + '\n')
        temp.replace(manifest_path)
    if attempts:
        with (root / 'retrieval_attempts.jsonl').open('a') as stream:
            for record in attempts:
                stream.write(json.dumps(record, sort_keys=True) + '\n')
    return current, attempts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).parent)
    parser.add_argument('--only', nargs='+')
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--retry-failed', action='store_true')
    args = parser.parse_args()
    run(args.root, args.only, args.refresh, args.retry_failed)
