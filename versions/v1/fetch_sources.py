"""Preserve a focused primary-source corpus with hashes and extraction provenance."""
from pathlib import Path
import hashlib, json, datetime, re
import requests
from pypdf import PdfReader

ROOT = Path(__file__).parent
SOURCES = {
 'schuck2015': 'https://schucklab.gitlab.io/docs/papers/Schuck_etal_2015_Neuron.pdf',
 'rose2010': 'https://www.kognition.uni-koeln.de/literature/Rose_Haider_Buechel_2010.pdf',
 'siniscalchi2016': 'https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf',
 'metcalfe1987': 'https://www.columbia.edu/cu/psychology/metcalfe/PDFs/Metcalfe%20Wiebe%201987.pdf',
 'drieu2025': 'https://cdn.prod.website-files.com/690a83fda53579ba8497635f/69bbf890f8d2b187f99e3620_2025_Nature_Drieu.pdf',
 'kuchibhotla2019': 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6517418/fullTextXML',
 'jungbeeman2004': 'https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0020097&type=printable',
 'nanda2023': 'https://arxiv.org/pdf/2301.05217',
 'bowden1998': 'https://cpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/a/699/files/2015/11/Getting-the-right-idea-Semantic-activation-in-the-right-hemisphere-may-help-solve-insight-problems-154um4l.pdf',
 'bilalic2021': 'https://neuroscienceofexpertise.com/Publications/papers/Bilalic_2021_Insight.pdf',
 'graf2023': 'https://eprints.whiterose.ac.uk/199182/1/jintelligence-11-00086-v2.pdf',
}
def main():
    records = []
    for name, url in SOURCES.items():
        record = dict(name=name, requested_url=url, retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        try:
            r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=45);r.raise_for_status()
            record.update(final_url=r.url,content_type=r.headers.get('content-type'),sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content))
            ext='pdf' if r.content.startswith(b'%PDF') else 'xml' if 'xml' in r.headers.get('content-type','') else 'html'
            dest=ROOT/'sources'/f'{name}.{ext}';dest.parent.mkdir(exist_ok=True);dest.write_bytes(r.content)
            if ext=='pdf':
                pdf=PdfReader(dest);record['pages']=len(pdf.pages)
                extracted='\n\n'.join(f'=== PDF PAGE {i+1} ===\n'+(p.extract_text() or '') for i,p in enumerate(pdf.pages))
                record['extraction']='pypdf; page reading order may vary; selected figures inspected separately'
                record['substantive_text_extracted']=len(re.sub(r'=== PDF PAGE \d+ ===','',extracted).strip()) > 500
                if not record['substantive_text_extracted']:
                    record['inspection_required']='Image-only PDF: render and inspect pages; file presence is not content verification.'
            else:
                extracted=re.sub(r'<[^>]+>',' ',r.text)
                extracted=re.sub(r'\s+',' ',extracted)
                record['extraction']='tag-stripped text; raw XML retained'
            dest.with_suffix('.txt').write_text(extracted)
            record['status']='saved';record['path']=str(dest.relative_to(ROOT))
        except Exception as e:
            record.update(status='failed',error=str(e))
        records.append(record);print(name,record['status'],record.get('bytes',record.get('error')))
    manifest=ROOT/'source_manifest.json'
    if manifest.exists():
        records=json.loads(manifest.read_text())+records
    manifest.write_text(json.dumps(records,indent=2)+'\n')
if __name__=='__main__': main()
