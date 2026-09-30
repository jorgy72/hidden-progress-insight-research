# Complete research handoff — version 2, 30 September 2026

Original research question: During the stuck period before a sudden insight or abrupt strategy change, is there evidence of gradual measurable brain/behaviour change, or is the neural transition abrupt too? Include human and animal studies; cite the specific study, what was measured and generalization; separate direct evidence and model analogy; end with unknowns and a settling experiment.



---

## File: README.md

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


---

## File: REPORT.md

# Hidden progress before insight or strategy change — version 2

Focused primary-source review, 30 September 2026. Question: during a period of apparent impasse, does useful change accumulate before sudden insight, or is the neural transition itself abrupt?

**Both earlier change and abrupt transitions are documented, sometimes in the same task.** The evidence rejects a universal equation of poor performance with no learning. It also rejects the assumption that every sudden behavioural improvement reflects a gradual neural ramp. The strongest conclusion is that acquisition, neural representation, policy selection, performance and conscious recognition can have different time courses. Whether a particular human impasse contains continuous, solution-specific neural accumulation remains substantially unresolved.

This is a focused review, not an exhaustive systematic review, meta-analysis or new experiment. Version 2 expands the original search and corrects its audit weaknesses. [Search and selection audit](SEARCH_AUDIT.md), [claim inspection ledger](EVIDENCE_LEDGER.md), [review response](REVIEW_RESPONSE.md) and [change log](CHANGELOG.md) are part of the result. Full papers remain at their original hosts.

## What would count as hidden progress?

Distinguish five observations before interpreting them:

- **Graded progress:** a measured variable becomes increasingly relevant to the eventual correct solution before its overt use. Generic changing activity, effort or fixation duration is insufficient.
- **Precursor:** a relevant representation or event appears before behaviour. Its earlier timing alone does not establish continuous accumulation or causality.
- **Abrupt transition:** a sampled variable changes rapidly relative to its measurement resolution. This says nothing by itself about unrecorded regions or synapses.
- **Latent knowledge:** a different probe/context reveals competence while ordinary performance remains poor. This establishes an acquisition/expression discrepancy, not necessarily a neural ramp.
- **Preparatory state:** an initial state predicts later solution mode. Before a problem is presented, it cannot be progress on that particular problem.

These categories can coexist. Evidence of subjective surprise is different from measured neural abruptness. A familiar rule switch is different from discovering a novel puzzle solution; neither necessarily involves a verified period of being stuck.

## Human evidence: behaviour and neural recordings

Inspection labels below describe what was actually checked. **Full relevant text** means relevant methods/results were inspected, not every analysis independently reproduced. **Abstract/preview** claims remain provisional because their detailed methods were not checked. **Partial pages** names the inspected portion.

| Specific study and inspection | What was measured and found | What it supports; generalization limit |
|---|---|---|
| [Metcalfe & Wiebe (1987)](https://doi.org/10.3758/BF03197722). Full author PDF; methods. | Subjective warmth ratings at 15-second intervals during insight and comparison problems. Perceived approach to insight solutions was less incremental. | Sudden subjective discovery can coexist with unreported change. Warmth is not an objective progress or neural measure; sampling also misses faster changes. |
| [Bowden & Beeman (1998)](https://doi.org/10.1111/1467-9280.00082). Full author PDF. | Naming/recognition of laterally presented solution words after attempts at verbal problems, including unsolved problems; solution priming was stronger with left visual field/right hemisphere presentation. | Solution-related accessibility can exist without overt solution. There was no continuous within-impasse recording or demonstration that every primed problem would later be solved spontaneously. |
| [Knoblich, Ohlsson & Raney (2001)](https://doi.org/10.3758/BF03195762). Full relevant author-uploaded article text; methods/results. | Eye position at 1,000 Hz in 24 people solving matchstick problems. Analyses aggregated fixation duration and location over three equal thirds of each attempt; successful solvers shifted long-fixation attention toward crucial elements late in solving. | Direct pre-response attentional change in classic puzzles. Third-wise group comparisons cannot distinguish a smooth individual ramp from differently timed jumps. Increasing fixation duration also occurred without success, so it is not itself progress. |
| [Ellis, Glaholt & Reingold (2011)](https://doi.org/10.1016/j.concog.2010.12.007). **Abstract/publisher preview only.** | Anagram eye tracking: relative attention to an irrelevant consonant declined several seconds before solution, with and without reported insight. | Reported evidence of a behavioural precursor; aggregate gaze is an attention proxy. Detailed individual trajectories and analysis robustness were not verified here. |
| [Tseng et al. (2014)](https://doi.org/10.1016/j.tsc.2014.04.004). Full relevant university-hosted PDF; results/figures. | Matchstick gaze percentages over attempt thirds; successful groups increasingly attended to the key region. A separate randomized experiment manipulated attention with animations and changed solution rates. | Adds behavioural change and a causal effect of an attention manipulation. Hints can convey solution information; neither manipulation nor coarse group trajectory establishes an unconscious, continuous neural mechanism. Internal table/reporting discrepancies warrant caution. |
| [Bilalić et al. (2021; online 2019)](https://doi.org/10.1080/13546783.2019.1705912). Full author PDF; Appendix C visually checked. | Among **26 unhinted solvers**, gaze trajectories were classified as **54% incremental, 27% sudden and 19% unclassifiable**. Three raters judged trajectories; a fourth resolved conflicts. | Stronger evidence that individual behavioural trajectories can differ within one puzzle. Classification uses time bins and visual judgement; it is not neural measurement. The incremental/sudden groups' perceived-suddenness contrast was **p = .06**, not conventionally significant. |
| [Cushen & Wiley (2012)](https://doi.org/10.1016/j.concog.2012.03.013). **Abstract/publisher preview only.** | Behavioural restructuring patterns with/without solution cues: individual patterns could appear insight-like while aggregation and cues yielded more incremental patterns; subjective insight did not reliably track trajectory classification. | A methodological counterweight to reading averaged curves as continuous learning. Detailed task measures and trajectory fits were not audited; use as supporting evidence, not a definitive trajectory estimate. |
| [Rose, Haider & Büchel (2010)](https://doi.org/10.1093/cercor/bhq025). Full relevant author PDF; Fig. 3 checked. | Coloured-square comparisons contained a hidden response regularity. Ventral striatal/right ventrolateral prefrontal BOLD and task-related EEG gamma coherence increased in a **ten-trial window** before an abrupt reaction-time decrease. | Biological neural precursors to exploiting a regularity. Windowed differences do not establish a monotonic ramp throughout an impasse, nor identify precisely when awareness began. Findings are task-specific; EEG and fMRI have different observation properties. |
| [Schuck et al. (2015)](https://doi.org/10.1016/j.neuron.2015.03.015). Full relevant author PDF; Figs. 2–3 checked. | Of 36 participants, **11** spontaneously adopted a newly useful colour strategy. Colour information was decodable in medial prefrontal fMRI in **two blocks before switching**, roughly five minutes. | Content relevant to a future policy precedes its overt use. Blockwise BOLD cannot decide whether individual neural changes were smooth or abrupt. Participants already succeeded with the old strategy; this is spontaneous optimization, not a classic failure impasse. |
| [Jung-Beeman et al. (2004)](https://doi.org/10.1371/journal.pbio.0020097). Full relevant primary HTML/PDF. | Remote-associate solutions rated insightful had a right temporal EEG gamma burst about **0.3 seconds before the button press**, with earlier posterior alpha differences; a separate fMRI experiment implicated right anterior temporal cortex. | A fast solution-associated event can coexist with earlier state changes. Response-aligned averages and self-report do not locate exact awareness onset or prove the whole brain made an instantaneous transition. |
| [Townsend et al. (2026)](https://doi.org/10.1016/j.cub.2026.04.021). Full relevant repository PDF; Figs. 3–4 and changepoint methods checked. | Trial-wise aiming in a visuomotor-rotation analogue and reanalysed reaching datasets: baseline-like aims were followed by a single-trial compensatory-magnitude shift; direction errors persisted. Pre-shift variability/error-correction tests generally found no positive precursor. | Direct evidence against gradual **expressed aiming** in these tasks. “Aha” was operationalized using the first detected aiming changepoint, not a recorded neural/subjective onset. Null tests do not rule out covert learning. The favoured hidden-state model beat specified alternatives; it does not prove its latent states exist in brains. |
| [Löwe et al. (2024), human component](https://doi.org/10.1371/journal.pcbi.1012505). Full relevant primary text/PDF; Fig. 2 checked. | Motion decisions acquired a hidden predictive colour cue. In the final sample of **99**, sigmoid steepness relative to a control classified **49** as showing abrupt improvement; many also reported colour use. | Direct behavioural evidence for heterogeneous switches. Performance criterion excluded many recruits, limiting prevalence estimates. There were **no biological neural recordings**; the accompanying model's hidden weights belong in the analogy section. |

## Animal evidence: early representation, abrupt switching and latent competence

| Specific study and inspection | What was measured and found | What it supports; generalization limit |
|---|---|---|
| [Durstewitz et al. (2010)](https://doi.org/10.1016/j.neuron.2010.03.029). **Primary abstract only.** | Rat medial prefrontal neurons recorded simultaneously during set shifting; trial-wise ensemble activity often transitioned abruptly near behavioural rule acquisition. | Direct neural transition evidence as reported, with provisional methodological confidence here. Does not show that earlier synapses or other regions were unchanged, or establish animal conscious insight. |
| [Karlsson, Tervo & Karpova (2012)](https://doi.org/10.1126/science.1226518). **Author-lab abstract only.** | Rat medial prefrontal ensemble recordings after contingency changes: coordinated reset on abandoning a policy, followed by elevated volatility during exploration. | Reported abrupt neural reset concerns **abandonment/entry into uncertainty**, not necessarily discovery of the correct solution. Detailed controls were not checked. |
| [Powell & Redish (2016)](https://doi.org/10.1038/ncomms12830). Full relevant primary HTML; Results/Methods. | Rat medial prefrontal lap-wise firing-vector correlations and transition scores during forced and volitional strategy changes, with path-matching controls. Representational transitions preceded behavioural changes; the volitional task's transition signal appeared approximately **5–8 laps earlier**. | Earlier neural change and abrupt state transitions coexist. Their distinct states and transition probabilities are not a demonstrated continuous solution ramp. Small animal samples and trained strategies limit generalization to novel human impasses; internal strategy remains inferred. |
| [Hasz & Redish (2020)](https://doi.org/10.1016/j.nlm.2020.107215). Full relevant author-PDF text via web reader; §3.3–3.6/Methods, no local figure-image audit. | Simultaneous rat dorsomedial prefrontal and hippocampal CA1 ensembles: lap-wise rule decoding and cluster/changepoint analysis. Prefrontal transitions tended to precede behaviour, while CA1 timing was closer to behavioural updating. Separate analyses detected rule-independent representational drift. | Timing differs across recorded regions. Lap-level analysis cannot resolve sub-lap changes; changepoint fitting is not proof of discontinuous synaptic learning. **Drift is measurable change, not automatically useful hidden progress.** |
| [Siniscalchi et al. (2016)](https://doi.org/10.1038/nn.4342). Full relevant author PDF/methods. | Mouse secondary motor cortical two-photon calcium signals and licking choices. Transitions into sound-guided responding were relatively abrupt and preceded recovery; transitions toward repetitive responding were slower/delayed. | Neural/behavioural timing and trajectory depend on switch direction. Familiar mapping retrieval differs from new insight; calcium filtering and fitted transition definitions constrain apparent timing. |
| [Kuchibhotla et al. (2019)](https://doi.org/10.1038/s41467-019-10089-0). Full relevant primary XML. | Discrimination in reinforced trials versus unrewarded probes in mice, rats and two ferrets. Probe competence appeared before ordinary reinforced performance reached expertise. | Direct evidence that poor performance can conceal learned discrimination. Probe context can alter motivation/control, and two ferrets provide limited species generalization. Biological neural weights were not recorded; the network account is modelling. |
| [Drieu et al. (2025)](https://doi.org/10.1038/s41586-025-08730-8). **Partial final author PDF: first two pages rendered/read.** | Mouse auditory task, knowledge probes, auditory-cortical calcium and optogenetics. The inspected portion reports early reward-prediction signals and slower action-suppression/performance changes. | Supports acquisition/expression separation in associative learning. **Full causal methods and later figures were not verified in this review**; do not use this row as a fully audited causal account of insight. Early reward prediction is not necessarily correct-solution progress. |
| [Rosenberg et al. (2021)](https://doi.org/10.7554/eLife.66175). Full relevant primary XML; discontinuous-learning Results and rate-fit Methods. | Infrared video/pose tracking of mouse maze routes, rewards and long direct paths. At least **5 of 10 rewarded mice** showed sharply timed increases in long-path rate; other mice improved more gradually. | Animal behaviour exhibits both trajectories beyond simple rule switching. Rate-model fits resolve minutes, not instantaneous events. No neural activity or conscious Aha was measured; the interpretation as a cognitive-map reorganization is not uniquely established. |

## Related observations that do not establish solution-specific progress

[Kounios et al. (2006)](https://doi.org/10.1111/j.1467-9280.2006.01798.x), **primary abstract only**, measured EEG/fMRI **before problem presentation** that predicted later reported insight versus analytic solving. This is preparatory-state evidence, not accumulation toward an unseen answer.

[Stuyck et al. (2024; online 2023)](https://doi.org/10.1177/17470218231202519), **primary abstract only**, measured vagally mediated heart-rate variability before/during/after remote-associate solving in 68 people. Task-related autonomic change is not a direct prefrontal recording or a solution-content trajectory. The recent theory paper that cited this work did not turn it into direct neural-ramp evidence.

## Models and analogy, separated from brain evidence

| Study and inspection | What was measured/modelled | What follows, and what does not |
|---|---|---|
| [Nanda et al. (2023)](https://arxiv.org/abs/2301.05217). Primary PDF; relevant mechanism/results. | Checkpoints, activations, Fourier circuit metrics and ablations in small transformers learning modular addition. A generalizing circuit formed before conspicuous test improvement; **the sharp test-accuracy rise occurred during cleanup**, as memorizing components weakened. | Direct hidden-mechanism evidence in those artificial networks. This is a possibility demonstration, not evidence that biological insight uses Fourier circuits or the same learning dynamics. |
| [Löwe et al. (2024), network component](https://doi.org/10.1371/journal.pcbi.1012505). Relevant primary model methods/results. | In regularized gated networks, relevant weights changed before a sharp gate/behaviour switch. | A hybrid mechanism can produce behaviour resembling the human task. Those hidden weight trajectories were measured in the **model**, not the human participants. Similar output does not identify the biological mechanism. |
| [Reddy (2022)](https://doi.org/10.1073/pnas.2215352119). Relevant primary XML/PNAS Results, experimental reanalysis and Methods. | RL simulations/analysis produced sequential reinforcement waves and sudden end-to-end performance. Reanalysis of Rosenberg's mouse routes showed later improvements for longer routes, consistent with the model. | Separate **direct behavioural reanalysis** from **inferred reinforcement dynamics**. No neural wave was recorded; the original data are reused, not independent replication. A sudden maze-performance jump therefore does not uniquely support a sudden global cognitive-map discovery. |
| [Doulfoukar, Pezzulo & Stuyck (2026)](https://doi.org/10.3758/s13423-026-02983-8). Primary abstract and relevant task/model description; not a full simulation audit. | Active-inference simulations of modified card sorting represent insight through Bayesian model reduction and changes in model confidence. | A current theoretical alternative, published 17 September 2026. Simulated confidence and replay proposals are not measurements of human awareness, biological dopamine or hidden neural progress. |

A methodological exclusion also matters: [Graf et al. (2023)](https://doi.org/10.3390/jintelligence11050086), full relevant PDF inspected, uses **simulated** data for its sudden-shift illustration (footnote 2). Its empirical reanalysis concerns the Bilalić dataset, so it is not independent replication. The illustration does not count as direct biological evidence.

## What the combined evidence actually establishes

**Established within the measured tasks:** some solution-relevant behavioural change precedes response; relevant neural representations can precede strategy expression; sampled neural populations can switch rapidly; probe competence can precede normal task proficiency. Powell, Hasz and Siniscalchi make the coexistence of neural precedence and rapid switching especially clear. The human gaze studies support behavioural change during attempts, with heterogeneous individual patterns and important averaging limitations.

**Reasonable inference:** different combinations of acquisition, exploration, representation and expression can generate similar sudden performance curves. There is no single trajectory that these studies establish for all insight.

**Speculation:** gradually changing synapses may drive a later population-state transition or awareness threshold. Existing activity recordings and behavioural fits generally do not observe those synapses, and several mechanistically different models fit abrupt outputs.

**Measurement limitation:** BOLD and calcium filter time; lap/block analyses miss faster changes; averaging differently timed steps can yield a ramp. Conversely, aligning data to a fitted changepoint emphasizes a discontinuity. Detecting no significant precursor is weaker than demonstrating a preregistered bound on a meaningful precursor. No one measure warrants “the brain was unchanged until the Aha.”

## What remains unknown, and the experiment that would settle it

We do not know how often real human impasses involve useful accumulation, an earlier discrete discovery with delayed expression, already acquired but suppressed knowledge, or unproductive exploration. We lack a general causal link between synaptic learning, population states, strategy adoption and conscious recognition. The evidence is strongest for short, constrained laboratory tasks; days-long scientific or personal breakthroughs remain a major generalization gap. Animal conscious experience is not established by these task signatures.

The decisive experiment would **prospectively track specific candidate solutions on individual attempts, then intervene before and during the switch**. Combine human puzzles and matched human/rodent rule-discovery tasks with continuous eye tracking and temporally precise neural recordings. Train locked content decoders on separate instructed-rule trials and test held-out discoveries, including incorrect and never-solved attempts. Measure knowledge, strategy use and human Aha reports separately, with sparse-probe/no-probe controls.

Compare gradual accumulation, discrete transition, hybrid accumulation-plus-switch, contextual gating and sequential local-learning models using held-out predictions and observation models for filtering. Simulated positive controls must show that the analysis can recover meaningful ramps and steps; null conclusions require prespecified equivalence bounds. In animals, randomly interrupt a decoded precursor versus the transition, with movement, reward and arousal controls, and test later knowledge and transfer.

A solution-specific ramp whose selective interruption delays later discovery would support hidden accumulation. A reliably resolved discrete transition with meaningful earlier ramps excluded would support abrupt change **in the sampled variables**. Early competent probes or different regional timing could favour gating or a hybrid mechanism. The [full experiment specification](NEXT_EXPERIMENT.md) adds a route-length/maze-topology test of sequential reinforcement. **It is a proposal: no experiment or study-data replication was run.** It could settle the competing mechanisms for the tested tasks and measurement scale; no finite recording can prove that every unobserved synapse was unchanged.


---

## File: EVIDENCE_LEDGER.md

# Evidence and inspection ledger — v2

Reading depth is separate from evidential strength. “Relevant text” does not imply complete statistical/supplement audit. Original-study data and published simulations were **not rerun**. Source files and figure renders stay local; all claims remain independently checkable through the primary links.

Codes: G = graded behavioural change; P = relevant precursor without demonstrated continuous accumulation; J = rapid measured transition; L = latent competence; S = preparatory/nonspecific state; A = model/analogy. Overlapping codes are intentional. An activity precursor is not a synaptic-strength trajectory.

| Study / primary identifier | Code | Precisely inspected | Important unresolved audit boundary |
|---|---|---|---|
| [Metcalfe & Wiebe 1987](https://doi.org/10.3758/BF03197722) | Subjective J | Author PDF; rating procedure and comparisons. | No objective content or neural trajectory. Retained v1 inspection. |
| [Bowden & Beeman 1998](https://doi.org/10.1111/1467-9280.00082) | P | Author PDF; lateralized solution-word tests. | Probe-derived accessibility; eventual spontaneous discovery not guaranteed. Retained v1 inspection. |
| [Knoblich et al. 2001](https://doi.org/10.3758/BF03195762) | G/P | [Author-uploaded full article text](https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving): Method; Eye Movement Data; crucial-element Results; Discussion. | Author text reproduced by web reader; no local original-figure audit. Springer preview and script download did not provide full article bytes. |
| [Ellis et al. 2011](https://doi.org/10.1016/j.concog.2010.12.007) | G/P provisional | Primary abstract/publisher preview only. | Full methods and single-attempt trajectory analysis unchecked. |
| [Tseng et al. 2014](https://doi.org/10.1016/j.tsc.2014.04.004) | G/P; attention intervention | University-hosted PDF: Experiments 1–2 methods/results; PDF pages 7, 9–10, table/animation/rate figures. | Table 2 says 12 successful participants while text reports 14; Table 5 percentages appear transposed for fixation/control despite counts and Fig. 7. Do not treat early reported significance as a validated classifier or infer a smooth individual ramp. |
| [Bilalić et al. 2021](https://doi.org/10.1080/13546783.2019.1705912) | G/J | Author PDF relevant methods/results; Appendix C, PDF pages 36–37 rendered/read in v2. | The residual class is retained. Suddenness contrast is borderline; gaze categories are observer judgements. |
| [Cushen & Wiley 2012](https://doi.org/10.1016/j.concog.2012.03.013) | G/J provisional | Primary publisher abstract/preview. | Task details and restructuring fits not independently inspected; aggregation warning retained provisionally. |
| [Rose et al. 2010](https://doi.org/10.1093/cercor/bhq025) | P | Author PDF relevant neural/behavioural methods/results; Fig. 3 rendered in v1. | Ten-trial window is not continuous whole-impasse progress. |
| [Schuck et al. 2015](https://doi.org/10.1016/j.neuron.2015.03.015) | P/J behaviour | Author PDF relevant methods/results; Figs. 2–3 rendered in v1. | Block-level content decoding cannot establish individual smoothness. |
| [Jung-Beeman et al. 2004](https://doi.org/10.1371/journal.pbio.0020097) | P/J | Primary HTML/PDF relevant EEG/fMRI methods/results. | Response alignment and report latency differ from awareness onset. |
| [Townsend et al. 2026](https://doi.org/10.1016/j.cub.2026.04.021) | J behaviour; model | [Repository PDF](https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf): aiming Results, null pre-shift tests, model comparison, STAR changepoint methods; PDF pages 6, 8, 17 rendered/read. | First changepoint defines “Aha”; supplementary detection penalty differs. Model-fit totals combine original/reanalysed datasets. [Public code/data](https://github.com/Max-Townsend/aha_precedes_strategy_VMR) located, not executed. |
| [Löwe et al. 2024](https://doi.org/10.1371/journal.pcbi.1012505) | J human / P-J artificial | Primary HTML/PDF relevant human sample/classification and network gate/weight methods/results; PDF page 7 (Fig. 2) rendered/read. | Selected human sample; model weights are not human neural measurements. Supplements not exhaustively audited. |
| [Durstewitz et al. 2010](https://doi.org/10.1016/j.neuron.2010.03.029) | J provisional | Primary abstract only; publisher full access unavailable. | Exact transition/control methods not verified here. |
| [Karlsson et al. 2012](https://doi.org/10.1126/science.1226518) | J provisional | Author-lab abstract only. | Policy abandonment, not demonstrated correct-solution acquisition; full controls unchecked. |
| [Powell & Redish 2016](https://doi.org/10.1038/ncomms12830) | P/J | Primary full HTML: forced/volitional Results, path controls, population-vector transition-score Methods and Discussion. | Neural lead does not imply gradualness or establish necessity. No local figure-image audit. |
| [Hasz & Redish 2020](https://doi.org/10.1016/j.nlm.2020.107215) | P/J; drift | [Author PDF](https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf) via primary web text: relevant Methods and §3.3–3.6. | Local download 403; figure text read, figure images not visually audited. Lap-level comparison limits precise lead estimates. |
| [Siniscalchi et al. 2016](https://doi.org/10.1038/nn.4342) | P/J | Author PDF relevant task/imaging and transition methods/results. | Familiar mapping, direction effects and calcium observation model. Retained v1 inspection. |
| [Kuchibhotla et al. 2019](https://doi.org/10.1038/s41467-019-10089-0) | L | Primary XML relevant probe/task results and methods. | Biological behaviour and explanatory model kept distinct. Retained v1 inspection. |
| [Drieu et al. 2025](https://doi.org/10.1038/s41586-025-08730-8) | P/L provisional | Final author-hosted image-only PDF, **pages 1–2 only** rendered/read in v1. | Empty extraction; failed final XML request again in v2. Full causal methods/later figures unchecked. |
| [Rosenberg et al. 2021](https://doi.org/10.7554/eLife.66175) | J/G behaviour | Primary full XML: Discontinuous learning; Statistics of sudden insight rate-fit Methods; Discussion and sample/task context. | No neural recordings. Rate fits and post-hoc event detection do not locate instantaneous learning. |
| [Kounios et al. 2006](https://doi.org/10.1111/j.1467-9280.2006.01798.x) | S provisional | Primary abstract only. | Prep state reclassified out of solution-progress category. |
| [Stuyck et al. 2024](https://doi.org/10.1177/17470218231202519) | S provisional | Publisher abstract only; first online 2023. | Autonomic proxy, not direct prefrontal recording or within-puzzle solution-content slope. |
| [Nanda et al. 2023](https://arxiv.org/abs/2301.05217) | A | Primary PDF relevant circuit analysis/ablation and phase descriptions. | Accuracy rise assigned to cleanup; no biological inference. |
| [Reddy 2022](https://doi.org/10.1073/pnas.2215352119) | A / direct behavioural reanalysis | Primary XML and PNAS relevant RL Results, Experimental Tests, Materials/Methods. | Reuses Rosenberg data; model dynamics are inferred, not recorded biological signals. |
| [Doulfoukar et al. 2026](https://doi.org/10.3758/s13423-026-02983-8) | A; limited audit | Primary abstract and relevant task/model description/publication metadata. | No new biological measurements; complete simulation/supplement audit not performed. |
| [Graf et al. 2023](https://doi.org/10.3390/jintelligence11050086) | Methodology; exclude illustration | PDF relevant methods/footnote 2 and distinction between simulated illustration and empirical reanalysis. | Same Bilalić dataset; neither simulated curve nor reanalysis is an independent biological replication. |

## File retrieval is a different audit

`SOURCE_LIST.json` declares downloadable **resources**, not all cited studies: some claims were inspected through primary abstracts/web readers only, and Drieu has PDF and XML resource IDs. `source_manifest.json` is the deduplicated current cache view. `retrieval_attempts.jsonl` preserves actual v2 script/manual attempts, including DNS restrictions, 403 responses, timeouts and XML failure. A failed local download can coexist with primary text inspected through the web reader; the table states which route was used.

`SOURCE_HISTORY_V1.json` preserves all 15 original records unchanged, including failures/alternate sources. The v2 script does not pretend to reproduce unlogged v1 searches or all manually acquired v1 bytes. Reading provenance is in this ledger; a saved file is not a verified claim.


---

## File: NEXT_EXPERIMENT.md

# A discriminating experiment

Proposal only; no participants or animals tested and no data collected.

Use homologous human and rodent rule-discovery tasks, plus human anagram and constraint-relaxation puzzles. Establish an old strategy that initially fails after a hidden relation changes. Keep standard sensory inputs and motor outputs matched. Treat repeated failure/no improvement as an operational impasse; human subjective stuckness is a separate variable.

Record continuous human MEG/EEG and eye tracking (intracranial activity only where already clinically appropriate), and multi-region rodent electrophysiology including frontal, sensory, hippocampal, and striatal sites. Record stimulus, choices, reaction times, candidate answers, pupil/arousal, movement, reward expectation and timing. Neural activity is the primary measure; activity is not a direct synaptic-strength assay.

Randomize trials/cohorts to sparse neutral probes versus no probes. A probe asks for knowledge or confidence without revealing the solution, but could still teach or redirect attention; quantify this reactivity. Include no-report/delayed-report conditions and independently calibrated response delays. Differentiate task knowledge from correct use of the new policy and from human Aha phenomenology.

Train a content decoder using independent instructed-strategy and known-solution trials. Lock analysis and test on held-out individuals/problems. Do not fit a decoder to a trial's post-solution data and then claim it prospectively predicts that same trial. Decode the specific new rule or correct candidate, not just global effort or arousal. Also decode incorrect alternatives.

Compare matched-complexity state-space models on individual trials: (1) accumulation plus an output threshold, (2) discrete neural-state transitions with no meaningful pre-transition content ramp, (3) gradual acquisition plus a discrete policy/representation transition, (4) latent knowledge with contextual gating, and (5) shuffled/artifact controls. Fit the observation model to actual temporal filtering in BOLD/calcium/EEG preprocessing. Preserve failed, unsolved, and false-insight trials. Avoid time normalization and solution alignment as the sole analysis. Prefer held-out predictive likelihood to visually assessing curves.

Use online neural content estimates to trigger randomized animal perturbations. Inhibit candidate precursor activity during poor-performance periods and compare with time-matched, state-matched, off-target and motor/reward/arousal controls. Test later transfer and knowledge probes after the perturbation, not just immediate performance. Perturb near the neural transition in separate trials to distinguish acquisition effects from expression effects. Closed-loop randomization must account for selection by the trigger.

Predictions and weakening conditions:

- A prospective solution-specific ramp that predicts both solution content and transition timing, and whose selective disruption delays later discovery/transfer, weakens the pure abrupt/no-progress model.
- A discrete neural jump with preregistered equivalence bounds ruling out a biologically meaningful ramp in adequately sampled populations weakens the continuous-only model at that measurement scale.
- A content ramp in one circuit with a fast policy transition in another, with distinct perturbation effects, favors a hybrid mechanism.
- Correct knowledge revealed early by context change, without new training, favors acquisition/expression gating; persistent probe effects would expose a probe-induced-learning alternative.

This could adjudicate mechanisms within the tested task family. It cannot prove that no unrecorded neuron, synapse, or biochemical variable changed, or settle every kind of real-world insight. Replication across tasks and species is required for broader generalization.

## V2 additions: distinguish local learning from a global switch

Include a sequential-local-learning alternative explicitly, motivated by [Reddy (2022)](https://doi.org/10.1073/pnas.2215352119). In the animal maze arm, vary tree versus densely connected topology and start-to-goal distance while matching exposure and motor difficulty as far as feasible. Track individual junction choices and short-route competence before the long end-to-end route improves. Compare staggered content/value changes from near-goal to distant junctions against a simultaneous global rule/map transition. Abrupt end-to-end accuracy alone is not an identifying observation.

Calibrate detection before testing a null. Use separate pilot/instructed-rule recordings to specify the smallest precursor magnitude and duration that would materially affect the mechanism. Choose animal/session and human/problem counts by prospective power/model-recovery simulation rather than inventing an evidence-free sample size. Inject synthetic ramps and steps into realistic recordings, including observation filtering, drift and missing trials; lock analysis only after adequate recovery. Report uncertainty and equivalence bounds, and state which unobserved variables remain unconstrained.

Estimate switch timing prospectively from held-out observations where possible. If a changepoint is fitted to the same output used to display the “jump,” use null/model simulations to measure the alignment-induced effect. Include models with equalized complexity and compare out-of-sample predictive performance; the best of three selected models is not automatically the true mechanism.

Recruit tasks with independently measured failure/stuckness alongside tasks in which the old policy still works. This separates optimization from genuine impasse. Decode incorrect hypotheses and competing policies, not just the eventual successful one. An intervention that changes arousal, attention, reward expectation or expression without changing later knowledge should not be called selective disruption of acquisition.

All additions remain **unrun proposals**. Published data/code were located for some studies, but no original study analysis or simulation was replicated during the v2 literature rerun.


---

## File: LAB_NOTEBOOK.md

# Lab Notebook

Investigation started 2026-09-30. Previous notebook preserved in research/2026-09-30-hidden-progress/previous-LAB_NOTEBOOK.md.

## Current Question

During apparent impasse before human insight or animal strategy change, does measurable progress precede the transition, or are neural transitions also abrupt?

## Current Model

Mixed, task-dependent account. Acquisition, neural representation, policy expression, and conscious report can have distinct time courses. Behavioral ramps, neural precursors, abrupt ensemble transitions, and context-gated latent knowledge are all observed within specific tasks. No universal mechanism established.

## Competing Hypotheses

H1: Continuous solution-specific accumulation precedes abrupt report/output.
H2: Discrete representational transition produces abrupt neural and behavioral change.
H3: Mixed: gradual learning enables a discrete transition; context gates expression.
H4: Apparent ramps or jumps arise from averaging, response alignment, filtering, or selection.

## Assumptions

Animal rule switching is comparable to some human strategy change, but animal Aha phenomenology cannot be inferred. Neural activity is not identical to synaptic learning. Lack of detected progress is not proof of none.

## Experiments Run

Registered primary-source literature audit: extract task, measure, time resolution, precursor type, directness, and generalization. No new biological experiment. Preserve source search results and an evidence ledger.

## Results

Primary evidence adjudicated in research/2026-09-30-hidden-progress/EVIDENCE_LEDGER.md. Strong behavioral graded precursors: Ellis 2011 and Bilalic 2021. Human neural precursors: Rose 2010 and Schuck 2015, with coarse time resolution and limited generalization. Fast neural events/transitions: Jung-Beeman 2004, Durstewitz 2010, Karlsson 2012, Siniscalchi 2016. Latent task knowledge and causal acquisition/expression dissociation: Kuchibhotla 2019 and Drieu 2025. Nanda 2023 kept as artificial-system analogy.

## Failed Approaches

None yet. Search snippets count only as leads; full text preferred, abstract-only limitations explicit.

## Surprises / Anomalies

Pending.

## Strongest Evidence For

For hidden progress: solution-relevant gaze changes in Ellis 2011; individual gradual trajectories in Bilalic 2021; rule-relevant MPFC decoding before strategy shift in Schuck 2015; task-specific BOLD/EEG coherence before abrupt output in Rose 2010. Latent knowledge: contextual probes in Kuchibhotla 2019 and cortical imaging/perturbation in Drieu 2025.

## Strongest Evidence Against

Against universal gradual representation change: abrupt recorded rat frontal ensemble shifts in Durstewitz 2010 and Karlsson 2012; individual abrupt gaze patterns coexist with gradual ones in Bilalic 2021. Against universal neural/behavioral synchrony: Siniscalchi 2016 neural transition precedes recovery; Schuck 2015 precursor precedes behavioral change. These do not rule out unseen synaptic accumulation.

## Kill Zones

H1 weakened by adequately powered single-trial absence of a meaningful ramp plus a discrete neural jump. H2 weakened by prospective solution-specific precursor predicting time and content before report. H3 must outperform simpler models on held-out trials. H4 weakened by independently replicated raw/single-trial results with leakage controls.

## Robust Findings

1. Subjective suddenness does not demonstrate absence of earlier objective change.
2. Earlier brain activity is not automatically solution-specific progress.
3. Some population transitions are genuinely fast at recorded trial resolution.
4. Learning and behavioral expression are dissociable.
5. Group averaging and measurement filtering can alter apparent trajectory shape.

## Speculative Interpretations

Thresholded accumulation and metastable attractor switching are candidates, not findings.

## Newly Discovered Abstractions

Separate acquisition from expression; separate precursor state from solution content.

## Next Best Experiment

Prospective solution-content decoding with independent training data, individual-trial ramp/change-point/hybrid model comparison, context/no-report/probe controls, and randomized closed-loop rodent perturbations. Full proposal: research/2026-09-30-hidden-progress/NEXT_EXPERIMENT.md. A new toy simulation would not adjudicate biological mechanisms and was not run.

## Confidence / Remaining Uncertainty

High that both hidden precursors and abrupt sampled-population transitions exist within these task families; moderate on a mixed organizing interpretation; low on prevalence or a universal neural mechanism. Unknown whether each precursor is causal/necessary, whether synaptic changes are continuous, and how results generalize to long natural impasses.

## Audit update, 2026-09-30

- Verified Schuck 2015: color decoding in MPFC in two 84-trial blocks (~5 minutes) before behavioral switch; small switching subset (11/36); blockwise decoding does not establish a smooth single-trial ramp.
- Verified Rose 2010: VLPFC/ventral striatal BOLD and task-specific EEG coherence changes in ten pre-transition trials; early neural change, not proof of monotonic learning throughout impasse.
- Important negative result: Graf et al. 2023 uses simulated data to illustrate its abrupt pre-solution shift (footnote 2). Do not treat that illustration as biological evidence of abrupt insight. Original Bilalic data show gradual change; inspect original.
- Drieu 2025 author-hosted PDF downloaded, but pypdf extracted no substantive text (36 image pages). Retain as scanned source; render and inspect rather than treating file presence as verification. Earlier PMC11195094 is a 2024 preprint, not the final 2025 article.
- Full-text access failures: PMC browser checks, some publisher access failures, Gallistel author PDF timeout. Alternative author/repository sources used where possible; failures preserved in source_manifest.json.

## Completed source audit, 2026-09-30

Final synthesis uses a focused selection of primary studies, not an exhaustive systematic review. Full text was inspected for the key human neural-precursor papers. Ellis 2011, Kounios 2006, Durstewitz 2010 and Karlsson 2012 were verified at primary-abstract/preview level; no unavailable sample sizes or detailed dynamics are asserted. Bilalic 2021 (online 2019) supplies empirical individual gradual and sudden gaze patterns. Drieu final 2025 PDF first two pages were rendered and read, including final abstract and acquisition/expression figure. No new biological experiment or causal claim about human insight was made. Sources, hashes, exclusions, prior notebook and proposed experiment are preserved.

## Sharing handoff, 2026-09-30

Prepared share/FULL_RESEARCH.md and hidden-progress-research.zip under this inquiry directory. Includes full answer, evidence ledger, current-inquiry notebook snapshot, proposed experiment, retrieval code and manifest; excludes unrelated prior notebook and third-party full texts. Verified SHA256 integrity and ZIP contents. GitHub connector lacks repository/Gist creation capability; browser is signed out. Publishing awaits user login, requested asynchronously. No public URL yet.

## Publication completed, 2026-09-30

Public repository: https://github.com/jorgy72/hidden-progress-insight-research
Complete raw text: https://raw.githubusercontent.com/jorgy72/hidden-progress-insight-research/main/FULL_RESEARCH.md
Commit: a0dad4503c621923d42299cf8fdc377c3d13d03b. GitHub file content checked against local package; anonymous web retrieval succeeded. Alternate Sites project registered while login was unavailable but not published; GitHub became available after user signed in. Public package includes inquiry content only.

## External review and workflow revision, 2026-09-30

The user supplied an Opus review and requested adoption of useful workflow considerations. Review is testimony/leads, not automatic verification. Response: research/2026-09-30-hidden-progress/REVIEW_RESPONSE.md. Structured follow-up search log: SEARCH_LOG_REVIEW.jsonl in that directory.

Accepted workflow changes: explicit query/selection history; coverage mapping; backward/forward anchor citation chasing and recent-literature checks; stopping supported by batch yield and unresolved coverage; verification visible at each report claim; evidence-category and stage-order audits; idempotent retrieval with preserved attempt history; complete handoff; independent critic when available/authorized, otherwise honestly labelled self-review.

Important correction to Current Model/Confidence: the broad mixed account remains plausible, but the v1 coverage and low-information-gain stopping claim were insufficiently supported. Powell & Redish 2016 directly adds neural transitions before behavioral change; their individual transitions can themselves be abrupt, so temporal precedence is not evidence of a smooth ramp. Relevant Knoblich 2001 and Townsend 2026 were omitted. This follow-up inspected Powell publisher results/discussion, the other two primary abstracts, and local Nanda phase-order text. It does not complete a v2 source audit.

Search-log critique qualified: a raw local search-results file existed but was omitted from public handoff and lacked an adequate exact-query/selection trail. Do not invent that missing history. Existing retrieval script still needs repair and repeat-run validation; report still needs category/verification/residual-group/timing corrections. Original v1/public commit preserved. WORKFLOW.md and research/LITERATURE_AUDIT_TEMPLATE.md updated locally. No revised public report or independently reviewed v2 claimed.

## Version 2 registered, 2026-09-30

User requested rerun and GitHub publication. Search plan: research/2026-09-30-hidden-progress/v2/SEARCH_PLAN.md. Reopen coverage, inspect the three missing primary studies, chase anchors backward/forward, search current literature, expose inspection depth, repair/retest retrieval and conduct clearly labelled skeptical self-review. Preserve original public commit and publish a dated change log. Original Opus critique is independent feedback on v1; no independent review of v2 yet.

## V2 expanded evidence and revisions, 2026-09-30

Query batches B1-B5 and primary selection/access decisions preserved under research/2026-09-30-hidden-progress/v2. Backward Bilalic leads added Knoblich, Tseng and Cushen; targeted forward strategy coverage added Powell, Hasz and Lowe. Animal-task coverage added Rosenberg and Reddy's competing RL reanalysis. Recent boundary checks included Townsend, a September 2026 active-inference theory, autonomic evidence and the 2025 visual-insight/memory study.

Established at task/measurement scale: neural change before output does not imply a gradual ramp; regional timing differs; behavioural trajectories are heterogeneous; context can expose knowledge before routine performance. Inference: multiple mechanisms generate sudden output. Speculation: gradual synaptic accumulation triggers later population/awareness switching. Unknown: prevalence and causal mechanism during genuine prolonged human impasse.

Negative/access results retained: sandbox DNS failures; author-site 403 for Hasz and ResearchGate download; repository timeout before successful Townsend retry; repeated Drieu XML 500; CAPTCHA/client-challenge routes did not supply article text. Full primary content read through another route is distinguished from local byte retrieval. Drieu remains first-two-pages only. Hasz relevant PDF text was read but local figure images were not audited.

Audit corrections: restored Bilalic unclassifiable group and p=.06 boundary; retained simulated-versus-empirical Graf distinction; corrected Nanda cleanup stage; isolated preparation/autonomic signals; split model weights from human measures and Reddy's reanalysis from inferred dynamics; flagged Tseng internal table inconsistencies. No new original-study analyses run.

Retrieval instrument: stable resource declarations/current cache separated from dated attempts and unchanged v1 history; content-addressed refresh prevents overwriting earlier bytes. Four offline tests passed covering repeat-run identity, access challenges/retry, corrupt cache/unknown IDs, duplicate declarations and failed-refresh retention. A real default rerun used only valid caches or skipped recorded failures, with no new attempts. V2 stopping is bounded coverage, not low-yield/saturation. Separate skeptical self-review completed; no independent v2 review claimed. Publication still pending at this notebook entry.


---

## File: SEARCH_PLAN.md

# Version 2 search plan

Registered 2026-09-30 before the new search batches. Focused evidence assessment; not a systematic review. Literature cutoff: 2026-09-30.

Question: Does measurable solution-relevant change occur during apparent impasse before sudden human insight or animal strategy change, and can measured neural transitions themselves be abrupt?

Include primary human/animal studies with temporally resolved behavior/neural measurements before solution or strategy change, contextual probes of latent task knowledge, and methodological studies needed to interpret ramps/jumps. Keep preparatory-state controls and artificial-network mechanisms separately. Exclude review assertions as direct evidence, simulated illustrative trajectories, purely post-solution contrasts as pre-solution evidence, unrelated generic plasticity, and duplicates of the same dataset as independent replication.

Coverage: human puzzle gaze/semantic access; human strategy discovery neural content/timing; animal rule switching neural timing; learning versus expression/latent knowledge; abrupt versus graded individual trajectories; current papers through cutoff. Each included source must have explicit inspection depth and measurement/generalization limits.

Anchor backward routes: Bilalic (matchstick predecessors), Schuck (spontaneous strategy), Durstewitz and Powell (rodent ensemble transitions), Kuchibhotla/Drieu (acquisition-expression). Forward routes: publisher references and targeted cited-paper searches; indexes cannot guarantee exhaustive citing coverage. Recent targeted search: 2024–2026 human insight and animal latent strategies.

Starting material leads: Powell & Redish 2016; Knoblich et al. 2001; Townsend et al. 2026. Recheck Bilalic residual group, Kounios taxonomy, Nanda stage order, and verification visibility. Repair retrieval and test cached reruns without network. Preserve original manifest as historical provenance.

Stopping: record each batch's new relevant candidates and interpretation changes, document remaining access/coverage gaps, and stop at a bounded focused scope rather than claiming exhaustive saturation. Material contradictory/new direct evidence triggers additional targeted audit. Proposed experiment remains unrun.

Review: original user-supplied independent Opus review drives corrections; v2 receives a separate skeptical self-review. No new independent critic is claimed unless one actually reviews v2.


---

## File: SEARCH_AUDIT.md

# Search, selection and stopping audit — v2

Cutoff: **30 September 2026**. Focused coverage audit, not a systematic review. Plan recorded before the expanded searches in [SEARCH_PLAN.md](SEARCH_PLAN.md). Exact search strings, service and filters are in [SEARCH_BATCHES.json](SEARCH_BATCHES.json); primary access/citation decisions are in [SEARCH_LOG.jsonl](SEARCH_LOG.jsonl). Logs contain routes and decisions, not copyrighted article excerpts.

The v1 retrieval manifest was not a search log. Its missing query/ranking history cannot be reconstructed reliably; we preserve it as history instead of inventing it. The separately preserved v1 files retain their original, now inadequate stopping assertion.

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

Scope limitations: one investigator; English-language targeted web searching; no comprehensive PsycINFO/Web of Science/Scopus export; no dual independent screening; incomplete raw search-result preservation; bounded citation chasing; no effect-size meta-analysis or study-data replication. The critic pass for this version is explicitly **self-review**, with Opus's earlier independent critique retained as v1 feedback.


---

## File: SEARCH_BATCHES.json

```json
[
  {
    "id": "B1",
    "date": "2026-09-30",
    "route": "missing-study retrieval and recent coverage",
    "service": "web search",
    "queries": [
      "\"Knoblich\" \"Ohlsson\" \"Raney\" 2001 eye movement pdf",
      "\"Townsend\" \"An Aha moment precedes\" pdf",
      "\"prefrontal\" \"latent\" \"strategy\" \"2026\" representation",
      "insight hidden progress gradual neural 2024 2025 2026 study"
    ],
    "filters": "none"
  },
  {
    "id": "B2",
    "date": "2026-09-30",
    "route": "primary-source retrieval; targeted forward citing searches of Schuck and Durstewitz",
    "service": "web search",
    "queries": [
      "\"Townsend\" \"An Aha moment precedes\" site:eprints.whiterose.ac.uk",
      "\"Knoblich\" \"An eye movement study\" site:link.springer.com",
      "\"Schuck\" \"2015\" \"Abrupt and spontaneous strategy switches\" neural networks",
      "\"Durstewitz\" \"2010\" \"Powell\" \"Redish\" strategy changes"
    ],
    "filters": "domains explicit in two query strings; none otherwise"
  },
  {
    "id": "B3",
    "date": "2026-09-30",
    "route": "backward leads from Bilalic; independent recent and animal-task coverage",
    "service": "web search",
    "queries": [
      "\"Tseng\" \"2014\" insight eye movements",
      "\"Cushen\" \"Wiley\" \"2012\" insight",
      "\"insight\" \"gradual\" \"neural\" \"2025\" \"2026\"",
      "\"Rosenberg\" \"2021\" mice maze sudden insight"
    ],
    "filters": "none"
  },
  {
    "id": "B4",
    "date": "2026-09-30",
    "route": "forward follow-up of Rosenberg; disambiguate backward title; recent boundary studies",
    "service": "web search",
    "queries": [
      "\"A reinforcement-based mechanism for discontinuous learning\"",
      "\"Cues to solution, restructuring patterns\" pdf",
      "\"Time-dependent deployment of medial prefrontal cortical representations in male mice\"",
      "\"From pre-stimulus preparation\" \"2026\" insight"
    ],
    "filters": "none"
  },
  {
    "id": "B5",
    "date": "2026-09-30",
    "route": "resolve screened memory lead identifier; no new core claim",
    "service": "web search",
    "queries": [
      "\"Insight predicts subsequent memory\" \"2025\""
    ],
    "filters": "none"
  }
]
```


---

## File: SEARCH_LOG.jsonl

```json
{"id":"B1","date":"2026-09-30","route":"missing-study retrieval and recent coverage","service":"web search","queries":["\"Knoblich\" \"Ohlsson\" \"Raney\" 2001 eye movement pdf","\"Townsend\" \"An Aha moment precedes\" pdf","\"prefrontal\" \"latent\" \"strategy\" \"2026\" representation","insight hidden progress gradual neural 2024 2025 2026 study"],"filters":"none","type":"query_batch"}
{"id":"B2","date":"2026-09-30","route":"primary-source retrieval; targeted forward citing searches of Schuck and Durstewitz","service":"web search","queries":["\"Townsend\" \"An Aha moment precedes\" site:eprints.whiterose.ac.uk","\"Knoblich\" \"An eye movement study\" site:link.springer.com","\"Schuck\" \"2015\" \"Abrupt and spontaneous strategy switches\" neural networks","\"Durstewitz\" \"2010\" \"Powell\" \"Redish\" strategy changes"],"filters":"domains explicit in two query strings; none otherwise","type":"query_batch"}
{"id":"B3","date":"2026-09-30","route":"backward leads from Bilalic; independent recent and animal-task coverage","service":"web search","queries":["\"Tseng\" \"2014\" insight eye movements","\"Cushen\" \"Wiley\" \"2012\" insight","\"insight\" \"gradual\" \"neural\" \"2025\" \"2026\"","\"Rosenberg\" \"2021\" mice maze sudden insight"],"filters":"none","type":"query_batch"}
{"id":"B4","date":"2026-09-30","route":"forward follow-up of Rosenberg; disambiguate backward title; recent boundary studies","service":"web search","queries":["\"A reinforcement-based mechanism for discontinuous learning\"","\"Cues to solution, restructuring patterns\" pdf","\"Time-dependent deployment of medial prefrontal cortical representations in male mice\"","\"From pre-stimulus preparation\" \"2026\" insight"],"filters":"none","type":"query_batch"}
{"id":"B5","date":"2026-09-30","route":"resolve screened memory lead identifier; no new core claim","service":"web search","queries":["\"Insight predicts subsequent memory\" \"2025\""],"filters":"none","type":"query_batch"}
{"id":"D0","route":"reviewer-supplied lead","study":"Powell & Redish 2016","url":"https://www.nature.com/articles/ncomms12830","decision":"include","reason":"Neural representation precedes behaviour; transitions can still be abrupt.","inspection":"relevant primary HTML Results/Methods/Discussion","date":"2026-09-30","type":"selection_or_access"}
{"id":"D1","route":"reviewer lead + B1/B2; Bilalic backward reference","study":"Knoblich et al. 2001","url":"https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving","decision":"include","reason":"Impasse-related gaze shifts before response; thirds/group analysis boundary.","inspection":"author-uploaded full article text through web reader; local request 403","date":"2026-09-30","type":"selection_or_access"}
{"id":"D2","route":"reviewer lead + B1/B2 repository retrieval","study":"Townsend et al. 2026","url":"https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf","decision":"include","reason":"Behavioural abruptness and precursor null tests; neural onset unmeasured.","inspection":"relevant PDF Results/STAR Methods; PDF pages 6,8,17 visually read","date":"2026-09-30","type":"selection_or_access"}
{"id":"D3","route":"B2 targeted forward search; direct Powell/Durstewitz citing text","study":"Hasz & Redish 2020","url":"https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf","decision":"include","reason":"Different regional strategy-transition timing; independent drift control.","inspection":"relevant Methods and sections 3.3-3.6 via web PDF text; local 403","date":"2026-09-30","type":"selection_or_access"}
{"id":"D4","route":"B2 targeted Schuck forward search; primary references checked","study":"Lowe et al. 2024","url":"https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012505","decision":"include split human/model","reason":"Human behaviour recorded; hidden weights exist only in model.","inspection":"relevant primary full text and PDF; human Fig 2 visually checked","date":"2026-09-30","type":"selection_or_access"}
{"id":"D5","route":"B3 Bilalic backward lead","study":"Tseng et al. 2014","url":"https://doi.org/10.1016/j.tsc.2014.04.004","decision":"include with reporting caution","reason":"Gaze trajectory and randomized attention manipulation; coarse aggregation.","inspection":"relevant methods/results PDF and pages 7,9,10","date":"2026-09-30","type":"selection_or_access"}
{"id":"D6","route":"B3 mismatch corrected with exact cited title in B4","study":"Cushen & Wiley 2012","url":"https://doi.org/10.1016/j.concog.2012.03.013","decision":"include provisionally","reason":"Individual versus aggregate trajectories and cue effects.","inspection":"primary abstract/publisher preview only","date":"2026-09-30","type":"selection_or_access"}
{"id":"D7","route":"B3 animal-task coverage","study":"Rosenberg et al. 2021","url":"https://doi.org/10.7554/eLife.66175","decision":"include","reason":"Mouse maze rates include abrupt and graded behavioural patterns; no neural recording.","inspection":"primary XML discontinuous-learning Results and rate-fit Methods","date":"2026-09-30","type":"selection_or_access"}
{"id":"D8","route":"B3 lead, B4 exact follow-up; direct Rosenberg reanalysis","study":"Reddy 2022","url":"https://doi.org/10.1073/pnas.2215352119","decision":"include split reanalysis/model","reason":"Competing sequential reinforcement mechanism; shared dataset, no recorded neural wave.","inspection":"primary XML/PNAS relevant Results/Experimental Tests/Methods","date":"2026-09-30","type":"selection_or_access"}
{"id":"D9","route":"B3 recent coverage, primary publisher reading","study":"Doulfoukar et al. 2026","url":"https://doi.org/10.3758/s13423-026-02983-8","decision":"theoretical boundary only","reason":"Published September 17; simulations cannot establish biological mechanism.","inspection":"abstract/task/model description only; full simulation audit unperformed","date":"2026-09-30","type":"selection_or_access"}
{"id":"D10","route":"backward reference from Doulfoukar primary bibliography","study":"Stuyck et al. 2024","url":"https://doi.org/10.1177/17470218231202519","decision":"nonspecific-state boundary","reason":"HRV is not direct prefrontal recording or solution-content accumulation.","inspection":"primary abstract only","date":"2026-09-30","type":"selection_or_access"}
{"id":"D11","route":"B1 recent latent-strategy search","study":"Qian et al. 2026","url":"https://doi.org/10.1038/s41467-026-69380-6","decision":"exclude core temporal claims","reason":"Working-memory strategy geometry rather than measured breakthrough trajectory.","inspection":"primary abstract/indexed article text screening only","date":"2026-09-30","type":"selection_or_access"}
{"id":"D12","route":"publisher related lead + B4 exact search","study":"Time-dependent deployment of mPFC representations 2026","url":"https://doi.org/10.1038/s41467-025-68215-0","decision":"exclude core","reason":"History-dependent foraging representations; no specified impasse-discovery transition.","inspection":"relevant primary abstract/discussion/method text screening","date":"2026-09-30","type":"selection_or_access"}
{"id":"D13","route":"recent neural lead + B4 exact search","study":"From pre-stimulus preparation to the Aha burst 2026","url":"https://doi.org/10.1016/j.cortex.2026.06.017","decision":"boundary; defer full/date audit","reason":"Condition decoding and preparatory states do not establish within-impasse solution accumulation; issue month not treated as online date.","inspection":"primary abstract/preview only","date":"2026-09-30","type":"selection_or_access"}
{"id":"D14","route":"publisher related lead; B5 resolve identifier","study":"Becker et al. 2025","url":"https://doi.org/10.1038/s41467-025-59355-4","decision":"exclude core trajectory claim","reason":"Pre/post solution representational change and later memory; does not resolve hidden within-impasse time course.","inspection":"primary abstract/relevant Discussion only; full temporal methods not audited","date":"2026-09-30","type":"selection_or_access"}
{"id":"D15","route":"retained v1 methodological inspection","study":"Graf et al. 2023","url":"https://doi.org/10.3390/jintelligence11050086","decision":"methodology only; simulated illustration excluded","reason":"Footnote distinguishes simulated abrupt example; empirical reanalysis shares Bilalic data.","inspection":"relevant full PDF footnote/methods","date":"2026-09-30","type":"selection_or_access"}
{"id":"D16","route":"v2 source-access retry","study":"Drieu et al. 2025","url":"https://doi.org/10.1038/s41586-025-08730-8","decision":"retain partial verification","reason":"XML failure and image-only text extraction do not upgrade reading depth.","inspection":"final PDF first two pages rendered/read in v1","date":"2026-09-30","type":"selection_or_access"}
{"id":"STOP","route":"coverage audit","decision":"bounded delivery, no saturation claim","reason":"Named routes completed; queries still yielded relevant work. Remaining access, index coverage and independent review limits disclosed.","date":"2026-09-30","type":"selection_or_access"}
```


---

## File: REVIEW_RESPONSE.md

# Response to Opus's v1 critique and v2 self-review

The user supplied an independent model review of **version 1**. Its assertions were leads, checked where consequential against primary sources. Version 2 received a separate skeptical **self-review by the same author**, not a new independent review. No paper/data replication was performed.

| Criticism | Disposition and concrete v2 action |
|---|---|
| Missing Powell, Knoblich and Townsend | **Accepted.** Relevant primary methods/results inspected and included with explicit temporal/generalization boundaries. |
| Powell undermines “animal evidence mostly abrupt” | **Qualified.** It changes coverage and strengthens neural-before-behaviour evidence. Precedence and abruptness coexist; the study does not establish a smooth ramp. The revised animal account reflects this distinction. |
| Search stopped too early, missing selection history | **Accepted.** Added registered plan, exact batch queries, citation routes, selection/access decisions and coverage/stop audit. Searches kept yielding relevant evidence; the new stop is explicitly bounded, not a saturation assertion. Missing v1 history is not invented. |
| Verification levels disappear in report | **Accepted.** Inspection depth now accompanies every study claim, including provisional abstract rows and partial Drieu reading. |
| Kounios incorrectly classed as progress precursor | **Accepted.** Separate preparatory-state category; related autonomic evidence also kept outside solution-content progress. |
| Bilalić residual group omitted | **Accepted.** Unclassifiable trajectories restored; borderline subjective-suddenness contrast also qualified. Appendix visually inspected. |
| Grokking cleanup timing misstated | **Accepted.** Report distinguishes circuit formation from the test-accuracy rise during cleanup. |
| Retrieval code mismatches historical manifest and duplicates reruns | **Accepted.** Declared resource list, deduplicated current cache, unchanged historical v1 manifest, append-only actual attempt history and content-addressed refresh files. Default cache rerun tested. Script does not claim to reconstruct old manual acquisition/search steps. |
| End with independent critic | **Partially fulfilled.** Earlier independent Opus review retained as v1 feedback; v2 self-review completed and labelled. A fresh independent critic pass remains outstanding. |

## Skeptical self-review performed before publication

Checks included: study/task/measure alignment; precedence versus gradualness; individual versus averaged trajectories; changepoint-induced alignment; null test versus equivalence; preparatory state versus progress; human versus model weights; behavioural reanalysis versus new independent data; awareness versus response timing; source access versus actual reading depth; internal reporting discrepancies; script repeatability; scope and sharing contents.

Corrections/constraints resulting from the pass:

- Kept Townsend as behavioural evidence and bounded its latent-state interpretation; did not treat inferred “Aha” timing as a neural or independently reported awareness onset.
- Kept Hasz's drift separate from solution progress and its lap-level timing separate from sub-lap precision.
- Split Löwe's human and artificial components; split Reddy's route reanalysis and RL dynamics. Preserved shared-data status.
- Retained Drieu, Ellis, Kounios, Durstewitz, Karlsson, Cushen and Stuyck at their actual limited inspection depth.
- Flagged Tseng's internal count/percentage inconsistencies; avoided precise sample/classifier claims based on them.
- Resolved the screened Becker memory-study identifier to a primary source before publication; its pre/post comparison is not used as a hidden-trajectory estimate.
- Removed the original unsupported low-information-gain conclusion. Named ongoing access, search-index and independent-review gaps.

The remaining evidence gap is substantive: no universal causal account of continuous solution-specific neural accumulation throughout genuine impasse. Improved reporting does not close that gap. A full independent v2 review and fuller access to the limited-inspection papers would improve confidence.


---

## File: CHANGELOG.md

# Dated changes

## Version 2 — 30 September 2026

Authorized research rerun and publication after Opus's v1 critique. Expanded primary-source/citation searches; added the three omissions and related studies/alternative mechanisms. The central conclusion remains mixed, with stronger animal evidence that neural change can precede behaviour while still being abrupt.

Added exact query batches, selection/access log, coverage/stopping audit, registered scope, visible claim-level inspection labels, critic-response table and honestly labelled self-review. Restored unclassifiable gaze trajectories and qualified borderline evidence. Separated preparatory/autonomic states, neural precursors, abrupt transitions, latent competence and artificial mechanisms. Corrected grokking phase order and marked reused datasets.

Repaired retrieval provenance and caching; added meaningful offline failure tests and a verified no-change cached rerun. Preserved v1 manifest/history and original public files. Added local-learning alternatives, model-recovery/equivalence checks and changepoint-alignment controls to the unrun experiment proposal.

No original-study replication, new biological experiment or independent v2 critic review is claimed. Some studies remain abstract/preview or partial-page only. This is a focused review, not systematic search saturation.

## Version 1 — 30 September 2026

Original publication at commit `a0dad4503c621923d42299cf8fdc377c3d13d03b`; original files archived in [versions/v1](versions/v1). Its coverage, stop claim, category labels, percentage reporting and retrieval script limitations are superseded by v2. Preserve it as historical evidence, not the current recommendation.


---

## File: WORKFLOW.md

# Recursive Discovery Lab

Workspace operating method adopted by the user from the five-page `Research lab prompt.pdf`.

Source: `[local user]/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Mir theory /Research prompt/Research lab prompt.pdf`

This is a working transcription and condensation of the adopted workflow, with dated operational improvements learned from completed investigations and review. It establishes how to investigate substantial research questions; it does not supply a research topic or initiate experiments by itself.

## Purpose

Construct useful representations, build instruments that can test them, create executable environments where possible, run discriminating experiments, compress findings into higher-order principles, and use those principles to open the next level of inquiry.

## Core loop

### 1. Represent

- Restate the question clearly.
- Identify variables, relationships, assumptions, unknowns, constraints, and competing hypotheses.
- Separate established facts, reasonable inference, speculation, and unknowns.
- Identify observations that would discriminate among the main hypotheses.

### 2. Build an instrument

- Ask what executable tool would reduce uncertainty better than further discussion.
- When useful, build the smallest viable simulation, data pipeline, search/retrieval tool, benchmark, evaluator, visualization, toy model, statistical test, or agent environment.
- Prefer simple instruments that can falsify assumptions before building elaborate ones.

### 3. Create a persistent world

- Store code, data, assumptions, experiment definitions, outputs, and summaries so subsequent iterations can build on earlier ones.
- Retain failed experiments.
- Maintain reproducibility where practical.

### 4. Explore with multiple perspectives

- Use investigative roles when useful: advocates for competing hypotheses, skeptical reviewer, experimental designer, statistician, mechanism finder, or adversarial falsifier.
- Roles provide diversity of reasoning; they are not fictional personalities.
- Do not let consensus substitute for evidence.

### 5. Run discriminating experiments

- Prefer experiments that distinguish competing explanations.
- Avoid experiments that can only confirm the favored hypothesis.
- Before each important experiment, record the expected result under each hypothesis, what outcome would weaken each hypothesis, and what uncertainty may remain.

### 6. Track the kill zone

For every major hypothesis, maintain:

- Strongest supporting evidence.
- Strongest opposing evidence.
- Required assumptions.
- Unresolved contradictions.
- Predictions.
- Explicit falsification or weakening conditions.

Every enlargement of a model should enlarge its kill zone: it should expose more ways for observations to challenge it.

### 7. Compress

After a meaningful batch of experiments:

- Identify recurring relationships and invariants.
- Distinguish robust findings from accidental correlations.
- Compress results into the smallest useful set of principles.

Compression is not truth. A compact explanation is valuable only if it survives testing.

### 8. Create the next level

- Treat a robust principle as a new object of reasoning.
- Ask whether it opens a more useful possibility space.
- Build the next instrument or representation around that higher-level abstraction.
- Repeat only when the next iteration is likely to produce new information.

## Corrigibility

Coherence must remain permeable to error. Do not optimize for making the initial idea look correct.

Actively seek counterexamples, rival hypotheses, edge cases, negative results, alternative causal explanations, measurement artifacts, selection effects, and confounders.

When evidence damages the preferred model, update the model rather than explaining the evidence away. Never silently rescue a failing hypothesis by adding assumptions. Record any new assumption explicitly.

## Information gain and stopping

Continue only while work produces meaningful information gain. Stop or change direction when:

- Repeated experiments produce the same information.
- New complexity does not improve prediction or explanation.
- Available tools or data cannot operationalize the question.
- Unavailable evidence dominates the uncertainty.
- A simpler model explains the observations equally well.

A productive loop is question -> experiment -> partial understanding -> better question.

A sterile loop is question -> more explanation -> same uncertainty -> more explanation.

## Lab notebook

Maintain `LAB_NOTEBOOK.md` throughout the work, not only at the end. Its sections are:

1. Current Question
2. Current Model
3. Competing Hypotheses
4. Assumptions
5. Experiments Run
6. Results
7. Failed Approaches
8. Surprises / Anomalies
9. Strongest Evidence For
10. Strongest Evidence Against
11. Kill Zones
12. Robust Findings
13. Speculative Interpretations
14. Newly Discovered Abstractions
15. Next Best Experiment
16. Confidence / Remaining Uncertainty

When a new investigation replaces the current one, preserve the previous notebook and its linked artifacts before resetting the active notebook.

## Literature search, verification and review

Added 2026-09-30 after external review of the hidden-progress investigation. Scale these checks to the question; a focused assessment must not imply systematic coverage.

### Search provenance and coverage

- Define inclusion/exclusion criteria and a coverage map before searching: populations/species, tasks, measures, timescales, competing mechanisms, supporting and opposing findings. Search for each materially different explanation rather than following only the first promising papers.
- Maintain a structured SEARCH_LOG alongside the notebook. For each batch record the date, exact queries, search engine/database and filters, candidate identifiers/URLs, discovery route, inclusion/exclusion/defer reasons and access failures. Raw search results and download manifests supplement this log; they do not replace it. Mark retrospective reconstruction as retrospective, and unknown queries as unknown.
- Follow backward references and forward citations from the central anchor papers. Record which anchors were checked, the service and date, relevant candidates and decisions, and any unavailable citation index. Include a targeted recent-literature search through a stated cutoff date. Citation proximity alone does not establish relevance or independence.
- Before stopping, record the yield of the final search and citation-chasing batches: new relevant candidates, new measures/mechanisms or contradictions, and changes to the synthesis. Review unfilled coverage areas and unresolved directly relevant leads. Repeatedly finding familiar papers is not sufficient evidence of saturation.
- If stopping because of access, time or diminishing returns, state that reason and the remaining gaps. Do not substitute an unsupported claim of low information gain. Discovery of a material omission reopens the affected part of the search rather than requiring every source to be collected.

### Claim-level verification

- Carry verification into the final report at the point of the claim, including evidence-table rows: relevant full-text methods/results inspected; named pages/figures inspected; abstract/preview only; or secondary/unverified lead. Downloading or extracting a file does not establish that its contents were read. Full-text access does not mean the entire study or supplements were audited.
- Keep verification depth separate from evidential strength. Record task, participants/animals, measured variable, temporal resolution, analysis, what the result supports, alternative explanations and generalization limits. Avoid conclusions that require unavailable methods or results.
- Maintain an evidence ontology that follows the question. Preparatory state, solution-related precursor, gradual accumulation, abrupt transition, latent knowledge and analogy can differ and coexist. Temporal precedence does not establish gradualness, causality or correct solution content.
- Inspect figure captions, footnotes and methods for simulated versus empirical data, averaging, filtering, alignment and exclusions. Report denominators and residual/unclassifiable groups when giving category percentages. Avoid treating linked analyses of one dataset as independent replication.
- Audit descriptions of multi-stage mechanisms for temporal order; internal mechanism formation and visible performance change need not occur in the same stage.

### Reproducibility and handoff

- Use a declared source list and stable source identifiers. Reconcile it with the retrieval manifest; explain historical attempts, alternate URLs, excluded leads and script changes rather than claiming the current script reproduces every past action.
- Repeated default retrieval must not silently append duplicate stable records. Reuse validated cached files; keep explicit refresh/retry attempts in a separate dated history and update a deduplicated current view. Preserve failures and changed hashes. Verify this behaviour before calling an instrument repeatable.
- Share the search/selection log, evidence ledger, verification limits, notebook, exclusions and experiment status with the final report. Check that the handoff actually includes them. Preserve the original version and provide a dated change log for revisions; distinguish local edits from published revisions.

### Critic pass and response

- For substantial syntheses, seek an independent critic when available and authorized. Give the critic the question, scope, full draft, search/selection log and access ledger. Ask specifically for missing counterevidence, unjustified stopping, incorrect timing/measurement interpretation, confidence inflation and reproducibility failures.
- If independent review is unavailable, perform a separate skeptical self-check and label it as self-review. Do not call a second pass by the same author independent or claim an unperformed review.
- Treat a critic's report as leads, not proof. Check important criticisms against primary sources and local artifacts; keep a response table with accepted, qualified, rejected or unresolved findings, evidence and concrete actions. Fix material problems, recheck changed claims and record remaining limitations before presenting a revision as reviewed.

## Output style

Prefer experiments over speculation, mechanisms over labels, discriminating evidence over volume of evidence, small executable models over elaborate verbal theories, and uncertainty over false precision.

Explain useful results at two levels:

1. Plain-language interpretation.
2. Technical evidence and limitations.

## Guiding principles

- Intelligence is the ability to build and revise useful models of relationships, then use them to predict, choose, and act toward goals.
- Metaphor generates the hypothesis. Structural correspondence makes it interesting. Prediction tells us whether we found more than a metaphor.
- Build the widest coherent model possible without making it harder for the world to prove it wrong.
- A productive theory produces experiments that can hurt it.
- Commit to the research program more strongly than to its current explanation.
- Recursion should turn a possibility space into a tested principle that supports a better possibility space, rather than endless thought.


---

## File: fetch_sources.py

```python
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
```


---

## File: test_fetch_sources.py

```python
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
```


---

## File: SOURCE_LIST.json

```json
[
  {
    "id": "schuck2015",
    "url": "https://schucklab.gitlab.io/docs/papers/Schuck_etal_2015_Neuron.pdf"
  },
  {
    "id": "rose2010",
    "url": "https://www.kognition.uni-koeln.de/literature/Rose_Haider_Buechel_2010.pdf"
  },
  {
    "id": "metcalfe1987",
    "url": "https://www.columbia.edu/cu/psychology/metcalfe/PDFs/Metcalfe%20Wiebe%201987.pdf"
  },
  {
    "id": "kuchibhotla2019",
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6517418/fullTextXML"
  },
  {
    "id": "jungbeeman2004",
    "url": "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0020097&type=printable"
  },
  {
    "id": "nanda2023",
    "url": "https://arxiv.org/pdf/2301.05217"
  },
  {
    "id": "drieu2025",
    "url": "https://cdn.prod.website-files.com/690a83fda53579ba8497635f/69bbf890f8d2b187f99e3620_2025_Nature_Drieu.pdf"
  },
  {
    "id": "graf2023",
    "url": "https://eprints.whiterose.ac.uk/199182/1/jintelligence-11-00086-v2.pdf"
  },
  {
    "id": "bowden1998",
    "url": "https://cpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/a/699/files/2015/11/Getting-the-right-idea-Semantic-activation-in-the-right-hemisphere-may-help-solve-insight-problems-154um4l.pdf"
  },
  {
    "id": "siniscalchi2016",
    "url": "https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf"
  },
  {
    "id": "bilalic2021",
    "url": "https://neuroscienceofexpertise.com/Publications/papers/Bilalic_2021_Insight.pdf"
  },
  {
    "id": "powell2016",
    "url": "https://www.nature.com/articles/ncomms12830"
  },
  {
    "id": "knoblich2001",
    "url": "https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving"
  },
  {
    "id": "townsend2026",
    "url": "https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf"
  },
  {
    "id": "hasz2020",
    "url": "https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf"
  },
  {
    "id": "lowe2024",
    "url": "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1012505&type=printable"
  },
  {
    "id": "rosenberg2021",
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8294850/fullTextXML"
  },
  {
    "id": "reddy2022",
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9894243/fullTextXML"
  },
  {
    "id": "drieu2025xml",
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML"
  },
  {
    "id": "tseng2014",
    "url": "https://www.epc.ntnu.edu.tw/Download.aspx?dir=Archive&file=B9-EE-32-17-F9-BB-EC-CA-4B-E1-17-79-7E-19-EE-49.pdf&filename=%E7%9C%BC%E5%8B%95%E7%A0%94%E7%A9%B66-20140301&sn=137"
  }
]
```


---

## File: source_manifest.json

```json
{
  "bilalic2021": {
    "bytes": 2360903,
    "extraction": "pypdf",
    "final_url": "https://neuroscienceofexpertise.com/Publications/papers/Bilalic_2021_Insight.pdf",
    "id": "bilalic2021",
    "name": "bilalic2021",
    "pages": 37,
    "path": "sources/bilalic2021.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://neuroscienceofexpertise.com/Publications/papers/Bilalic_2021_Insight.pdf",
    "retrieved_utc": "2026-09-30T22:16:31.952969+00:00",
    "sha256": "f6235acd7777a5633e6b058855b47d58d96d71c07f8f48a58c8df7cad9e34756",
    "status": "saved"
  },
  "bowden1998": {
    "bytes": 69806,
    "extraction": "pypdf",
    "final_url": "https://cpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/a/699/files/2015/11/Getting-the-right-idea-Semantic-activation-in-the-right-hemisphere-may-help-solve-insight-problems-154um4l.pdf",
    "id": "bowden1998",
    "name": "bowden1998",
    "pages": 6,
    "path": "sources/bowden1998.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://cpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/a/699/files/2015/11/Getting-the-right-idea-Semantic-activation-in-the-right-hemisphere-may-help-solve-insight-problems-154um4l.pdf",
    "retrieved_utc": "2026-09-30T22:13:14.712900+00:00",
    "sha256": "cae2f436cb756db92f93753077d02a840678a69d05b98eab2c6884f382ce97ee",
    "status": "saved"
  },
  "drieu2025": {
    "bytes": 10465863,
    "extraction": "pypdf",
    "final_url": "https://cdn.prod.website-files.com/690a83fda53579ba8497635f/69bbf890f8d2b187f99e3620_2025_Nature_Drieu.pdf",
    "id": "drieu2025",
    "inspection_note": "Image-only final article; title, abstract and Fig 1 inspected from rendered pages.",
    "name": "drieu2025",
    "pages": 36,
    "path": "sources/drieu2025.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://cdn.prod.website-files.com/690a83fda53579ba8497635f/69bbf890f8d2b187f99e3620_2025_Nature_Drieu.pdf",
    "retrieved_utc": "2026-09-30T22:13:10.557117+00:00",
    "sha256": "8c4586306785a777965532a0bf41b2705f7e48582092f764ed09b69db17d021e",
    "status": "saved",
    "substantive_text_extracted": false,
    "visual_inspection_pages": [
      1,
      2
    ]
  },
  "drieu2025xml": {
    "error": "500 Server Error:  for url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML",
    "id": "drieu2025xml",
    "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML",
    "retrieved_utc": "2026-09-30T23:01:37.556661+00:00",
    "status": "failed"
  },
  "graf2023": {
    "bytes": 3081190,
    "extraction": "pypdf",
    "final_url": "https://eprints.whiterose.ac.uk/id/eprint/199182/1/jintelligence-11-00086-v2.pdf",
    "id": "graf2023",
    "name": "graf2023",
    "pages": 18,
    "path": "sources/graf2023.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://eprints.whiterose.ac.uk/199182/1/jintelligence-11-00086-v2.pdf",
    "retrieved_utc": "2026-09-30T22:13:10.999725+00:00",
    "sha256": "e63bf218a1375c2e1833904cbd818cacf503740563ae400fedfab871d34a8c47",
    "status": "saved"
  },
  "hasz2020": {
    "error": "403 Client Error: Forbidden for url: https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf",
    "id": "hasz2020",
    "requested_url": "https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf",
    "retrieved_utc": "2026-09-30T23:01:32.902735+00:00",
    "status": "failed"
  },
  "jungbeeman2004": {
    "bytes": 356826,
    "content_type": "application/pdf",
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "final_url": "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0020097&type=printable",
    "id": "jungbeeman2004",
    "name": "jungbeeman2004",
    "pages": 11,
    "path": "sources/jungbeeman2004.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0020097&type=printable",
    "retrieved_utc": "2026-09-30T22:11:45.127280+00:00",
    "sha256": "5ab0cd5e0d7fcdf6ed3c8ca3e2431704f272ba76757979dc0072a90991f9a491",
    "status": "saved"
  },
  "knoblich2001": {
    "error": "403 Client Error: Forbidden for url: https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving",
    "id": "knoblich2001",
    "requested_url": "https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving",
    "retrieved_utc": "2026-09-30T23:00:56.499812+00:00",
    "status": "failed"
  },
  "kuchibhotla2019": {
    "bytes": 174035,
    "content_type": "application/xml",
    "extraction": "tag-stripped text; raw XML retained",
    "final_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6517418/fullTextXML",
    "id": "kuchibhotla2019",
    "name": "kuchibhotla2019",
    "path": "sources/kuchibhotla2019.xml",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6517418/fullTextXML",
    "retrieved_utc": "2026-09-30T22:11:43.822552+00:00",
    "sha256": "c9b37676e6c1a0a21b80e0bc333389d9262bebcb454e7c8200f024c6f0161d3c",
    "status": "saved"
  },
  "lowe2024": {
    "bytes": 2105912,
    "content_type": "application/pdf",
    "extraction": "pypdf; reading order may vary",
    "final_url": "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1012505&type=printable",
    "id": "lowe2024",
    "pages": 29,
    "path": "sources/lowe2024-dbed452b2013.pdf",
    "requested_url": "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1012505&type=printable",
    "retrieved_utc": "2026-09-30T23:01:33.099329+00:00",
    "sha256": "dbed452b201388e600db44c94d46e338bb61665562a61b11291c5d88dbd76460",
    "status": "saved",
    "substantive_text_extracted": true
  },
  "metcalfe1987": {
    "bytes": 810549,
    "content_type": "application/pdf",
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "final_url": "https://www.columbia.edu/cu/psychology/metcalfe/PDFs/Metcalfe%20Wiebe%201987.pdf",
    "id": "metcalfe1987",
    "name": "metcalfe1987",
    "pages": 9,
    "path": "sources/metcalfe1987.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://www.columbia.edu/cu/psychology/metcalfe/PDFs/Metcalfe%20Wiebe%201987.pdf",
    "retrieved_utc": "2026-09-30T22:11:41.473159+00:00",
    "sha256": "7794d738e5f76c518b824c86753ed967e9903439356da9e79366018f15073cd3",
    "status": "saved"
  },
  "nanda2023": {
    "bytes": 3057847,
    "content_type": "application/pdf",
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "final_url": "https://arxiv.org/pdf/2301.05217",
    "id": "nanda2023",
    "name": "nanda2023",
    "pages": 35,
    "path": "sources/nanda2023.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://arxiv.org/pdf/2301.05217",
    "retrieved_utc": "2026-09-30T22:11:46.003020+00:00",
    "sha256": "93dcdafc2ecf75d31ab2e32e74cdc11e2e488fec42edfef58ad3d4b6515bcd5f",
    "status": "saved"
  },
  "powell2016": {
    "bytes": 469736,
    "content_type": "text/html; charset=utf-8",
    "extraction": "tag-stripped navigation aid; verify article content separately",
    "final_url": "https://www.nature.com/articles/ncomms12830",
    "id": "powell2016",
    "path": "sources/powell2016-17b46db599f8.html",
    "requested_url": "https://www.nature.com/articles/ncomms12830",
    "retrieved_utc": "2026-09-30T23:00:54.746265+00:00",
    "sha256": "17b46db599f857219271de969df2db05001c118859cb6c9a411a1d31bfeb1683",
    "status": "saved"
  },
  "reddy2022": {
    "bytes": 115217,
    "content_type": "application/xml",
    "extraction": "tag-stripped navigation aid; verify article content separately",
    "final_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9894243/fullTextXML",
    "id": "reddy2022",
    "path": "sources/reddy2022-acd36416f22b.xml",
    "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9894243/fullTextXML",
    "retrieved_utc": "2026-09-30T23:01:36.237852+00:00",
    "sha256": "acd36416f22bac94c61b41d44dbdffa5e4cd314ab7fdef6b4428b088206a5657",
    "status": "saved"
  },
  "rose2010": {
    "bytes": 864221,
    "content_type": "application/pdf",
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "final_url": "https://www.kognition.uni-koeln.de/literature/Rose_Haider_Buechel_2010.pdf",
    "id": "rose2010",
    "name": "rose2010",
    "pages": 11,
    "path": "sources/rose2010.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://www.kognition.uni-koeln.de/literature/Rose_Haider_Buechel_2010.pdf",
    "retrieved_utc": "2026-09-30T22:11:35.686572+00:00",
    "sha256": "deb2fc4a44803b267fdd892880590a8513b7e659f3ac5286d59880a46a6514f1",
    "status": "saved",
    "visual_inspection_pages": [
      6
    ]
  },
  "rosenberg2021": {
    "bytes": 265386,
    "content_type": "application/xml",
    "extraction": "tag-stripped navigation aid; verify article content separately",
    "final_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8294850/fullTextXML",
    "id": "rosenberg2021",
    "path": "sources/rosenberg2021-0311732fee9e.xml",
    "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8294850/fullTextXML",
    "retrieved_utc": "2026-09-30T23:01:34.414054+00:00",
    "sha256": "0311732fee9e19f37ae2698a45ec157a9baeebcabeba3e1e203b03c7f6dbb822",
    "status": "saved"
  },
  "schuck2015": {
    "bytes": 1606959,
    "content_type": "application/pdf",
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "final_url": "https://schucklab.gitlab.io/docs/papers/Schuck_etal_2015_Neuron.pdf",
    "id": "schuck2015",
    "name": "schuck2015",
    "pages": 11,
    "path": "sources/schuck2015.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://schucklab.gitlab.io/docs/papers/Schuck_etal_2015_Neuron.pdf",
    "retrieved_utc": "2026-09-30T22:11:33.980363+00:00",
    "sha256": "7173a24268f6682147f4805a218ce24a4d0ccbd7df41969b9e1f9751e9b8f74f",
    "status": "saved",
    "visual_inspection_pages": [
      4,
      5
    ]
  },
  "siniscalchi2016": {
    "bytes": 1954732,
    "extraction": "pypdf",
    "final_url": "https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf",
    "id": "siniscalchi2016",
    "name": "siniscalchi2016",
    "pages": 12,
    "path": "sources/siniscalchi2016.pdf",
    "provenance": "Imported unchanged from v1; reading level is in EVIDENCE_LEDGER.md.",
    "requested_url": "https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf",
    "retrieved_utc": "2026-09-30T22:13:45.659589+00:00",
    "sha256": "950f2c35fbd3665077b3217bc619118ca8fe7617056fbdd792d772c453d74236",
    "status": "saved"
  },
  "townsend2026": {
    "bytes": 5517491,
    "content_type": "application/pdf",
    "extraction": "pypdf",
    "final_url": "https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf",
    "id": "townsend2026",
    "pages": 19,
    "path": "sources/townsend2026-67a5f5b6c3d3.pdf",
    "requested_url": "https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf",
    "retrieval_method": "normal requests with browser user agent; retry of timeout or blocked script request",
    "retrieved_utc": "2026-09-30T23:03:33.264106+00:00",
    "sha256": "67a5f5b6c3d3584aad3467740dff3ac280142c910798984affa09013516d04a5",
    "status": "saved"
  },
  "tseng2014": {
    "bytes": 1122588,
    "content_type": "application/pdf",
    "extraction": "pypdf; reading order may vary",
    "final_url": "https://www.epc.ntnu.edu.tw/Download.aspx?dir=Archive&file=B9-EE-32-17-F9-BB-EC-CA-4B-E1-17-79-7E-19-EE-49.pdf&filename=%E7%9C%BC%E5%8B%95%E7%A0%94%E7%A9%B66-20140301&sn=137",
    "id": "tseng2014",
    "pages": 12,
    "path": "sources/tseng2014-41278c4db9cb.pdf",
    "requested_url": "https://www.epc.ntnu.edu.tw/Download.aspx?dir=Archive&file=B9-EE-32-17-F9-BB-EC-CA-4B-E1-17-79-7E-19-EE-49.pdf&filename=%E7%9C%BC%E5%8B%95%E7%A0%94%E7%A9%B66-20140301&sn=137",
    "retrieved_utc": "2026-09-30T23:01:44.720426+00:00",
    "sha256": "41278c4db9cb194610e5e6250206ceb23fbe25fbcc9eae947700519f74732702",
    "status": "saved",
    "substantive_text_extracted": true
  }
}
```


---

## File: SOURCE_HISTORY_V1.json

```json
[
  {
    "name": "schuck2015",
    "requested_url": "https://schucklab.gitlab.io/docs/papers/Schuck_etal_2015_Neuron.pdf",
    "retrieved_utc": "2026-09-30T22:11:33.980363+00:00",
    "final_url": "https://schucklab.gitlab.io/docs/papers/Schuck_etal_2015_Neuron.pdf",
    "content_type": "application/pdf",
    "sha256": "7173a24268f6682147f4805a218ce24a4d0ccbd7df41969b9e1f9751e9b8f74f",
    "bytes": 1606959,
    "pages": 11,
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "status": "saved",
    "path": "sources/schuck2015.pdf",
    "visual_inspection_pages": [
      4,
      5
    ]
  },
  {
    "name": "rose2010",
    "requested_url": "https://www.kognition.uni-koeln.de/literature/Rose_Haider_Buechel_2010.pdf",
    "retrieved_utc": "2026-09-30T22:11:35.686572+00:00",
    "final_url": "https://www.kognition.uni-koeln.de/literature/Rose_Haider_Buechel_2010.pdf",
    "content_type": "application/pdf",
    "sha256": "deb2fc4a44803b267fdd892880590a8513b7e659f3ac5286d59880a46a6514f1",
    "bytes": 864221,
    "pages": 11,
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "status": "saved",
    "path": "sources/rose2010.pdf",
    "visual_inspection_pages": [
      6
    ]
  },
  {
    "name": "siniscalchi2016",
    "requested_url": "https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf",
    "retrieved_utc": "2026-09-30T22:11:41.088157+00:00",
    "status": "failed",
    "error": "406 Client Error: Not Acceptable for url: https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf"
  },
  {
    "name": "metcalfe1987",
    "requested_url": "https://www.columbia.edu/cu/psychology/metcalfe/PDFs/Metcalfe%20Wiebe%201987.pdf",
    "retrieved_utc": "2026-09-30T22:11:41.473159+00:00",
    "final_url": "https://www.columbia.edu/cu/psychology/metcalfe/PDFs/Metcalfe%20Wiebe%201987.pdf",
    "content_type": "application/pdf",
    "sha256": "7794d738e5f76c518b824c86753ed967e9903439356da9e79366018f15073cd3",
    "bytes": 810549,
    "pages": 9,
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "status": "saved",
    "path": "sources/metcalfe1987.pdf"
  },
  {
    "name": "drieu2025",
    "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML",
    "retrieved_utc": "2026-09-30T22:11:42.862985+00:00",
    "status": "failed",
    "error": "500 Server Error:  for url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML"
  },
  {
    "name": "kuchibhotla2019",
    "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6517418/fullTextXML",
    "retrieved_utc": "2026-09-30T22:11:43.822552+00:00",
    "final_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6517418/fullTextXML",
    "content_type": "application/xml",
    "sha256": "c9b37676e6c1a0a21b80e0bc333389d9262bebcb454e7c8200f024c6f0161d3c",
    "bytes": 174035,
    "extraction": "tag-stripped text; raw XML retained",
    "status": "saved",
    "path": "sources/kuchibhotla2019.xml"
  },
  {
    "name": "jungbeeman2004",
    "requested_url": "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0020097&type=printable",
    "retrieved_utc": "2026-09-30T22:11:45.127280+00:00",
    "final_url": "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0020097&type=printable",
    "content_type": "application/pdf",
    "sha256": "5ab0cd5e0d7fcdf6ed3c8ca3e2431704f272ba76757979dc0072a90991f9a491",
    "bytes": 356826,
    "pages": 11,
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "status": "saved",
    "path": "sources/jungbeeman2004.pdf"
  },
  {
    "name": "nanda2023",
    "requested_url": "https://arxiv.org/pdf/2301.05217",
    "retrieved_utc": "2026-09-30T22:11:46.003020+00:00",
    "final_url": "https://arxiv.org/pdf/2301.05217",
    "content_type": "application/pdf",
    "sha256": "93dcdafc2ecf75d31ab2e32e74cdc11e2e488fec42edfef58ad3d4b6515bcd5f",
    "bytes": 3057847,
    "pages": 35,
    "extraction": "pypdf; page reading order may vary; selected figures inspected separately",
    "status": "saved",
    "path": "sources/nanda2023.pdf"
  },
  {
    "name": "drieu2025",
    "requested_url": "https://cdn.prod.website-files.com/690a83fda53579ba8497635f/69bbf890f8d2b187f99e3620_2025_Nature_Drieu.pdf",
    "retrieved_utc": "2026-09-30T22:13:10.557117+00:00",
    "status": "saved",
    "bytes": 10465863,
    "pages": 36,
    "sha256": "8c4586306785a777965532a0bf41b2705f7e48582092f764ed09b69db17d021e",
    "final_url": "https://cdn.prod.website-files.com/690a83fda53579ba8497635f/69bbf890f8d2b187f99e3620_2025_Nature_Drieu.pdf",
    "path": "sources/drieu2025.pdf",
    "extraction": "pypdf",
    "substantive_text_extracted": false,
    "visual_inspection_pages": [
      1,
      2
    ],
    "inspection_note": "Image-only final article; title, abstract and Fig 1 inspected from rendered pages."
  },
  {
    "name": "graf2023",
    "requested_url": "https://eprints.whiterose.ac.uk/199182/1/jintelligence-11-00086-v2.pdf",
    "retrieved_utc": "2026-09-30T22:13:10.999725+00:00",
    "status": "saved",
    "bytes": 3081190,
    "pages": 18,
    "sha256": "e63bf218a1375c2e1833904cbd818cacf503740563ae400fedfab871d34a8c47",
    "final_url": "https://eprints.whiterose.ac.uk/id/eprint/199182/1/jintelligence-11-00086-v2.pdf",
    "path": "sources/graf2023.pdf",
    "extraction": "pypdf"
  },
  {
    "name": "bowden1998",
    "requested_url": "https://cpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/a/699/files/2015/11/Getting-the-right-idea-Semantic-activation-in-the-right-hemisphere-may-help-solve-insight-problems-154um4l.pdf",
    "retrieved_utc": "2026-09-30T22:13:14.712900+00:00",
    "status": "saved",
    "bytes": 69806,
    "pages": 6,
    "sha256": "cae2f436cb756db92f93753077d02a840678a69d05b98eab2c6884f382ce97ee",
    "final_url": "https://cpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/a/699/files/2015/11/Getting-the-right-idea-Semantic-activation-in-the-right-hemisphere-may-help-solve-insight-problems-154um4l.pdf",
    "path": "sources/bowden1998.pdf",
    "extraction": "pypdf"
  },
  {
    "name": "gallistel2004",
    "requested_url": "https://nemenmanlab.org/~ilya/images/5/5e/Gallistel-etal-04.pdf",
    "retrieved_utc": "2026-09-30T22:13:15.602804+00:00",
    "status": "failed",
    "error": "HTTPSConnectionPool(host='nemenmanlab.org', port=443): Max retries exceeded with url: /~ilya/images/5/5e/Gallistel-etal-04.pdf (Caused by ConnectTimeoutError(<HTTPSConnection(host='nemenmanlab.org', port=443) at 0x106219ca0>, 'Connection to nemenmanlab.org timed out. (connect timeout=30)'))"
  },
  {
    "name": "siniscalchi2016",
    "requested_url": "https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf",
    "retrieved_utc": "2026-09-30T22:13:45.659589+00:00",
    "status": "saved",
    "bytes": 1954732,
    "pages": 12,
    "sha256": "950f2c35fbd3665077b3217bc619118ca8fe7617056fbdd792d772c453d74236",
    "final_url": "https://alexkwanlab.org/wp-content/uploads/2019/02/siniscalchiNatNeurosci2016.pdf",
    "path": "sources/siniscalchi2016.pdf",
    "extraction": "pypdf"
  },
  {
    "name": "bilalic2021",
    "requested_url": "https://neuroscienceofexpertise.com/Publications/papers/Bilalic_2021_Insight.pdf",
    "final_url": "https://neuroscienceofexpertise.com/Publications/papers/Bilalic_2021_Insight.pdf",
    "retrieved_utc": "2026-09-30T22:16:31.952969+00:00",
    "status": "saved",
    "pages": 37,
    "bytes": 2360903,
    "sha256": "f6235acd7777a5633e6b058855b47d58d96d71c07f8f48a58c8df7cad9e34756",
    "extraction": "pypdf",
    "path": "sources/bilalic2021.pdf"
  }
]
```


---

## File: retrieval_attempts.jsonl

```json
{"error": "HTTPSConnectionPool(host='www.nature.com', port=443): Max retries exceeded with url: /articles/ncomms12830 (Caused by NameResolutionError(\"HTTPSConnection(host='www.nature.com', port=443): Failed to resolve 'www.nature.com' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "powell2016", "requested_url": "https://www.nature.com/articles/ncomms12830", "retrieved_utc": "2026-09-30T23:00:36.870642+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='www.researchgate.net', port=443): Max retries exceeded with url: /publication/11538874_An_eye_movement_study_of_insight_problem_solving (Caused by NameResolutionError(\"HTTPSConnection(host='www.researchgate.net', port=443): Failed to resolve 'www.researchgate.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "knoblich2001", "requested_url": "https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving", "retrieved_utc": "2026-09-30T23:00:36.881061+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='eprints.whiterose.ac.uk', port=443): Max retries exceeded with url: /id/eprint/240892/1/PIIS0960982226004562.pdf (Caused by NameResolutionError(\"HTTPSConnection(host='eprints.whiterose.ac.uk', port=443): Failed to resolve 'eprints.whiterose.ac.uk' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "townsend2026", "requested_url": "https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf", "retrieved_utc": "2026-09-30T23:00:36.881842+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='redishlab.umn.edu', port=443): Max retries exceeded with url: /sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf (Caused by NameResolutionError(\"HTTPSConnection(host='redishlab.umn.edu', port=443): Failed to resolve 'redishlab.umn.edu' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "hasz2020", "requested_url": "https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf", "retrieved_utc": "2026-09-30T23:00:36.882447+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='journals.plos.org', port=443): Max retries exceeded with url: /ploscompbiol/article/file?id=10.1371/journal.pcbi.1012505&type=printable (Caused by NameResolutionError(\"HTTPSConnection(host='journals.plos.org', port=443): Failed to resolve 'journals.plos.org' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "lowe2024", "requested_url": "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1012505&type=printable", "retrieved_utc": "2026-09-30T23:00:36.883052+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='www.ebi.ac.uk', port=443): Max retries exceeded with url: /europepmc/webservices/rest/PMC8294850/fullTextXML (Caused by NameResolutionError(\"HTTPSConnection(host='www.ebi.ac.uk', port=443): Failed to resolve 'www.ebi.ac.uk' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "rosenberg2021", "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8294850/fullTextXML", "retrieved_utc": "2026-09-30T23:00:36.883749+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='www.ebi.ac.uk', port=443): Max retries exceeded with url: /europepmc/webservices/rest/PMC9894243/fullTextXML (Caused by NameResolutionError(\"HTTPSConnection(host='www.ebi.ac.uk', port=443): Failed to resolve 'www.ebi.ac.uk' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "reddy2022", "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9894243/fullTextXML", "retrieved_utc": "2026-09-30T23:00:36.884274+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='www.ebi.ac.uk', port=443): Max retries exceeded with url: /europepmc/webservices/rest/PMC13034642/fullTextXML (Caused by NameResolutionError(\"HTTPSConnection(host='www.ebi.ac.uk', port=443): Failed to resolve 'www.ebi.ac.uk' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "drieu2025xml", "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML", "retrieved_utc": "2026-09-30T23:00:36.884786+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='www.epc.ntnu.edu.tw', port=443): Max retries exceeded with url: /Download.aspx?dir=Archive&file=B9-EE-32-17-F9-BB-EC-CA-4B-E1-17-79-7E-19-EE-49.pdf&filename=%E7%9C%BC%E5%8B%95%E7%A0%94%E7%A9%B66-20140301&sn=137 (Caused by NameResolutionError(\"HTTPSConnection(host='www.epc.ntnu.edu.tw', port=443): Failed to resolve 'www.epc.ntnu.edu.tw' ([Errno 8] nodename nor servname provided, or not known)\"))", "id": "tseng2014", "requested_url": "https://www.epc.ntnu.edu.tw/Download.aspx?dir=Archive&file=B9-EE-32-17-F9-BB-EC-CA-4B-E1-17-79-7E-19-EE-49.pdf&filename=%E7%9C%BC%E5%8B%95%E7%A0%94%E7%A9%B66-20140301&sn=137", "retrieved_utc": "2026-09-30T23:00:36.885313+00:00", "status": "failed"}
{"bytes": 469736, "content_type": "text/html; charset=utf-8", "extraction": "tag-stripped navigation aid; verify article content separately", "final_url": "https://www.nature.com/articles/ncomms12830", "id": "powell2016", "path": "sources/powell2016-17b46db599f8.html", "requested_url": "https://www.nature.com/articles/ncomms12830", "retrieved_utc": "2026-09-30T23:00:54.746265+00:00", "sha256": "17b46db599f857219271de969df2db05001c118859cb6c9a411a1d31bfeb1683", "status": "saved"}
{"error": "403 Client Error: Forbidden for url: https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving", "id": "knoblich2001", "requested_url": "https://www.researchgate.net/publication/11538874_An_eye_movement_study_of_insight_problem_solving", "retrieved_utc": "2026-09-30T23:00:56.499812+00:00", "status": "failed"}
{"error": "HTTPSConnectionPool(host='eprints.whiterose.ac.uk', port=443): Read timed out. (read timeout=35)", "id": "townsend2026", "requested_url": "https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf", "retrieved_utc": "2026-09-30T23:00:56.632191+00:00", "status": "failed"}
{"error": "403 Client Error: Forbidden for url: https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf", "id": "hasz2020", "requested_url": "https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf", "retrieved_utc": "2026-09-30T23:01:32.902735+00:00", "status": "failed"}
{"bytes": 2105912, "content_type": "application/pdf", "extraction": "pypdf; reading order may vary", "final_url": "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1012505&type=printable", "id": "lowe2024", "pages": 29, "path": "sources/lowe2024-dbed452b2013.pdf", "requested_url": "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1012505&type=printable", "retrieved_utc": "2026-09-30T23:01:33.099329+00:00", "sha256": "dbed452b201388e600db44c94d46e338bb61665562a61b11291c5d88dbd76460", "status": "saved", "substantive_text_extracted": true}
{"bytes": 265386, "content_type": "application/xml", "extraction": "tag-stripped navigation aid; verify article content separately", "final_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8294850/fullTextXML", "id": "rosenberg2021", "path": "sources/rosenberg2021-0311732fee9e.xml", "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8294850/fullTextXML", "retrieved_utc": "2026-09-30T23:01:34.414054+00:00", "sha256": "0311732fee9e19f37ae2698a45ec157a9baeebcabeba3e1e203b03c7f6dbb822", "status": "saved"}
{"bytes": 115217, "content_type": "application/xml", "extraction": "tag-stripped navigation aid; verify article content separately", "final_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9894243/fullTextXML", "id": "reddy2022", "path": "sources/reddy2022-acd36416f22b.xml", "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9894243/fullTextXML", "retrieved_utc": "2026-09-30T23:01:36.237852+00:00", "sha256": "acd36416f22bac94c61b41d44dbdffa5e4cd314ab7fdef6b4428b088206a5657", "status": "saved"}
{"error": "500 Server Error:  for url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML", "id": "drieu2025xml", "requested_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13034642/fullTextXML", "retrieved_utc": "2026-09-30T23:01:37.556661+00:00", "status": "failed"}
{"bytes": 1122588, "content_type": "application/pdf", "extraction": "pypdf; reading order may vary", "final_url": "https://www.epc.ntnu.edu.tw/Download.aspx?dir=Archive&file=B9-EE-32-17-F9-BB-EC-CA-4B-E1-17-79-7E-19-EE-49.pdf&filename=%E7%9C%BC%E5%8B%95%E7%A0%94%E7%A9%B66-20140301&sn=137", "id": "tseng2014", "pages": 12, "path": "sources/tseng2014-41278c4db9cb.pdf", "requested_url": "https://www.epc.ntnu.edu.tw/Download.aspx?dir=Archive&file=B9-EE-32-17-F9-BB-EC-CA-4B-E1-17-79-7E-19-EE-49.pdf&filename=%E7%9C%BC%E5%8B%95%E7%A0%94%E7%A9%B66-20140301&sn=137", "retrieved_utc": "2026-09-30T23:01:44.720426+00:00", "sha256": "41278c4db9cb194610e5e6250206ceb23fbe25fbcc9eae947700519f74732702", "status": "saved", "substantive_text_extracted": true}
{"bytes": 5517491, "content_type": "application/pdf", "extraction": "pypdf", "final_url": "https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf", "id": "townsend2026", "pages": 19, "path": "sources/townsend2026-67a5f5b6c3d3.pdf", "requested_url": "https://eprints.whiterose.ac.uk/id/eprint/240892/1/PIIS0960982226004562.pdf", "retrieval_method": "normal requests with browser user agent; retry of timeout or blocked script request", "retrieved_utc": "2026-09-30T23:03:33.264106+00:00", "sha256": "67a5f5b6c3d3584aad3467740dff3ac280142c910798984affa09013516d04a5", "status": "saved"}
{"error": "403 Client Error: Forbidden for url: https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf", "id": "hasz2020", "requested_url": "https://redishlab.umn.edu/sites/redishlab.neuroscience.umn.edu/files/2023-01/2020_bmh_mpfc-hc_in_nlm.pdf", "retrieval_method": "normal requests with browser user agent; retry of timeout or blocked script request", "retrieved_utc": "2026-09-30T23:03:39.013254+00:00", "status": "failed"}
```


---

## File: VALIDATION.json

```json
{
  "date": "2026-09-30",
  "offline_tests": {
    "command": "python3 -m unittest discover -s . -p test_fetch_sources.py",
    "tests": 4,
    "result": "passed"
  },
  "cached_default_rerun": {
    "command": "python3 fetch_sources.py",
    "manifest_and_history_byte_identical": true,
    "sha256_before": {
      "source_manifest.json": "adda388c5f746dd5ea20712aa4218fd5537ce1777925478710967a1bb8b42439",
      "retrieval_attempts.jsonl": "fa16e82d53a67b21489fe28ffec113c76364fc4d0fca4c96f6fc49579accdd53"
    },
    "sha256_after": {
      "source_manifest.json": "adda388c5f746dd5ea20712aa4218fd5537ce1777925478710967a1bb8b42439",
      "retrieval_attempts.jsonl": "fa16e82d53a67b21489fe28ffec113c76364fc4d0fca4c96f6fc49579accdd53"
    }
  },
  "scientific_replication": "not performed",
  "biological_experiment": "proposal only"
}
```
