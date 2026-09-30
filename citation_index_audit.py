"""Bounded forward-citation discovery; public metadata, never full-text rehosting."""
from pathlib import Path
import datetime, hashlib, json, time
import requests

OUT = Path(__file__).parent
ANCHORS = {'Schuck2015': '25819613', 'PowellRedish2016': '27653278', 'Knoblich2001': '11820744'}
plan = {'cutoff': '2026-09-30', 'anchors': ANCHORS,
        'scope': 'Three-anchor indexed forward check, not an exhaustive literature search.',
        'screening': 'Metadata discovery followed by title triage and primary-source checking of potentially direct new leads.',
        'coverage_limit': 'Europe PMC citations use open PMC/Crossref data; NCBI citedin is a subset, not every global citing paper.'}
(OUT / 'CITATION_INDEX_PLAN.json').write_text(json.dumps(plan, indent=2) + '\n')
result = {'plan': plan, 'retrieved_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'anchors': {}}
session = requests.Session()
session.headers['User-Agent'] = 'ResearchLabCitationAudit/2.1 (public literature metadata)'
for name, pmid in ANCHORS.items():
    anchor = {'pmid': pmid, 'europe_pmc_queries': [], 'records': [], 'errors': []}
    page = 1
    while True:
        url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/MED/{pmid}/citations?format=json&page={page}&pageSize=1000'
        try:
            response = session.get(url, timeout=40)
            response.raise_for_status()
            data = response.json()
            anchor['europe_pmc_queries'].append({'url': url, 'response_sha256': hashlib.sha256(response.content).hexdigest(), 'hitCount': data.get('hitCount')})
            records = data.get('citationList', {}).get('citation', [])
            anchor['records'].extend(records)
            if len(anchor['records']) >= int(data.get('hitCount', 0)) or not records:
                break
            page += 1
        except Exception as exc:
            anchor['errors'].append({'url': url, 'error': str(exc)})
            break
    time.sleep(.4)
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&linkname=pubmed_pubmed_citedin&id={pmid}&retmode=json'
    try:
        response = session.get(url, timeout=40)
        response.raise_for_status()
        data = response.json()
        anchor['ncbi'] = {'url': url, 'response_sha256': hashlib.sha256(response.content).hexdigest(), 'linksets': data.get('linksets', []), 'error': data.get('error')}
    except Exception as exc:
        anchor['errors'].append({'url': url, 'error': str(exc)})
    result['anchors'][name] = anchor
    (OUT / 'CITATION_INDEX_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(name, 'Europe PMC returned', len(anchor['records']), 'records;', 'errors', len(anchor['errors']), flush=True)
    time.sleep(.4)
