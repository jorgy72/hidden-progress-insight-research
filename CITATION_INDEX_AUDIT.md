# Indexed forward-citation check — version 2.1

30 September 2026. Registered three-anchor follow-up: [plan](CITATION_INDEX_PLAN.json). This is actual indexed cited-by retrieval, not a web query containing an author name. The original v2 web-search audit is retained below its dated amendment.

| Anchor (PMID) | Europe PMC citing records | NCBI citedin PMIDs | NCBI-only PMIDs relative to that anchor's Europe PMC list |
|---|---:|---:|---|
| Schuck 2015 (25819613) | 105 | 71 | 38405946, 39314386 |
| Powell & Redish 2016 (27653278) | 76 | 49 | 39314328, 38370807, 40027783 |
| Knoblich 2001 (11820744) | 136 | 74 | 30618985 |

Every returned Europe PMC page was retrieved (each anchor fit on one 1,000-record page); both API routes succeeded for all three anchors. [Raw metadata and exact query URLs](CITATION_INDEX_RESULTS.json) include UTC retrieval time and response hashes. There are **317 anchor-record links, 299 unique Europe PMC source/ID pairs**; these counts are not numbers of independent studies. Preprints and final publications can appear separately, as the six NCBI-only records illustrate.

[Primary screening decisions](CITATION_SCREENING_LOG.json) cover 15 selected records: nine direct/boundary candidates plus all six NCBI-only records. All 15 primary abstracts and their first-publication metadata were checked. Six studies were added to the report, at the exact inspection depths recorded in its rows. Other metadata records remain discovery/deferred leads, not screened evidence or exclusions. This is priority follow-up, not a complete screening of 299 articles.

Consequential checks: Allegra reuses Schuck's data and its early frontal effect begins before the relevant correlation; Ding's decoder is Gaussian-smoothed; Ninomiya's gaze comparison has exclusions and broad equivalence bounds. Lu's full XML returned HTTP 500: its human intervention remains provisional at abstract/indexed-excerpt depth. The other two new XMLs were retrieved; [access/hashes](CITATION_RETRIEVAL_ATTEMPTS.json) preserve those outcomes. Full texts and abstract bodies are not rehosted. Allegra was inspected through the [author PDF](https://micheleallegra.github.io/publications/1-s2.0-S1053811920303402-main.pdf), not a local download.

## Coverage and cutoff limits

[NCBI's documentation](https://pmc.ncbi.nlm.nih.gov/tools/cites-citedby/) describes PMC-derived citing articles returned as PubMed identifiers. [Europe PMC's documentation](https://europepmc.org/help) explains that its network uses open PMC/Crossref citations and has narrower coverage than other services. Neither yields every global citing paper. Google Scholar, Scopus and Web of Science were not comprehensively accessed.

The API export is a dated snapshot, not an exhaustive corpus filtered to the research cutoff. Years alone do not validate every 2026 record's online date. Only the 15 checked follow-up papers are date-verified for inclusion; the raw index remains unfiltered discovery metadata. No post-cutoff paper is promoted to evidence from its year or title. Anchors beyond these three, other indexed leads, deeper provisional-paper Methods and duplicate-family resolution remain incomplete.

**Stopping:** this check still found relevant studies. We stop after the registered anchor retrieval and selected primary follow-ups to deliver the requested correction, not because yield is zero or the literature is saturated. A complete systematic review would require broader indexes, predefined complete screening and fuller Methods access.

## Reproduce the discovery step

Run `python3 citation_index_audit.py` with `requests` installed in a fresh writable folder containing the script. It writes the plan before API calls and then the metadata snapshot. It does not reproduce the manual screening or verify full reading. Network records/counts can change; response hashes document this run's returned bytes, which are not all rehosted.
