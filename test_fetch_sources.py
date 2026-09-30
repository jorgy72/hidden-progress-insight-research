"""Offline tests of cache and provenance failure modes, not scientific replication."""
import json, tempfile, unittest
from pathlib import Path
from fetch_sources import run

class Response:
    headers = {'content-type': 'text/html'}
    url = 'https://example.org/article'
    def __init__(self, text):
        self.text = text
        self.content = text.encode()
    def raise_for_status(self):
        pass

class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root/'SOURCE_LIST.json').write_text(json.dumps([{'id':'a','url':'https://example.org/article'}]))
    def tearDown(self):
        self.temp.cleanup()
    def test_rerun_is_byte_identical_and_refresh_preserves_old_bytes(self):
        run(self.root, fetch=lambda *a,**k: Response('<p>first content</p>'))
        original = (self.root/'source_manifest.json').read_bytes()
        history = (self.root/'retrieval_attempts.jsonl').read_bytes()
        def forbidden(*a,**k):
            self.fail('Cached rerun must not call network')
        run(self.root, fetch=forbidden)
        self.assertEqual(original,(self.root/'source_manifest.json').read_bytes())
        self.assertEqual(history,(self.root/'retrieval_attempts.jsonl').read_bytes())
        first = json.loads(original)['a']['path']
        current,_ = run(self.root, refresh=True, fetch=lambda *a,**k: Response('<p>second content</p>'))
        self.assertNotEqual(first,current['a']['path'])
        self.assertTrue((self.root/first).exists())
        self.assertEqual(2,len((self.root/'retrieval_attempts.jsonl').read_text().splitlines()))
    def test_access_failure_skip_retry_and_valid_cache_retention(self):
        bad=lambda *a,**k: Response('Checking your browser CAPTCHA')
        current,_=run(self.root,fetch=bad)
        self.assertEqual('failed',current['a']['status'])
        _,attempts=run(self.root,fetch=bad)
        self.assertEqual([],attempts)
        current,_=run(self.root,retry_failed=True,fetch=lambda *a,**k:Response('article'))
        before=(self.root/'source_manifest.json').read_bytes()
        _,attempts=run(self.root,refresh=True,fetch=bad)
        self.assertTrue(attempts[0]['previous_valid_cache_retained'])
        self.assertEqual(before,(self.root/'source_manifest.json').read_bytes())
    def test_corrupt_cache_is_retrieved_and_unknown_id_rejected(self):
        current,_=run(self.root,fetch=lambda *a,**k:Response('article'))
        (self.root/current['a']['path']).write_text('corrupt')
        _,attempts=run(self.root,fetch=lambda *a,**k:Response('article'))
        self.assertEqual(1,len(attempts))
        with self.assertRaises(ValueError):
            run(self.root, selected=['unknown'])
    def test_duplicate_declaration_rejected(self):
        (self.root/'SOURCE_LIST.json').write_text(json.dumps([{'id':'a','url':'x'},{'id':'a','url':'y'}]))
        with self.assertRaises(ValueError):
            run(self.root)

if __name__=='__main__': unittest.main()
