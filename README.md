# Hidden progress before insight — version 2

Focused research rerun, **30 September 2026**, responding to an independent Opus review of version 1. Human and animal evidence, precise measured variables, generalization limits, source inspection levels, competing mechanisms and an unrun discriminating experiment.

**Read the whole handoff:** [FULL_RESEARCH.md](FULL_RESEARCH.md)

**Direct text for another model:** [raw FULL_RESEARCH.md](https://raw.githubusercontent.com/jorgy72/hidden-progress-insight-research/main/FULL_RESEARCH.md)

The central result: measurable change can precede sudden strategy expression, and the measured neural transition can itself be abrupt. Precedence, gradualness, latent competence and awareness are separate questions.

## Contents

- [Report](REPORT.md) and [evidence/inspection ledger](EVIDENCE_LEDGER.md).
- [Registered search plan](SEARCH_PLAN.md), [search/selection audit](SEARCH_AUDIT.md), [exact query batches](SEARCH_BATCHES.json) and [machine-readable log](SEARCH_LOG.jsonl).
- [Response to the critique and v2 self-review](REVIEW_RESPONSE.md), [dated changes](CHANGELOG.md) and [lab notebook](LAB_NOTEBOOK.md).
- [Proposed experiment](NEXT_EXPERIMENT.md) and [research workflow](WORKFLOW.md).
- [Declared download resources](SOURCE_LIST.json), [current cache manifest](source_manifest.json), [v1 history](SOURCE_HISTORY_V1.json), [v2 retrieval attempts](retrieval_attempts.jsonl), retrieval script/tests and [validation results](VALIDATION.json).
- [Original v1 files](versions/v1), also preserved at [the original commit](https://github.com/jorgy72/hidden-progress-insight-research/tree/a0dad4503c621923d42299cf8fdc377c3d13d03b).

## Interpretation and reproducibility limits

This is a focused review, not a systematic review or saturation claim. Verification levels remain visible, including abstract-only and partial-page sources. The earlier independent critique concerned v1; the v2 critic pass is **self-review**, not independent review. No biological experiment or original-study analysis/simulation replication was run.

Downloaded third-party papers, source extracts and figure renders are **not rehosted**. Follow primary links for inspection. The manifest records local retrieval and hashes, not full reading verification. Some studies were inspected through web-reader primary text/abstracts and are not download resources.

To reconstruct the declared cache in a fresh directory with Python 3.9+:

```sh
python3 -m pip install requests pypdf
python3 fetch_sources.py
python3 -m unittest discover -s . -p test_fetch_sources.py
```

Copy `SOURCE_LIST.json` and the script there first. If using this repository directly, the cached source files are absent: saved manifest entries will be re-fetched, while recorded failures require `--retry-failed`. Default validated-cache reruns are byte-identical; `--refresh` explicitly creates new attempts and retains earlier content-addressed bytes. Upstream access/bytes may change. The current script cannot reconstruct unlogged v1 searches or every manual v1 acquisition.

`FILE_HASHES.json` covers this complete package, including archived v1, excluding itself. The combined text contains all current documents/code/provenance records; v1 is linked and separately preserved so outdated claims do not appear as current conclusions.
