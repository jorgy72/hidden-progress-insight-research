# Hidden progress before insight — workflow/handoff 2.2; research 2.1

**30 September 2026.** This package adds a fresh discovery stage to the reusable workflow. The scientific report, evidence ledger and proposed biological experiment remain version 2.1. No new literature rerun or reading-depth upgrade was performed for this method update.

Discovery sequence: neutral brief → fresh context and bounded search → freeze output/log → reconcile candidates → verify and synthesize → critic pass. The received fresh Opus answer is reconciled retrospectively; its unseen search history and independence are not invented.

**Read the whole handoff:** [FULL_RESEARCH.md](FULL_RESEARCH.md)

**Direct text for another model:** [raw FULL_RESEARCH.md](https://raw.githubusercontent.com/jorgy72/hidden-progress-insight-research/main/FULL_RESEARCH.md)

Feeling stuck does not necessarily mean nothing is changing. Some studies find useful attention or brain changes before a new strategy is used; others record abrupt brain transitions. Earlier change and a sudden breakthrough can coexist. We still cannot tell what happens during a particular long human impasse. The report gives primary examples and separates earlier timing from gradual progress.

## Contents

- [Fresh discovery brief and record](FRESH_DISCOVERY_TEMPLATE.md), [literature audit template](LITERATURE_AUDIT_TEMPLATE.md) and [retrospective candidate reconciliation](DISCOVERY_RECONCILIATION.md).
- [Report with plain-language opening](REPORT.md) and [evidence/inspection ledger](EVIDENCE_LEDGER.md).
- [Indexed forward-citation audit](CITATION_INDEX_AUDIT.md), [metadata](CITATION_INDEX_RESULTS.json), [selected primary checks](CITATION_SCREENING_LOG.json) and reproducible citation-retrieval script.
- [Registered search plan](SEARCH_PLAN.md), [search/selection audit](SEARCH_AUDIT.md), [exact query batches](SEARCH_BATCHES.json) and [machine-readable log](SEARCH_LOG.jsonl).
- [Response to the critique and v2 self-review](REVIEW_RESPONSE.md), [dated changes](CHANGELOG.md) and [lab notebook](LAB_NOTEBOOK.md).
- [Proposed experiment](NEXT_EXPERIMENT.md) and [research workflow](WORKFLOW.md).
- [Declared download resources](SOURCE_LIST.json), [current cache manifest](source_manifest.json), [v1 history](SOURCE_HISTORY_V1.json), [v2 retrieval attempts](retrieval_attempts.jsonl), retrieval script/tests and [validation results](VALIDATION.json).
- [Original v1 files](versions/v1), with v2 preserved at [its commit](https://github.com/jorgy72/hidden-progress-insight-research/tree/8444c2d2148270f7af0a09c4945f33a469658ecd); v2.1 preserved at [its commit](https://github.com/jorgy72/hidden-progress-insight-research/tree/b297a0aa3dbb26cc81aeeeb2061d53b145a5af19); v1 also preserved at [the original commit](https://github.com/jorgy72/hidden-progress-insight-research/tree/a0dad4503c621923d42299cf8fdc377c3d13d03b).

## Interpretation and reproducibility limits

This is a focused review, not a systematic review or saturation claim. Verification levels remain visible, including abstract-only and partial-page sources. The user supplied independent Opus critiques of v1 and published v2. The v2.1 amendments and this v2.2 method addition received **self-checks**. The later user-supplied fresh-answer comparison and Opus follow-up are recorded as bounded feedback; they are not a fresh independent audit of this entire package or a controlled workflow evaluation. No biological experiment or original-study analysis/simulation replication was run.

Downloaded third-party papers, source extracts and figure renders are **not rehosted**. Follow primary links for inspection. The manifest records local retrieval and hashes, not full reading verification. Some studies were inspected through web-reader primary text/abstracts and are not download resources.

To reconstruct the declared cache in a fresh directory with Python 3.9+:

```sh
python3 -m pip install requests pypdf
python3 fetch_sources.py
python3 -m unittest discover -s . -p test_fetch_sources.py
```

Copy `SOURCE_LIST.json` and the script there first. If using this repository directly, the cached source files are absent: saved manifest entries will be re-fetched, while recorded failures require `--retry-failed`. Default validated-cache reruns are byte-identical; `--refresh` explicitly creates new attempts and retains earlier content-addressed bytes. Upstream access/bytes may change. The current script cannot reconstruct unlogged v1 searches or every manual v1 acquisition.

`FILE_HASHES.json` covers this complete package, including archived v1, excluding itself. The combined text contains all current documents/code/provenance records; v1 is linked and separately preserved so outdated claims do not appear as current conclusions.
