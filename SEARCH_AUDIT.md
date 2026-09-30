# Search, selection and stopping audit — v2 with v2.1 amendment

Cutoff: **30 September 2026**. Focused coverage audit, not a systematic review. Plan recorded before the expanded searches in [SEARCH_PLAN.md](SEARCH_PLAN.md). Exact search strings, service and filters are in [SEARCH_BATCHES.json](SEARCH_BATCHES.json); primary access/citation decisions are in [SEARCH_LOG.jsonl](SEARCH_LOG.jsonl). Logs contain routes and decisions, not copyrighted article excerpts.

The v1 retrieval manifest was not a search log. Its missing query/ranking history cannot be reconstructed reliably; we preserve it as history instead of inventing it. The separately preserved v1 files retain their original, now inadequate stopping assertion.

## Version 2.1 amendment

A real indexed forward-citation check is now documented in [CITATION_INDEX_AUDIT.md](CITATION_INDEX_AUDIT.md), with a plan, exact API URLs, retrieved metadata and selected-primary decisions. It adds six further report studies; some remain provisional. The sections below record the v2 routes and limitations as performed, rather than retroactively converting web searches into indexed retrieval. The user-supplied independent Opus review of v2 has now arrived; amendments received a self-check.

## Search batches and observed information gain

| Batch | Purpose and actual selection outcome |
|---|---|
| B1 | Retrieve the three reviewer omissions and broaden recent coverage. Confirmed Knoblich and Townsend; latent-strategy results included a monkey working-memory paper whose use of “latent” did not mean progress before a breakthrough. |
| B2 | Resolve primary URLs and targeted citing work from Schuck/Durstewitz. Added Hasz & Redish and Löwe; publisher/repository reading verified their relevance. These searches added different neural-region timing and a human/model separation issue. |
| B3 | Chase Bilalić's backward references and independently search animal/recent evidence. Added Tseng and Rosenberg; identified Reddy's competing account. The broad Cushen author query produced irrelevant HRM results, so it was replaced with the exact cited title in B4. |
| B4 | Resolve Cushen; follow Rosenberg's alternative model; screen recent neural/preparatory studies. Added Cushen at preview depth and Reddy's behavioural reanalysis/model distinction; found a September 2026 active-inference theory, whose bibliography prompted a Stuyck primary-abstract check. |
| B5 | Resolved Becker et al. 2025 to its primary identifier and checked its pre/post-solution and subsequent-memory framing; not used to infer an impasse trajectory. |

These batches **continued yielding relevant evidence**. We do not claim saturation, low information gain, a complete citing-paper index or a reproducible database ranking. We stopped after the specified coverage routes and high-priority direct leads were examined, to deliver a bounded second version with its remaining gaps visible. Another exhaustive iteration could still add studies.

## Backward and forward routes actually checked

| Anchor | Route and selection |
|---|---|
| Bilalić | Read its reference/discussion entries for Knoblich, Ellis, Tseng and Cushen. Knoblich and Tseng primary relevant text inspected; Ellis retained at abstract/preview depth; Cushen added at preview depth. No claim that every reference was chased. |
| Schuck | Retained Rose as relevant precursor anchor. Powell explicitly discusses Schuck; Löwe cites the human strategy literature and supplies a separate human experiment plus model. Targeted search, not an exhaustive forward-citation export. |
| Durstewitz / Powell | Powell's references/discussion connect Durstewitz, Karlsson and Schuck. Hasz explicitly cites these strategy studies and extends the recording to hippocampal/prefrontal timing. Original full Durstewitz/Karlsson methods remain inaccessible here. |
| Kuchibhotla / Drieu | Acquisition/expression route retained and final Drieu publication identified. Reattempted final XML access failed; image-PDF reading depth remains two pages. No confidence upgrade from an index entry. |
| Rosenberg | Reddy explicitly reanalyses its routes and offers a competing mechanism. Counted as shared data, not independent animal replication. |
| Doulfoukar 2026 | Publisher metadata establishes September 17 publication; cited Stuyck 2024 followed to original abstract. The autonomic measure did not establish neural solution-content accumulation. Other theory references remain outside this bounded pass. |

## Other screened candidates and exclusions

| Candidate / source | Decision and inspection boundary |
|---|---|
| [Qian et al. 2026](https://doi.org/10.1038/s41467-026-69380-6), latent strategy from representational geometry | Screening primary abstract/indexed article text: monkey working-memory strategy discrimination, not a pre-breakthrough learning trajectory. Excluded from core temporal claims; complete methods not audited. |
| [Time-dependent deployment of medial prefrontal representations, 2026](https://doi.org/10.1038/s41467-025-68215-0) | Primary relevant abstract/discussion/method text: history-dependent reward-foraging representations and contextual deployment. No specified impasse-to-discovery trajectory. Excluded from core; could inform gating experiments. |
| [From pre-stimulus preparation to the Aha burst](https://doi.org/10.1016/j.cortex.2026.06.017) | Primary preview: EEG hidden-versus-unhidden character conditions, preparatory alpha and post-stimulus condition decoding. Does not establish accumulating answer content during an impasse. October issue date is not used as proof it was unavailable before cutoff; online publication date/full methods not fully audited. |
| [Becker et al. 2025, insight and subsequent memory](https://doi.org/10.1038/s41467-025-59355-4) | Primary abstract and relevant Discussion inspected: pre/post-solution visual representational change and subsequent memory. Does not resolve a hidden within-impasse trajectory; full temporal methods not audited. |
| Graf 2023 | Retained for methods; simulated abrupt illustration excluded and shared-data status recorded. |
| Doulfoukar 2026 | Included only as a bounded theoretical comparison, not biological evidence. |
| Generic reviews, theses, secondary summaries and unrelated author-name hits | Discovery leads or rejected mismatches; not independent evidence. Raw broad-search ranking is not preserved. |

## Coverage achieved and gaps

| Required stratum | Present evidence | Residual gap |
|---|---|---|
| Classic human puzzle/impasse | Knoblich, Tseng, Bilalić, Ellis; warmth/accessibility studies | Few prospective content measures with sufficient individual neural resolution; some preview-only studies. |
| Human neural strategy precursor | Rose, Schuck; solution EEG in Jung-Beeman | Generic/blocked measures cannot resolve all proposed hidden trajectories. |
| Animal neural switch | Powell, Hasz, Siniscalchi; provisional Durstewitz/Karlsson | Small species/task samples; no synaptic trajectory or animal conscious report. |
| Acquisition versus expression | Kuchibhotla; partially verified Drieu | Probe reactivity/context and full causal-method audit. |
| Abrupt animal behaviour and competing mechanism | Rosenberg plus Reddy reanalysis | Biological mechanism is not uniquely identified. |
| Recent human switching | Löwe 2024, Townsend 2026 | Human behavioural abruptness does not settle neural accumulation. |
| Model analogy/preparation boundary | Nanda, Löwe network, Reddy, Doulfoukar; Kounios/Stuyck | A matching model or early state is insufficient biological proof. |

V2 scope limitations at publication: one investigator; English-language targeted web searching; no comprehensive PsycINFO/Web of Science/Scopus export; no dual independent screening; incomplete raw search-result preservation; bounded citation chasing; no effect-size meta-analysis or study-data replication. The prepublication critic pass for v2 was explicitly **self-review**, with Opus's earlier independent critique retained as v1 feedback.
