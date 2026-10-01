# Complete research handoff — workflow/handoff 2.2; scientific report 2.1, 30 September 2026

Original research question: During the stuck period before a sudden insight or abrupt strategy change, is there evidence of gradual measurable brain/behaviour change, or is the neural transition abrupt too? Include human and animal studies; cite the specific study, what was measured and generalization; separate direct evidence and model analogy; end with unknowns and a settling experiment.



---

## File: README.md

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


---

## File: REPORT.md

# Hidden progress before insight or strategy change — version 2.1

Focused primary-source review, 30 September 2026. Question: during a period of apparent impasse, does useful change accumulate before sudden insight, or is the neural transition itself abrupt?

## In plain language

Feeling stuck does not necessarily mean nothing is changing. In some experiments, people’s attention shifted toward useful parts of a puzzle, and brain signals represented a different strategy before people or animals used it. But some recorded brain patterns also changed abruptly. A sudden breakthrough can therefore coexist with earlier change; that earlier change is not always gradual or demonstrably useful. We still cannot tell which process explains a particular long human impasse. The studies measured gaze, brain signals and task performance—not every change in the brain or the exact onset of conscious understanding. Examples: [Bilalić et al.](https://doi.org/10.1080/13546783.2019.1705912), [Schuck et al.](https://doi.org/10.1016/j.neuron.2015.03.015), [Powell & Redish](https://doi.org/10.1038/ncomms12830).

## Technical interpretation

**Both earlier change and abrupt transitions are documented, sometimes in the same task.** The evidence rejects a universal equation of poor performance with no learning. It also rejects the assumption that every sudden behavioural improvement reflects a gradual neural ramp. The strongest conclusion is that acquisition, neural representation, policy selection, performance and conscious recognition can have different time courses. Whether a particular human impasse contains continuous, solution-specific neural accumulation remains substantially unresolved.

This is a focused review, not an exhaustive systematic review, meta-analysis or new experiment. Version 2 expanded the original search; version 2.1 reconciles the notebook, adds this plain-language layer and checks indexed forward citations. [Search and selection audit](SEARCH_AUDIT.md), [claim inspection ledger](EVIDENCE_LEDGER.md), [review response](REVIEW_RESPONSE.md) and [change log](CHANGELOG.md) are part of the result. Full papers remain at their original hosts.

The version 2.1 indexed-citation follow-up is documented in [CITATION_INDEX_AUDIT.md](CITATION_INDEX_AUDIT.md). It adds direct leads without claiming complete screening or search saturation.

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
| [Ninomiya, Terai & Miwa (2022)](https://doi.org/10.3389/fpsyg.2022.934029). Relevant primary XML Methods/Results/Discussion. | Water-jar task: 60-Hz gaze, trial-mean horizontal position and fixation-duration proportions. Eventual discoverers attended differently in two trials before first reporting the better procedure, while still using the trained one. | A pre-expression attentional difference, not a demonstrated smooth solution ramp. Main gaze comparison used 21 finders/15 non-finders after exclusions. Initial equivalence bounds were broad (d = 0.97); they cannot establish identical starting attention. |
| [Allegra et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116854). Selected author-PDF Methods/Results/Discussion, pp. 2–5 and 9–13. | Reanalysis of Schuck's dataset: fMRI coherence in 22-second windows, summarized by blocks. Frontal connectivity increased earlier in eventual switchers, even before the colour-response correlation began. | Network dynamics and later switching propensity; the early effect cannot be accumulation of the not-yet-present colour rule. Shared data, not independent replication; neither connectivity nor averaging identifies continuous solution-content progress. |
| [Lu et al. (2023)](https://doi.org/10.1523/jneurosci.2172-22.2023). **Primary abstract and indexed excerpts only; full Methods not audited.** | Serial-reaction-time learning: session-wise awareness/RT, EEG/MEG theta and phase-transfer entropy. Reported parietal theta transfer precedes awareness by one session; precuneus rTMS changes transition rate and learning benefit. | Provisional human pre-awareness and intervention evidence. Session-level results do not show a continuous impasse ramp; transfer estimates alone are not causation. Stimulation controls/selectivity remain unchecked here; sequence learning is not a novel puzzle impasse. |

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
| [Ding et al. (2025)](https://doi.org/10.1523/jneurosci.1670-24.2025). Relevant primary XML task/decoding Methods and Results/Discussion. | Four male TH-Cre rats: simultaneous CA1, mPFC and optotagged VTA dopamine spikes during uncued rule switching. Reward-predictive dopamine firing emerges gradually with rule-decoding changes, before behavioural adaptation by several trials. | Direct reward-related neural change before expression in trained animals. Decoding curves are Gaussian-smoothed and transition-thresholded; aligned ramps are not an unsmoothed single-trial accumulation test. Optotagging identifies cells, not a causal test of switching. |
| [Russo et al. (2021)](https://doi.org/10.1523/jneurosci.2588-20.2021). **Primary abstract only.** | Male-rat mPFC multiunit recordings during extinction of alcohol-reward seeking; reported unit changes coordinate into population transitions before behavioural extinction. | Provisional neural-before-behaviour switching evidence. Extinction differs from discovering a new solution; detailed timing, model assumptions and attractor interpretation were not audited. |
| [Singh, Peyrache & Humphries (2019)](https://doi.org/10.1523/jneurosci.1370-17.2019). **Primary abstract only.** | Male-rat mPFC population activity across Y-maze training and surrounding sleep changes even without overt rule learning; learning-associated changes have different sleep carryover. | Supports the caution that measurable neural change need not be useful progress. Pre/post population plasticity is not a recorded synaptic ramp throughout impasse; full analysis not audited. |

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

# Evidence and inspection ledger — v2.1

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

## Indexed-citation additions — version 2.1

| Study / primary identifier | Code | Precisely inspected | Unresolved audit boundary |
|---|---|---|---|
| [Ninomiya 2022](https://doi.org/10.3389/fpsyg.2022.934029) | P | Primary XML task, gaze Methods, Results and Discussion. | Retrospective grouping/exclusions; coarse trial comparisons, wide equivalence bounds; no smooth ramp established. |
| [Allegra 2020](https://doi.org/10.1016/j.neuroimage.2020.116854) | S/P network | Author PDF selected pp. 2–5, 9–13. | Same Schuck dataset; early connectivity starts before useful correlation. Connectivity is not decoded solution content. |
| [Lu 2023](https://doi.org/10.1523/jneurosci.2172-22.2023) | P; intervention provisional | Primary abstract via Europe PMC; indexed primary excerpts. | Full XML failed; stimulation Methods/controls unverified, session-level timing. |
| [Ding 2025](https://doi.org/10.1523/jneurosci.1670-24.2025) | P; graded reward signal | Primary XML task/decoding Methods and relevant Results/Discussion. | Smoothed, aligned estimates in four rats; no causal switching manipulation. |
| [Russo 2021](https://doi.org/10.1523/jneurosci.2588-20.2021) | P/J provisional | Primary abstract via Europe PMC. | Full temporal/statistical Methods not inspected. |
| [Singh 2019](https://doi.org/10.1523/jneurosci.1370-17.2019) | S/plasticity provisional | Primary abstract via Europe PMC. | Sleep/training comparison, not within-impasse solution trajectory; full Methods unchecked. |

[Indexed-citation audit](CITATION_INDEX_AUDIT.md) records discovery, decisions, access failures and unscreened candidates. Download records for the two new XML files are separate from the earlier cache instrument; full text remains local.


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

# Lab Notebook — current synthesis v2.1; workflow package v2.2

Investigation started 30 September 2026. The main sections below supersede earlier summaries. Dated entries at the end retain what was known and done at each stage; pending statements there are historical. Earlier report versions are preserved in GitHub history.

## Current Question

During apparent impasse before human insight or animal strategy change, does measurable progress precede the transition, or are neural transitions also abrupt?

## Current Model

Feeling stuck can conceal earlier change, but that change need not be a smooth approach to a solution. Different tasks show gradual attention changes, earlier neural representations, abrupt recorded neural transitions and competence revealed by a different context. Acquisition, representation, strategy selection, performance and conscious recognition can have different time courses. Their relationship during a particular prolonged human impasse remains unknown.

## Competing Hypotheses

H1: Continuous solution-specific accumulation precedes abrupt report/output.
H2: A rapid representational transition produces abrupt recorded neural change.
H3: Earlier learning enables a later switch; task context gates expression.
H4: Averaging, filtering, response alignment or selection creates apparent ramps/jumps.
H5: Local learning can produce sudden end-to-end success without a global insight transition; Reddy's model and shared-data behavioural reanalysis make this an alternative, not an observed neural mechanism.

## Assumptions

Animal switching illuminates some strategy dynamics, without establishing animal Aha experience or equivalence to novel human puzzle insight. Recorded neural activity is not identical to synaptic learning. Earlier activity and drift are not automatically useful progress. A null result does not establish absence; decoding is not causality. Verification depth and evidence strength are separate.

## Experiments Run

Focused literature audits and provenance checks, followed by a three-anchor indexed forward-citation check. No new biological experiment, original-data reanalysis or replication of the cited studies. Retrieval instrument tests address file integrity/repeatability, not scientific conclusions. The scientific report/ledger remain version 2.1. A supplied fresh-answer comparison found additional leads and two confirmed citation/attribution errors; it was not a controlled workflow experiment. The new prospective discovery path is adopted in workflow package v2.2, without claiming a new isolated discovery run. Current handoff documents are under research/2026-09-30-hidden-progress/v22.

## Results

[The report](REPORT.md) and [inspection ledger](EVIDENCE_LEDGER.md) are authoritative for study-specific measurements and limits. Full relevant primary reading supports heterogeneous individual gaze trajectories in Bilalić, coarse pre-response attentional changes in Knoblich/Tseng, and neural representations preceding human switching in Schuck/Rose. Powell and Hasz support earlier rat neural state changes, without establishing a continuous solution ramp. Indexed follow-up adds Ninomiya's pre-expression gaze difference, Allegra's shared-data/pre-correlation connectivity, and Ding's earlier reward-related firing with smoothed decoding. Lu's human theta/stimulation, Russo's extinction and Singh's nonspecific plasticity remain provisional at abstract or excerpt depth. Townsend measures abrupt human aiming changes, not brain activity or independently reported Aha onset. Rosenberg shows both abrupt and gradual mouse behavioural improvement; Reddy supplies a competing model with reused behavioural data. Kuchibhotla supports context-dependent latent competence. Ellis, Kounios, Durstewitz and Karlsson remain abstract/preview-only; Drieu remains a two-page reading. Those limitations prevent upgrading them to fully verified strong/causal evidence. Nanda and other artificial systems remain analogies. The subsequent fresh-answer comparison identifies further developmental, primate, movement-dynamics and overtraining candidates in [DISCOVERY_RECONCILIATION.md](DISCOVERY_RECONCILIATION.md); their stated reading depths are preserved, and they have not been promoted to fully audited report findings.

## Failed Approaches

The v1 search stopped without defensible yield evidence and omitted relevant studies. An unlabeled download list could not reconstruct selection history. Some primary retrievals failed because of access checks, timeouts or extraction failures; available bytes did not establish reading. V2 corrected the report but failed to reconcile these notebook main sections and left stale placeholders. This version repairs that reporting failure while preserving historical entries. Web searches could not provide a genuine forward-citation export; the indexed follow-up now addresses that narrow gap, without proving comprehensive coverage. Further relevant leads in an externally supplied fresh answer show that the audited search remained incomplete; new discovery routes need explicit reconciliation.

## Surprises / Anomalies

Graf's abrupt illustration uses simulated data rather than the original gradual empirical shift. Powell's neural change precedes behaviour yet is itself described as abrupt: precedence and gradualness are independent. Hasz's measurable drift need not be learning progress. Bilalić has 19% unclassifiable trajectories and a p = .06 subjective-suddenness comparison. Tseng has internal reporting discrepancies. Indexed citations yield further relevant leads, so neither repeated familiar hits nor this correction establishes saturation. Fresh Opus added complementary populations/measures while missing studies our review retained. Its acceptance of two citation mistakes supports those primary checks, not a causal workflow-performance claim.

## Strongest Evidence For

For measured gradual behavioural change: Bilalić's individual trajectories, with classification/time-bin limitations; Knoblich/Tseng add coarser attentional evidence. For neural-before-behaviour change: relevant primary methods/results in Schuck, Rose, Powell, Hasz and Ding, with small/task-specific samples and block/lap/trial resolution. For acquisition/expression separation: Kuchibhotla's context probes. These support different claims, not one universal continuous accumulation mechanism. Ellis and Drieu remain provisional at their stated inspection depths and are not elevated here.

## Strongest Evidence Against

Against universal smooth recorded neural change: Powell's abrupt strategy transitions and Siniscalchi's rapid population change; Durstewitz/Karlsson are supplementary abstract-level leads. Against universal smooth behavioural change: abrupt trajectories coexist with gradual ones in Bilalić/Rosenberg; Townsend detects single-trial aiming shifts. Against interpreting every early signal as progress: preparation and rule-independent drift lack demonstrated solution-specific accumulation. None rules out earlier change in unobserved synapses or regions.

## Kill Zones

H1 requires prospective solution-content prediction and must survive alignment/leakage controls; it is weakened by adequately powered equivalence bounds excluding a meaningful ramp. H2 is weakened if continuous content changes explain held-out data better than rapid transitions. H3 must outperform simpler accumulation/switch/selection models rather than absorbing every result. H4 is weakened by replicated raw individual trajectories with independent timing. H5 must predict route-length-dependent learning and causal dynamics beyond a retrospective fit.

## Robust Findings

1. Subjective suddenness does not establish absence of earlier objective change.
2. Earlier brain activity does not establish graded, solution-specific progress.
3. Some recorded population transitions are fast at their sampled resolution.
4. Learning and ordinary behavioural expression can dissociate in specific tasks.
5. Averaging, sampling, exclusions and alignment can change apparent trajectory shape.

## Speculative Interpretations

Thresholded accumulation, attractor switching and strategy selection remain candidate mechanisms. No universal mechanism or measured synaptic trajectory through natural impasse is established.

## Newly Discovered Abstractions

Separate acquisition, representation, strategy selection, expression and recognition; distinguish solution-content precursors from preparation/drift; distinguish an indexed citation from a verified relevant finding. Separate fresh discovery from criticism of an existing draft; preserve complementary coverage before reconciling candidates.

## Next Best Experiment

Prospective solution-content decoding trained independently; individual ramp/changepoint/hybrid/local-learning model comparison; model-recovery, equivalence, alignment and no-report/probe controls; randomized closed-loop rodent perturbations. [The proposed experiment](NEXT_EXPERIMENT.md) is unrun. A new toy simulation alone would not settle the biological question. For the method addition, evaluate fresh discovery versus usual search with model, tools and budget held fixed across several questions; use blinded checks of consequential omissions, citation precision, unsupported claims, clarity and cost.

## Confidence / Remaining Uncertainty

High confidence in the task-bounded coexistence of earlier measured change and abrupt expression/recorded transitions in fully inspected studies. Moderate confidence in the mixed organizing account; low confidence in prevalence, continuous synaptic accumulation, precursor necessity or generalization to prolonged natural human impasses. Limited-reading papers retain lower verification. Indexed coverage and deeper methods checks remain incomplete. Independent Opus feedback on v2 is user-supplied review testimony; the current corrections are self-checked, not a fresh independent review. The discovery-stage addition is promising but has not been prospectively tested; the supplied comparison lacks controlled prompts/settings/budgets.

## Historical dated entries

The entries below preserve the chronology. Their then-current claims and unfinished actions are not the current synthesis above.

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

## V2 publication completed and verified, 2026-09-30

Published the complete v2 handoff to https://github.com/jorgy72/hidden-progress-insight-research at commit 8444c2d2148270f7af0a09c4945f33a469658ecd using a non-forced main update based on the verified v1 parent. Original nine v1 files preserved byte-for-byte under versions/v1 and in original commit history. Public package contains 30 files and excludes full papers, extracted article text, figure renders, unrelated notebooks and private local paths.

Connector fetch of main/FULL_RESEARCH.md matched local text exactly (135,959 characters). Anonymous pinned raw retrieval verified SHA256 hashes for all 30 public files, including the hash manifest; web reader also fetched the complete handoff without authentication. Publication receipt: research/2026-09-30-hidden-progress/PUBLICATION_V2.json. The published notebook is a frozen pre-publication snapshot: its historical pending entry describes its state at that entry, superseded by this local completion receipt. No independent v2 review or original-study replication was performed.

## Version 2.1 review corrections prepared, 2026-09-30

The user's independent Opus review of published v2 was checked against local artifacts. Main notebook sections reconciled; plain-language report opening added; source location removed from current workflow. Europe PMC and NCBI indexed forward retrieval succeeded for three anchors, yielding 317 Europe PMC anchor-record links/299 source-ID pairs. Fifteen selected primary abstracts checked; six studies added at actual inspection depth. Other records remain unscreened/deferred. Lu full XML failed with HTTP 500; Ding/Ninomiya XML succeeded. No saturation, complete global citing index, full causal Lu audit or fresh independent amendment review is claimed. Current changes await publication verification at this dated entry.

## Version 2.1 publication verified, 2026-09-30

Published commit b297a0aa3dbb26cc81aeeeb2061d53b145a5af19 at https://github.com/jorgy72/hidden-progress-insight-research. Anonymous pinned raw retrieval verified exact SHA256 bytes for all 36 public files; main/FULL_RESEARCH.md also matched the local handoff. Receipt: research/2026-09-30-hidden-progress/PUBLICATION_V21.json. The public notebook snapshot preserves its prepared/pending entry as dated history, superseded by this local receipt. The substantive main sections published are current. Six added studies retain their actual inspection depths, and full indexed screening/global coverage remain incomplete. Current public workflow omits the private source location; older commits were not rewritten.

## Fresh unstructured Opus comparison, 2026-09-30

Compared supplied fresh response with published v2.1; audit in research/2026-09-30-hidden-progress/fresh-opus-comparison/COMPARISON.md. New relevant child, primate, movement-dynamics and overtraining leads expose remaining coverage gaps. Targeted primary checks confirmed wrong Ellis DOI link and rat neural-finding misattribution to Jang (actual Bissonette & Roesch). Core conclusions overlap, but fresh prevalence/causal exclusivity statements exceed displayed support. Bilalic attention-onset association and individual subgroup p=.06 are different analyses; do not conflate them. Unseen fresh tool execution cannot be judged; this is not a controlled workflow evaluation. No full source rerun or new GitHub revision performed. Full fresh text/provenance and local primary checks preserved.

## Fresh discovery path adopted, 2026-09-30

User explicitly requested adding the discovery path and supplied Opus's follow-up acceptance of confirmed errors. WORKFLOW.md now requires a neutral brief, fresh-context exposure record, bounded search, saved discovery output and candidate reconciliation before synthesis. Added research/FRESH_DISCOVERY_TEMPLATE.md and expanded the literature-audit template. Reading-depth and identity checks remain compulsory; unavailable independence is disclosed rather than invented. Retrospective project reconciliation preserves new leads, unresolved checks and reviewer-vs-primary distinctions. Scientific report/ledger remain v2.1; this is a workflow/handoff v2.2 update, not a new literature rerun or controlled benchmark. Publication verification follows separately.


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

## Dated follow-up — version 2.1

Original v2 plan above is preserved. The registered indexed-citation follow-up is in [CITATION_INDEX_PLAN.json](CITATION_INDEX_PLAN.json). The second user-supplied Opus review concerns the published v2; current amendments are self-checked. Indexed retrieval is complete only for its returned pages/three anchors, not for every global citing paper or full relevance screening.


---

## File: SEARCH_AUDIT.md

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
{"date": "2026-09-30", "batch": "V2.1-indexed", "service": ["Europe PMC REST citations", "NCBI ELink pubmed_pubmed_citedin"], "anchors": ["25819613", "27653278", "11820744"], "queries_and_raw_metadata": "CITATION_INDEX_RESULTS.json", "selected_primary_checks": "CITATION_SCREENING_LOG.json", "stop": "Registered three-anchor/priority follow-up delivered; ongoing yield and unscreened metadata prevent saturation claim."}
```


---

## File: REVIEW_RESPONSE.md

# Review responses — versions 1, 2 and 2.1

The user supplied an independent model review of **version 1**. Its assertions were leads, checked where consequential against primary sources. At publication, version 2 received a skeptical **self-review by the same author**. The user has now supplied a second independent Opus critique of the published v2. Version 2.1 responds to it; its amendments are self-checked, without a fresh independent review. No paper/data replication was performed.

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
| End with independent critic | **Partially fulfilled.** Earlier independent Opus review retained as v1 feedback; v2 self-review completed and labelled. At v2 publication it was outstanding; the user-supplied v2 review now supplies that feedback. |

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

The remaining evidence gap is substantive: no universal causal account of continuous solution-specific neural accumulation throughout genuine impasse. Improved reporting does not close that gap. At that time an independent v2 review was outstanding. That feedback has now arrived; fuller access to limited-inspection papers and independent review of these amendments remain useful.

## Response to the user-supplied independent review of v2 — 30 September 2026

| Review finding | Check and version 2.1 action |
|---|---|
| Main notebook is stale and overstates Ellis/Drieu | **Accepted after local inspection.** Rewrote all main sections from the current ledger, restored failures/anomalies, downgraded limited-reading papers and preserved dated entries as explicitly historical. New indexed leads are reconciled in the main synthesis too. |
| Missing plain-language layer | **Accepted.** Short opening paragraph in report and README; technical evidence and uncertainty remain underneath. |
| Forward citations are still web-search only | **Accepted for v2; addressed in a bounded follow-up.** Both Europe PMC citations and NCBI citedin succeeded for three anchors. Exact queries, raw metadata, response hashes, selected primary checks and remaining unscreened records are public. Neither index guarantees every later citing paper. |
| Private relative iCloud source path remains | **Accepted after inspecting current WORKFLOW export.** Removed the complete local source location, including relative folder names, from the current workflow and rebuilt handoff. Public Git history retains earlier versions; no history rewrite or claim of complete historical erasure. |

Reviewer spot-checks are testimony, not independent primary verification by this author. No confidence upgrade was assigned to abstract/partial sources merely because the reviewer approved them. The optional Townsend model-count detail was not needed for these corrections and was not promoted solely from the review.

## Self-check of the amendments

Checked notebook/report consistency, every added study's inspection label, actual indexed API success/counts, duplicate publication families, publication-date limits and complete-export privacy/link integrity. Allegra's shared dataset/pre-correlation signal, Ding's smoothing and Ninomiya's broad equivalence bounds were checked in primary text. Lu's XML failure prevents a full causal-method claim. Remaining index records are explicitly unscreened/deferred, not silent exclusions. No new biological study or original-data replication was run.

## Fresh-answer comparison and subsequent Opus feedback — workflow v2.2

The user supplied fresh Opus output and a subsequent acceptance of the two independently checked citation errors. Adopted a prospective fresh-discovery stage before exposure to the existing synthesis; [reconciliation](DISCOVERY_RECONCILIATION.md) records candidate status and remaining checks. Opus's concessions are feedback, not additional primary verification. Its proposed causal explanation of errors and overall workflow score remain untested. A missing study can materially change conclusions, so coverage checks retain equal methodological importance. No new independent review of this workflow amendment or fresh research run is claimed.


---

## File: CHANGELOG.md

# Dated changes

## Workflow/handoff version 2.2 — 30 September 2026

User-authorized addition of fresh discovery before exposure to the existing draft. Added a neutral prompt/context/freeze/reconciliation template and expanded the literature-audit template. Made same-study author/title/version/identifier mapping explicit. Added retrospective reconciliation of the fresh Opus leads and qualified its follow-up judgments. Reconciled the notebook's main sections and retained its dated history.

The report, scientific evidence ledger and experiment proposal retain their v2.1 contents and inspection limits. No new independent discovery run, full literature rerun, causal workflow benchmark or upgraded source reading is claimed. Prior package [v2.1 is preserved](https://github.com/jorgy72/hidden-progress-insight-research/tree/b297a0aa3dbb26cc81aeeeb2061d53b145a5af19).

## Version 2.1 — 30 September 2026

Responds to the user-supplied independent Opus review of v2. Reconciles every notebook main section with the actual verification ledger; historical entries are preserved and labelled. Restores concrete failed approaches/anomalies. Adds a short plain-language opening to the report/README and makes those requirements explicit in the workflow.

Adds a registered three-anchor Europe PMC/NCBI forward-citation check with exact queries, response hashes, metadata export and selected primary screening. Six further studies enter the report at their actual reading depths. A pre-correlation frontal signal, smoothing and exclusion/equivalence limits are explicit. This remains bounded follow-up with unscreened leads, not comprehensive citation screening or saturation.

Removes the local source folder location from the current workflow/export. Earlier public commits retain historical content; their history was not rewritten. The v2 publication is preserved at [its commit](https://github.com/jorgy72/hidden-progress-insight-research/tree/8444c2d2148270f7af0a09c4945f33a469658ecd). The amendments are self-checked, with no fresh independent v2.1 review or biological experiment.

## Version 2 — 30 September 2026

Authorized research rerun and publication after Opus's v1 critique. Expanded primary-source/citation searches; added the three omissions and related studies/alternative mechanisms. The central conclusion remains mixed, with stronger animal evidence that neural change can precede behaviour while still being abrupt.

Added exact query batches, selection/access log, coverage/stopping audit, registered scope, visible claim-level inspection labels, critic-response table and honestly labelled self-review. Restored unclassifiable gaze trajectories and qualified borderline evidence. Separated preparatory/autonomic states, neural precursors, abrupt transitions, latent competence and artificial mechanisms. Corrected grokking phase order and marked reused datasets.

Repaired retrieval provenance and caching; added meaningful offline failure tests and a verified no-change cached rerun. Preserved v1 manifest/history and original public files. Added local-learning alternatives, model-recovery/equivalence checks and changepoint-alignment controls to the unrun experiment proposal.

At the time of v2 publication, no original-study replication, new biological experiment or independent v2 critic review was claimed. Some studies remain abstract/preview or partial-page only. This is a focused review, not systematic search saturation.

## Version 1 — 30 September 2026

Original publication at commit `a0dad4503c621923d42299cf8fdc377c3d13d03b`; original files archived in [versions/v1](versions/v1). Its coverage, stop claim, category labels, percentage reporting and retrieval script limitations are superseded by v2. Preserve it as historical evidence, not the current recommendation.


---

## File: WORKFLOW.md

# Recursive Discovery Lab

Workspace operating method adopted by the user from the five-page `Research lab prompt.pdf`.

Source: user-provided `Research lab prompt.pdf`. Local source location omitted from shareable documents.

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

### Fresh discovery before reading the existing synthesis

Added 2026-09-30 after comparing a fresh Opus answer with the audited insight review. Their complementary coverage motivates this addition; one uncontrolled comparison does not establish that the method improves accuracy.

For substantial literature investigations, use this sequence: **neutral brief -> fresh discovery -> freeze the discovery record -> reconcile with the ledger -> verify and synthesize -> critic pass**. This discovery pass complements the later critic: it searches without knowing the draft's preferred account, while the critic examines the assembled result.

- Before the discovery researcher sees the draft, give only the original question, user constraints, cutoff, scope, output requirements and source-checking rules. Withhold the current answer, chosen anchors, bibliography, evidence ledger and reviewer omission lists. Choose search routes from the question, covering supporting, opposing and null findings, populations/development/species, tasks, measures, timescales and alternative mechanisms. A previous report must not define the entire search space.
- Use a separate researcher in a fresh context when available and authorized. A new role, second pass, or model label in the same exposed conversation is not independent discovery. Record researcher/model/settings if known, the exact brief and what material was visible; disclose accidental exposure. If fresh context is unavailable, perform a bounded exploratory search but label it as an already-exposed search. Continue the authorized work without inventing independence or blocking delivery solely on this step.
- Declare the pass's scope and practical stopping bound before searching. Produce a concise candidate map, exact search/citation routes, source identifiers and inspection/access status, including contrary evidence and empty routes. Check each cited author, title, publication version/year and DOI/PMID/URL against a primary record. Unresolved mappings remain unverified leads; preserve the original mismatch and correction. Do not infer full reading from access or repeat a model's claim as a source finding.
- Save the discovery output, brief, search log and known context before exposing the researcher to the existing draft. Record a timestamp and file hash when available. For externally supplied work, preserve the received text and mark missing prompt/settings/search history as unknown; do not reconstruct them as contemporaneous evidence.
- Then reconcile every material candidate with the current evidence ledger: existing evidence, genuinely new relevant lead, duplicate publication/dataset, background, excluded with reason, or deferred with a named next check. Check original primary methods/results before promoting a consequential claim; carry the actual reading depth into every summary. Count distinct studies separately from publications and datasets. Reopen the affected coverage route when a material gap appears.
- Report what the fresh pass added or challenged, its marginal verification/search cost if known, and what remains unresolved. A negative/no-new-lead pass is also a result. Do not select a story by how confidently or elegantly a model narrates it, and do not claim saturation from a bounded pass.

Use [FRESH_DISCOVERY_TEMPLATE.md](FRESH_DISCOVERY_TEMPLATE.md) for the neutral brief, discovery record and reconciliation. Keep the opening answer readable: one short plain-language account with its main uncertainty, followed by the technical ledger. Missing evidence can change a conclusion, so audit consequential omissions alongside citation errors.

### Search provenance and coverage

- Define inclusion/exclusion criteria and a coverage map before searching: populations/species, tasks, measures, timescales, competing mechanisms, supporting and opposing findings. Search for each materially different explanation rather than following only the first promising papers.
- Maintain a structured SEARCH_LOG alongside the notebook. For each batch record the date, exact queries, search engine/database and filters, candidate identifiers/URLs, discovery route, inclusion/exclusion/defer reasons and access failures. Raw search results and download manifests supplement this log; they do not replace it. Mark retrospective reconstruction as retrospective, and unknown queries as unknown.
- Use available citation indexes (for example NCBI ELink citedin or Europe PMC citations) for forward retrieval; author-name web searches are only a fallback. Record complete returned-page retrieval separately from relevance screening; check publication dates and preprint/final duplicates before treating records as cutoff-qualified independent studies. Every index has coverage limits.
- Follow backward references and forward citations from the central anchor papers. Record which anchors were checked, the service and date, relevant candidates and decisions, and any unavailable citation index. Include a targeted recent-literature search through a stated cutoff date. Citation proximity alone does not establish relevance or independence.
- Before stopping, record the yield of the final search and citation-chasing batches: new relevant candidates, new measures/mechanisms or contradictions, and changes to the synthesis. Review unfilled coverage areas and unresolved directly relevant leads. Repeatedly finding familiar papers is not sufficient evidence of saturation.
- If stopping because of access, time or diminishing returns, state that reason and the remaining gaps. Do not substitute an unsupported claim of low information gain. Discovery of a material omission reopens the affected part of the search rather than requiring every source to be collected.

### Claim-level verification

- Resolve the cited author/title/publication version and identifier to the same primary study before using a citation. A real paper behind a wrong DOI or wrong author attribution is still a citation error; record and correct it.
- Carry verification into the final report at the point of the claim, including evidence-table rows: relevant full-text methods/results inspected; named pages/figures inspected; abstract/preview only; or secondary/unverified lead. Downloading or extracting a file does not establish that its contents were read. Full-text access does not mean the entire study or supplements were audited.
- Keep verification depth separate from evidential strength. Record task, participants/animals, measured variable, temporal resolution, analysis, what the result supports, alternative explanations and generalization limits. Avoid conclusions that require unavailable methods or results.
- Maintain an evidence ontology that follows the question. Preparatory state, solution-related precursor, gradual accumulation, abrupt transition, latent knowledge and analogy can differ and coexist. Temporal precedence does not establish gradualness, causality or correct solution content.
- Inspect figure captions, footnotes and methods for simulated versus empirical data, averaging, filtering, alignment and exclusions. Report denominators and residual/unclassifiable groups when giving category percentages. Avoid treating linked analyses of one dataset as independent replication.
- Audit descriptions of multi-stage mechanisms for temporal order; internal mechanism formation and visible performance change need not occur in the same stage.

### Reproducibility and handoff

- Use a declared source list and stable source identifiers. Reconcile it with the retrieval manifest; explain historical attempts, alternate URLs, excluded leads and script changes rather than claiming the current script reproduces every past action.
- Repeated default retrieval must not silently append duplicate stable records. Reuse validated cached files; keep explicit refresh/retry attempts in a separate dated history and update a deduplicated current view. Preserve failures and changed hashes. Verify this behaviour before calling an instrument repeatable.
- Before sharing a revision, reconcile the notebook's main sections with the current evidence ledger. Preserve dated entries as history, label superseded conclusions and remove stale placeholders. Inspection limits must travel with claims in every summary, including the notebook.
- Check current public exports for personal paths and unnecessary private context, including relative folder names; removing only the username is insufficient. Preserve research provenance without publishing local source locations.
- Share the search/selection log, evidence ledger, verification limits, notebook, exclusions and experiment status with the final report. Check that the handoff actually includes them. Preserve the original version and provide a dated change log for revisions; distinguish local edits from published revisions.

### Critic pass and response

- For substantial syntheses, seek an independent critic when available and authorized. Give the critic the question, scope, full draft, search/selection log and access ledger. Ask specifically for missing counterevidence, unjustified stopping, incorrect timing/measurement interpretation, confidence inflation and reproducibility failures.
- If independent review is unavailable, perform a separate skeptical self-check and label it as self-review. Do not call a second pass by the same author independent or claim an unperformed review.
- Treat a critic's report as leads, not proof. Check important criticisms against primary sources and local artifacts; keep a response table with accepted, qualified, rejected or unresolved findings, evidence and concrete actions. Fix material problems, recheck changed claims and record remaining limitations before presenting a revision as reviewed.

## Output style

Prefer experiments over speculation, mechanisms over labels, discriminating evidence over volume of evidence, small executable models over elaborate verbal theories, and uncertainty over false precision.

Explain useful results at two levels:

1. A short plain-language interpretation at the start, preserving the key uncertainty and giving primary-source examples.
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
  "biological_experiment": "proposal only",
  "version_2_1": {
    "date": "2026-09-30",
    "notebook_main_sections_reconciled": true,
    "notebook_export_matches_current": true,
    "plain_language_opening_present": true,
    "current_export_private_paths_absent": true,
    "v1_archive_byte_identical": true,
    "all_three_anchor_index_requests_succeeded": true,
    "returned_europe_pmc_pages_complete": true,
    "selected_primary_records": 15,
    "selected_publication_dates_within_cutoff": true,
    "all_index_records_fully_screened": false,
    "global_citation_coverage_complete": false,
    "fresh_independent_amendment_review": "not performed",
    "publication_verification": "separate receipt after publication",
    "syntax_check": "ast.parse passed; py_compile attempted a system cache write and was replaced with a read-only parse"
  },
  "version_2_2": {
    "scientific_report_ledger_experiment_byte_identical_to_2_1": true,
    "notebook_export_matches_current_at_build": true,
    "workflow_matches_canonical_except_export_relative_link": true,
    "reusable_templates_match_canonical": true,
    "date": "2026-09-30",
    "new_fresh_context_research_run": "not performed; received output reconciled retrospectively",
    "new_primary_reading_upgrades": "none",
    "fresh_independent_method_review": "not performed",
    "performance_benefit": "untested",
    "publication_verification": "separate receipt after publication",
    "unchanged_retrieval_tests": "earlier results retained as history; not rerun for document-only change"
  }
}
```


---

## File: CITATION_INDEX_PLAN.json

```json
{
  "cutoff": "2026-09-30",
  "anchors": {
    "Schuck2015": "25819613",
    "PowellRedish2016": "27653278",
    "Knoblich2001": "11820744"
  },
  "scope": "Three-anchor indexed forward check, not an exhaustive literature search.",
  "screening": "Metadata discovery followed by title triage and primary-source checking of potentially direct new leads.",
  "coverage_limit": "Europe PMC citations use open PMC/Crossref data; NCBI citedin is a subset, not every global citing paper."
}
```


---

## File: CITATION_INDEX_RESULTS.json

```json
{
  "plan": {
    "cutoff": "2026-09-30",
    "anchors": {
      "Schuck2015": "25819613",
      "PowellRedish2016": "27653278",
      "Knoblich2001": "11820744"
    },
    "scope": "Three-anchor indexed forward check, not an exhaustive literature search.",
    "screening": "Metadata discovery followed by title triage and primary-source checking of potentially direct new leads.",
    "coverage_limit": "Europe PMC citations use open PMC/Crossref data; NCBI citedin is a subset, not every global citing paper."
  },
  "retrieved_at_utc": "2026-09-30T23:26:44.172235+00:00",
  "anchors": {
    "Schuck2015": {
      "pmid": "25819613",
      "europe_pmc_queries": [
        {
          "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/MED/25819613/citations?format=json&page=1&pageSize=1000",
          "response_sha256": "5d72e33654c75a4a7038940ac807a46feeea71cfa555dc658d1ff20a80d5f3c1",
          "hitCount": 105
        }
      ],
      "records": [
        {
          "source": "MED",
          "id": "42323994",
          "citationType": "review; journal article",
          "title": "Individual-specific precision neuroimaging of learning-related plasticity.",
          "authorString": "Leipold S, Moffat R.",
          "journalAbbreviation": "Neurosci Biobehav Rev",
          "pubYear": 2026,
          "volume": "188",
          "pageInfo": "106824",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "42215782",
          "citationType": "meta-analysis; journal article",
          "title": "Consistent neural evidence to support novelty and appropriateness processing for creative thinking: a coordinated meta-analysis using activation likelihood estimation.",
          "authorString": "Lin J, He Y, Zhang S, Mo L, Kuang C, Chen Y.",
          "journalAbbreviation": "Brain Struct Funct",
          "pubYear": 2026,
          "volume": "231",
          "issue": "5",
          "pageInfo": "74",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "41650240",
          "citationType": "research-article; journal article",
          "title": "Sensory integration, temporal prediction, and rule discovery reflect interdependent inference processes.",
          "authorString": "Benjamin L, Morillon B, Wyart V.",
          "journalAbbreviation": "Proc Natl Acad Sci U S A",
          "pubYear": 2026,
          "volume": "123",
          "issue": "6",
          "pageInfo": "e2524629123",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "41308940",
          "citationType": "research-article; journal article",
          "title": "Time-resolved functional connectivity during visuomotor graph learning.",
          "authorString": "Loman S, Caciagli L, Patankar SP, Kahn AE, Szymula KP, Nyema N, Bassett DS.",
          "journalAbbreviation": "Neuroimage",
          "pubYear": 2026,
          "volume": "325",
          "pageInfo": "121617",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "40882180",
          "citationType": "research support, non-u.s. gov't; research-article; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "Practice reshapes the geometry and dynamics of task-tailored representations.",
          "authorString": "Kikumoto A, Shibata K, Nishio T, Badre D.",
          "journalAbbreviation": "Cereb Cortex",
          "pubYear": 2025,
          "volume": "35",
          "issue": "8",
          "pageInfo": "bhaf125",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "40569931",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "N2 sleep promotes the occurrence of 'aha' moments in a perceptual insight task.",
          "authorString": "L\u00f6we AT, Petzka M, Tzegka MM, Schuck NW.",
          "journalAbbreviation": "PLoS Biol",
          "pubYear": 2025,
          "volume": "23",
          "issue": "6",
          "pageInfo": "e3003185",
          "citedByCount": 4
        },
        {
          "source": "PPR",
          "id": "PPR1013354",
          "citationType": "preprint",
          "title": "Sensory integration, temporal prediction and rule discovery reflect interdependent inference processes",
          "authorString": "Benjamin L, Morillon B, Wyart V.",
          "pubYear": 2025,
          "citedByCount": 1
        },
        {
          "source": "PPR",
          "id": "PPR1009617",
          "citationType": "preprint",
          "title": "Cognitive Graphs of Latent Structure in Rostral Anterior Cingulate Cortex",
          "authorString": "Manakov M, Proskurin M, Wang H, Kuleshova E, Lustig A, Behnam R, Druckmann S, Tervo DGR, Karpova AY.",
          "pubYear": 2025,
          "citedByCount": 4
        },
        {
          "source": "PPR",
          "id": "PPR993990",
          "citationType": "preprint",
          "title": "Recasting adaptation as strategy inference",
          "authorString": "Beaumont S, Khamassi M, Domenech P.",
          "pubYear": 2025,
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "39929102",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Common and unique network basis for externally and internally driven flexibility in cognition: From a developmental perspective.",
          "authorString": "Huang Z, Yin D.",
          "journalAbbreviation": "Dev Cogn Neurosci",
          "pubYear": 2025,
          "volume": "72",
          "pageInfo": "101528",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "39847600",
          "citationType": "research-article; journal article",
          "title": "Cost-benefit tradeoff mediates the transition from rule-based to memory-based processing during practice.",
          "authorString": "Yang G, Jiang J.",
          "journalAbbreviation": "PLoS Biol",
          "pubYear": 2025,
          "volume": "23",
          "issue": "1",
          "pageInfo": "e3002987",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "39882026",
          "citationType": "research-article; journal article",
          "title": "Theta and beta power in the subthalamic nucleus responds to conflict across subregions and hemispheres.",
          "authorString": "Bowersock JL, Wylie SA, Alhourani A, Zemmar A, Holiday V, Hedera P, Stewart T, Bridwell E, Hattab I, Ugiliweneza B, Neimat JS, van Wouwe NC.",
          "journalAbbreviation": "Brain Commun",
          "pubYear": 2025,
          "volume": "7",
          "issue": "1",
          "pageInfo": "fcaf021",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "39715747",
          "citationType": "research-article; journal article",
          "title": "Broadscale dampening of uncertainty adjustment in the aging brain.",
          "authorString": "Kosciessa JQ, Mayr U, Lindenberger U, Garrett DD.",
          "journalAbbreviation": "Nat Commun",
          "pubYear": 2024,
          "volume": "15",
          "issue": "1",
          "pageInfo": "10717",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "39585903",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "An inductive bias for slowly changing features in human reinforcement learning.",
          "authorString": "Hedrich NL, Schulz E, Hall-McMaster S, Schuck NW.",
          "journalAbbreviation": "PLoS Comput Biol",
          "pubYear": 2024,
          "volume": "20",
          "issue": "11",
          "pageInfo": "e1012568",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "39557563",
          "citationType": "research-article; journal article",
          "title": "Impulsive Choices Emerge When the Anterior Cingulate Cortex Fails to Encode Deliberative Strategies.",
          "authorString": "White SM, Morningstar MD, De Falco E, Linsenbardt DN, Ma B, Parks MA, Czachowski CL, Lapish CC.",
          "journalAbbreviation": "eNeuro",
          "pubYear": 2024,
          "volume": "11",
          "issue": "11",
          "pageInfo": "ENEURO.0379-24.2024",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "39547861",
          "citationType": "research support, non-u.s. gov't; review; journal article",
          "title": "Representational spaces in orbitofrontal and ventromedial prefrontal cortex: task states, values, and beyond.",
          "authorString": "Moneta N, Grossman S, Schuck NW.",
          "journalAbbreviation": "Trends Neurosci",
          "pubYear": 2024,
          "volume": "47",
          "issue": "12",
          "pageInfo": "1055-1069",
          "citedByCount": 21
        },
        {
          "source": "MED",
          "id": "39432516",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Abrupt and spontaneous strategy switches emerge in simple regularised neural networks.",
          "authorString": "L\u00f6we AT, Touzo L, Muhle-Karbe PS, Saxe AM, Summerfield C, Schuck NW.",
          "journalAbbreviation": "PLoS Comput Biol",
          "pubYear": 2024,
          "volume": "20",
          "issue": "10",
          "pageInfo": "e1012505",
          "citedByCount": 4
        },
        {
          "source": "PPR",
          "id": "PPR911591",
          "citationType": "preprint",
          "title": "Practice Reshapes the Geometry and Dynamics of Task-tailored Representations",
          "authorString": "Kikumoto A, Shibata K, Nishio T, Badre D.",
          "pubYear": 2024,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "39134298",
          "citationType": "research support, u.s. gov't, p.h.s.; research-article; review; journal article",
          "title": "Alcohol, flexible behavior, and the prefrontal cortex: Functional changes underlying impaired cognitive flexibility.",
          "authorString": "Nippert KE, Rowland CP, Vazey EM, Moorman DE.",
          "journalAbbreviation": "Neuropharmacology",
          "pubYear": 2024,
          "volume": "260",
          "pageInfo": "110114",
          "citedByCount": 32
        },
        {
          "source": "PPR",
          "id": "PPR874911",
          "citationType": "preprint",
          "title": "N2 Sleep Inspires Insight",
          "authorString": "L\u00f6we AT, Petzka M, Tzegka M, Schuck NW.",
          "pubYear": 2024,
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "38916598",
          "citationType": "research-article; journal article",
          "title": "Reconfigurations of cortical manifold structure during reward-based motor learning.",
          "authorString": "Nick Q, Gale DJ, Areshenkoff C, De Brouwer A, Nashed J, Wammes J, Zhu T, Flanagan R, Smallwood J, Gallivan J.",
          "journalAbbreviation": "Elife",
          "pubYear": 2024,
          "volume": "12",
          "pageInfo": "RP91928",
          "citedByCount": 10
        },
        {
          "source": "MED",
          "id": "38899521",
          "citationType": "research-article; journal article",
          "title": "Stochastic characterization of navigation strategies in an automated variant of the Barnes maze.",
          "authorString": "Lee JY, Jung D, Royer S.",
          "journalAbbreviation": "Elife",
          "pubYear": 2024,
          "volume": "12",
          "pageInfo": "RP88648",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "38528782",
          "citationType": "review; journal article",
          "title": "Neural representation in active inference: Using generative models to interact with-and understand-the lived world.",
          "authorString": "Pezzulo G, D'Amato L, Mannella F, Priorelli M, Van de Maele T, Stoianov IP, Friston K.",
          "journalAbbreviation": "Ann N Y Acad Sci",
          "pubYear": 2024,
          "volume": "1534",
          "issue": "1",
          "pageInfo": "45-68",
          "citedByCount": 11
        },
        {
          "source": "MED",
          "id": "38447579",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Behavioral strategy shapes activation of the Vip-Sst disinhibitory circuit in visual cortex.",
          "authorString": "Piet A, Ponvert N, Ollerenshaw D, Garrett M, Groblewski PA, Olsen S, Koch C, Arkhipov A.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2024,
          "volume": "112",
          "issue": "11",
          "pageInfo": "1876-1890.e4",
          "citedByCount": 24
        },
        {
          "source": "MED",
          "id": "37991007",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "ACC neural ensemble dynamics are structured by strategy prevalence.",
          "authorString": "Proskurin M, Manakov M, Karpova A.",
          "journalAbbreviation": "Elife",
          "pubYear": 2023,
          "volume": "12",
          "pageInfo": "e84897",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "38027474",
          "citationType": "research-article; journal article",
          "title": "Human behavior in free search online shopping scenarios can be predicted from EEG activation using Hjorth parameters.",
          "authorString": "Horr NK, Mousavi B, Han K, Li A, Tang R.",
          "journalAbbreviation": "Front Neurosci",
          "pubYear": 2023,
          "volume": "17",
          "pageInfo": "1191213",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "37607820",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Theta Signal Transfer from Parietal to Prefrontal Cortex Ignites Conscious Awareness of Implicit Knowledge during Sequence Learning.",
          "authorString": "Lu Y, Guo X, Weng X, Jiang H, Yan H, Shen X, Feng Z, Zhao X, Li L, Zheng L, Liu Z, Men W, Gao JH.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2023,
          "volume": "43",
          "issue": "40",
          "pageInfo": "6760-6778",
          "citedByCount": 9
        },
        {
          "source": "PPR",
          "id": "PPR687144",
          "citationType": "preprint",
          "title": "Reconfigurations of cortical manifold structure during reward-based motor learning",
          "authorString": "Nick Q, Gale DJ, Areshenkoff C, De Brouwer A, Nashed J, Wammes J, Zhu T, Flanagan R, Smallwood J, Gallivan J.",
          "pubYear": 2023,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "37258534",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Task state representations in vmPFC mediate relevant and irrelevant value signals and their behavioral influence.",
          "authorString": "Moneta N, Garvert MM, Heekeren HR, Schuck NW.",
          "journalAbbreviation": "Nat Commun",
          "pubYear": 2023,
          "volume": "14",
          "issue": "1",
          "pageInfo": "3156",
          "citedByCount": 36
        },
        {
          "source": "PPR",
          "id": "PPR645860",
          "citationType": "preprint",
          "title": "Stochastic characterization of navigation strategies in an automated variant of the Barnes maze",
          "authorString": "Lee J, Jung D, Royer S.",
          "pubYear": 2023,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "36759690",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Seeing inferences: brain dynamics and oculomotor signatures of non-verbal deduction.",
          "authorString": "Mart\u00edn-Salguero A, Reverberi C, Solari A, Filippin L, Pallier C, Bonatti LL.",
          "journalAbbreviation": "Sci Rep",
          "pubYear": 2023,
          "volume": "13",
          "issue": "1",
          "pageInfo": "2341",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "36471828",
          "citationType": "research-article; journal article",
          "title": "Target-the-Two: a lab-in-the-field experiment on routinization.",
          "authorString": "Attanasi G, Egidi M, Manzoni E.",
          "journalAbbreviation": "J Evol Econ",
          "pubYear": 2023,
          "volume": "33",
          "issue": "1",
          "pageInfo": "1-33",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "36446707",
          "citationType": "research support, non-u.s. gov't; review; journal article",
          "title": "Goals, usefulness and abstraction in value-based choice.",
          "authorString": "De Martino B, Cortese A.",
          "journalAbbreviation": "Trends Cogn Sci",
          "pubYear": 2023,
          "volume": "27",
          "issue": "1",
          "pageInfo": "65-80",
          "citedByCount": 31
        },
        {
          "source": "PPR",
          "id": "PPR573706",
          "citationType": "preprint",
          "title": "ACC neural ensemble dynamics are structured by strategy prevalence",
          "authorString": "Proskurin M, Manakov M, Karpova AY.",
          "pubYear": 2022,
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "36160553",
          "citationType": "research-article; journal article",
          "title": "Using position rather than color at the traffic light - Covariation learning-based deviation from instructions in attention deficit/hyperactivity disorder.",
          "authorString": "Gaschler R, Ditsche-Klein BE, Kriechbaumer M, Blech C, Wenke D.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2022,
          "volume": "13",
          "pageInfo": "967467",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "36081853",
          "citationType": "research-article; journal article",
          "title": "Front and center: Maturational dysregulation of frontal lobe functional neuroanatomic connections in attention deficit hyperactivity disorder.",
          "authorString": "Leisman G, Melillo R.",
          "journalAbbreviation": "Front Neuroanat",
          "pubYear": 2022,
          "volume": "16",
          "pageInfo": "936025",
          "citedByCount": 18
        },
        {
          "source": "MED",
          "id": "36081729",
          "citationType": "research-article; journal article",
          "title": "Differences in the distribution of attention to trained procedure between finders and non-finders of the alternative better procedure.",
          "authorString": "Ninomiya Y, Terai H, Miwa K.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2022,
          "volume": "13",
          "pageInfo": "934029",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "35981525",
          "citationType": "research support, non-u.s. gov't; review; journal article",
          "title": "Functional neuroimaging in psychiatry and the case for failing better.",
          "authorString": "Nour MM, Liu Y, Dolan RJ.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2022,
          "volume": "110",
          "issue": "16",
          "pageInfo": "2524-2544",
          "citedByCount": 66
        },
        {
          "source": "MED",
          "id": "35906880",
          "citationType": "meta-analysis; research support, non-u.s. gov't; research-article; journal article",
          "title": "Uncovering neural distinctions and commodities between two creativity subsets: A meta-analysis of fMRI studies in divergent thinking and insight using activation likelihood estimation.",
          "authorString": "Kuang C, Chen J, Chen J, Shi Y, Huang H, Jiao B, Lin Q, Rao Y, Liu W, Zhu Y, Mo L, Ma L, Lin J.",
          "journalAbbreviation": "Hum Brain Mapp",
          "pubYear": 2022,
          "volume": "43",
          "issue": "16",
          "pageInfo": "4864-4885",
          "citedByCount": 16
        },
        {
          "source": "MED",
          "id": "35705077",
          "citationType": "research support, non-u.s. gov't; research-article; review; journal article",
          "title": "Medial and orbital frontal cortex in decision-making and flexible behavior.",
          "authorString": "Klein-Fl\u00fcgge MC, Bongioanni A, Rushworth MFS.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2022,
          "volume": "110",
          "issue": "17",
          "pageInfo": "2743-2770",
          "citedByCount": 166
        },
        {
          "source": "MED",
          "id": "35639714",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Spontaneous discovery of novel task solutions in children.",
          "authorString": "Schuck NW, Li AX, Wenke D, Ay-Bryson DS, Loewe AT, Gaschler R, Shing YL.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2022,
          "volume": "17",
          "issue": "5",
          "pageInfo": "e0266253",
          "citedByCount": 7
        },
        {
          "source": "MED",
          "id": "35560155",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Feature blindness: A challenge for understanding and modelling visual object recognition.",
          "authorString": "Malhotra G, Dujmovi\u0107 M, Bowers JS.",
          "journalAbbreviation": "PLoS Comput Biol",
          "pubYear": 2022,
          "volume": "18",
          "issue": "5",
          "pageInfo": "e1009572",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "35360631",
          "citationType": "discussion; journal article",
          "title": "Trade-Off vs. Common Factor-Differentiating Resource-Based Explanations From Their Alternative.",
          "authorString": "Naefgen C, Gaschler R.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2022,
          "volume": "13",
          "pageInfo": "774938",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "35260845",
          "citationType": "research support, non-u.s. gov't; review; journal article",
          "title": "Decoding cognition from spontaneous neural activity.",
          "authorString": "Liu Y, Nour MM, Schuck NW, Behrens TEJ, Dolan RJ.",
          "journalAbbreviation": "Nat Rev Neurosci",
          "pubYear": 2022,
          "volume": "23",
          "issue": "4",
          "pageInfo": "204-214",
          "citedByCount": 63
        },
        {
          "source": "MED",
          "id": "35153653",
          "citationType": "research-article; journal article",
          "title": "Effects of Spatial Speech Presentation on Listener Response Strategy for Talker-Identification.",
          "authorString": "Uhrig S, Perkis A, M\u00f6ller S, Svensson UP, Behne DM.",
          "journalAbbreviation": "Front Neurosci",
          "pubYear": 2021,
          "volume": "15",
          "pageInfo": "730744",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "34951662",
          "citationType": "research-article; journal article",
          "title": "The interplay between unexpected events and behavior in the development of explicit knowledge in implicit sequence learning.",
          "authorString": "Lustig C, Esser S, Haider H.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2022,
          "volume": "86",
          "issue": "7",
          "pageInfo": "2225-2238",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "34586489",
          "citationType": "research-article; review; journal article",
          "title": "What triggers explicit awareness in implicit sequence learning? Implications from theories of consciousness.",
          "authorString": "Esser S, Lustig C, Haider H.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2022,
          "volume": "86",
          "issue": "5",
          "pageInfo": "1442-1457",
          "citedByCount": 12
        },
        {
          "source": "MED",
          "id": "34389808",
          "citationType": "review-article; review; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "Computational models of adaptive behavior and prefrontal cortex.",
          "authorString": "Soltani A, Koechlin E.",
          "journalAbbreviation": "Neuropsychopharmacology",
          "pubYear": 2022,
          "volume": "47",
          "issue": "1",
          "pageInfo": "58-71",
          "citedByCount": 58
        },
        {
          "source": "MED",
          "id": "34371078",
          "citationType": "research support, non-u.s. gov't; review; journal article",
          "title": "Replay in minds and machines.",
          "authorString": "Wittkuhn L, Chien S, Hall-McMaster S, Schuck NW.",
          "journalAbbreviation": "Neurosci Biobehav Rev",
          "pubYear": 2021,
          "volume": "129",
          "pageInfo": "367-388",
          "citedByCount": 34
        },
        {
          "source": "MED",
          "id": "34330775",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Learning and Representation of Hierarchical Concepts in Hippocampus and Prefrontal Cortex.",
          "authorString": "Theves S, Neville DA, Fern\u00e1ndez G, Doeller CF.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2021,
          "volume": "41",
          "issue": "36",
          "pageInfo": "7675-7686",
          "citedByCount": 33
        },
        {
          "source": "MED",
          "id": "33852896",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The anterior cingulate cortex directs exploration of alternative strategies.",
          "authorString": "Tervo DGR, Kuleshova E, Manakov M, Proskurin M, Karlsson M, Lustig A, Behnam R, Karpova AY.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2021,
          "volume": "109",
          "issue": "11",
          "pageInfo": "1876-1887.e6",
          "citedByCount": 81
        },
        {
          "source": "MED",
          "id": "33752958",
          "citationType": "review; journal article",
          "title": "The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation.",
          "authorString": "Patai EZ, Spiers HJ.",
          "journalAbbreviation": "Trends Cogn Sci",
          "pubYear": 2021,
          "volume": "25",
          "issue": "6",
          "pageInfo": "520-533",
          "citedByCount": 103
        },
        {
          "source": "MED",
          "id": "33734733",
          "citationType": "research-article; review; journal article",
          "title": "What are grid-like responses doing in the orbitofrontal cortex?",
          "authorString": "Raithel CU, Gottfried JA.",
          "journalAbbreviation": "Behav Neurosci",
          "pubYear": 2021,
          "volume": "135",
          "issue": "2",
          "pageInfo": "218-225",
          "citedByCount": 6
        },
        {
          "source": "PPR",
          "id": "PPR299509",
          "citationType": "preprint",
          "title": "Representations of context and context-dependent values in vmPFC compete for guiding behavior",
          "authorString": "Moneta N, Garvert MM, Heekeren HR, Schuck NW.",
          "pubYear": 2021,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "33730510",
          "citationType": "research-article; review; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "Human Representation Learning.",
          "authorString": "Radulescu A, Shin YS, Niv Y.",
          "journalAbbreviation": "Annu Rev Neurosci",
          "pubYear": 2021,
          "volume": "44",
          "pageInfo": "253-273",
          "citedByCount": 46
        },
        {
          "source": "MED",
          "id": "33531416",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Coordinated Prefrontal State Transition Leads Extinction of Reward-Seeking Behaviors.",
          "authorString": "Russo E, Ma T, Spanagel R, Durstewitz D, Toutounji H, K\u00f6hr G.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2021,
          "volume": "41",
          "issue": "11",
          "pageInfo": "2406-2419",
          "citedByCount": 18
        },
        {
          "source": "MED",
          "id": "33104801",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Expecting social punishment facilitates control over a decision under uncertainty by recruiting medial prefrontal cortex.",
          "authorString": "Kim J, Jeong B.",
          "journalAbbreviation": "Soc Cogn Affect Neurosci",
          "pubYear": 2020,
          "volume": "15",
          "issue": "11",
          "pageInfo": "1260-1270",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "33060292",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Formation of global self-beliefs in the human brain.",
          "authorString": "Rouault M, Fleming SM.",
          "journalAbbreviation": "Proc Natl Acad Sci U S A",
          "pubYear": 2020,
          "volume": "117",
          "issue": "44",
          "pageInfo": "27268-27276",
          "citedByCount": 56
        },
        {
          "source": "MED",
          "id": "33020515",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Data segmentation based on the local intrinsic dimension.",
          "authorString": "Allegra M, Facco E, Denti F, Laio A, Mira A.",
          "journalAbbreviation": "Sci Rep",
          "pubYear": 2020,
          "volume": "10",
          "issue": "1",
          "pageInfo": "16449",
          "citedByCount": 11
        },
        {
          "source": "MED",
          "id": "34296121",
          "citationType": "research-article; journal article",
          "title": "Temporal Learning Among Prefrontal and Striatal Ensembles.",
          "authorString": "Emmons E, Tunes-Chiuffa G, Choi J, Bruce RA, Weber MA, Kim Y, Narayanan NS.",
          "journalAbbreviation": "Cereb Cortex Commun",
          "pubYear": 2020,
          "volume": "1",
          "issue": "1",
          "pageInfo": "tgaa058",
          "citedByCount": 29
        },
        {
          "source": "PPR",
          "id": "PPR167239",
          "citationType": "preprint",
          "title": "Anterior Cingulate Cortex Directs Exploration of Alternative Strategies",
          "authorString": "Tervo DGR, Kuleshova E, Manakov M, Proskurin M, Karlsson M, Lustig A, Behnam R, Karpova AY.",
          "pubYear": 2020,
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "32334091",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Brain network dynamics during spontaneous strategy shifts and incremental task optimization.",
          "authorString": "Allegra M, Seyed-Allaei S, Schuck NW, Amati D, Laio A, Reverberi C.",
          "journalAbbreviation": "Neuroimage",
          "pubYear": 2020,
          "volume": "217",
          "pageInfo": "116854",
          "citedByCount": 16
        },
        {
          "source": "MED",
          "id": "32255423",
          "citationType": "research support, non-u.s. gov't; research-article; research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "Preparation for upcoming attentional states in the hippocampus and medial prefrontal cortex.",
          "authorString": "G\u00fcnseli E, Aly M.",
          "journalAbbreviation": "Elife",
          "pubYear": 2020,
          "volume": "9",
          "pageInfo": "e53191",
          "citedByCount": 39
        },
        {
          "source": "MED",
          "id": "31504263",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Decoding Changes of Mind in Voluntary Action-Dynamics of Intentional Choice Representations.",
          "authorString": "L\u00f6ffler A, Haggard P, Bode S.",
          "journalAbbreviation": "Cereb Cortex",
          "pubYear": 2020,
          "volume": "30",
          "issue": "3",
          "pageInfo": "1199-1212",
          "citedByCount": 9
        },
        {
          "source": "PPR",
          "id": "PPR115144",
          "citationType": "preprint",
          "title": "Coordinated prefrontal state transition leads extinction of reward-seeking behaviors",
          "authorString": "Russo E, Ma T, Spanagel R, Durstewitz D, Toutounji H, K\u00f6hr G.",
          "pubYear": 2020,
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "31696233",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Cerebellar contribution to the cognitive alterations in SCA1: evidence from mouse models.",
          "authorString": "Asher M, Rosa JG, Rainwater O, Duvick L, Bennyworth M, Lai RY, CRC-SCA, Kuo SH, Cvetanovic M.",
          "journalAbbreviation": "Hum Mol Genet",
          "pubYear": 2020,
          "volume": "29",
          "issue": "1",
          "pageInfo": "117-131",
          "citedByCount": 34
        },
        {
          "source": "MED",
          "id": "31738167",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Neural representation of newly instructed rule identities during early implementation trials.",
          "authorString": "Ruge H, Sch\u00e4fer TA, Zwosta K, Mohr H, Wolfensteller U.",
          "journalAbbreviation": "Elife",
          "pubYear": 2019,
          "volume": "8",
          "pageInfo": "e48293",
          "citedByCount": 22
        },
        {
          "source": "MED",
          "id": "31712574",
          "citationType": "research-article; journal article",
          "title": "Early stimulation of the left posterior parietal cortex promotes representation change in problem solving.",
          "authorString": "Debarnot U, Schlatter S, Monteil J, Guillot A.",
          "journalAbbreviation": "Sci Rep",
          "pubYear": 2019,
          "volume": "9",
          "issue": "1",
          "pageInfo": "16523",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "31249030",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Sequential replay of nonspatial task states in the human hippocampus.",
          "authorString": "Schuck NW, Niv Y.",
          "journalAbbreviation": "Science",
          "pubYear": 2019,
          "volume": "364",
          "issue": "6447",
          "pageInfo": "eaaw5181",
          "citedByCount": 201
        },
        {
          "source": "MED",
          "id": "30988525",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "The macaque anterior cingulate cortex translates counterfactual choice value into actual behavioral change.",
          "authorString": "Fouragnan EF, Chau BKH, Folloni D, Kolling N, Verhagen L, Klein-Fl\u00fcgge M, Tankelevitch L, Papageorgiou GK, Aubry JF, Sallet J, Rushworth MFS.",
          "journalAbbreviation": "Nat Neurosci",
          "pubYear": 2019,
          "volume": "22",
          "issue": "5",
          "pageInfo": "797-808",
          "citedByCount": 194
        },
        {
          "source": "MED",
          "id": "30677046",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Incidental covariation learning leading to strategy change.",
          "authorString": "Gaschler R, Schuck NW, Reverberi C, Frensch PA, Wenke D.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2019,
          "volume": "14",
          "issue": "1",
          "pageInfo": "e0210597",
          "citedByCount": 11
        },
        {
          "source": "MED",
          "id": "30617208",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Beta and Theta Oscillations Differentially Support Free Versus Forced Control over Multiple-Target Search.",
          "authorString": "van Driel J, Ort E, Fahrenfort JJ, Olivers CNL.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2019,
          "volume": "39",
          "issue": "9",
          "pageInfo": "1733-1743",
          "citedByCount": 12
        },
        {
          "source": "MED",
          "id": "30523066",
          "citationType": "research-article; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "Dissociable Forms of Uncertainty-Driven Representational Change Across the Human Brain.",
          "authorString": "Nassar MR, McGuire JT, Ritz H, Kable JW.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2019,
          "volume": "39",
          "issue": "9",
          "pageInfo": "1688-1698",
          "citedByCount": 63
        },
        {
          "source": "MED",
          "id": "30358821",
          "citationType": "research support, n.i.h., intramural; research support, non-u.s. gov't; research-article; journal article",
          "title": "Cognitive control involves theta power within trials and beta power across trials in the prefrontal-subthalamic network.",
          "authorString": "Zavala B, Jang A, Trotta M, Lungu CI, Brown P, Zaghloul KA.",
          "journalAbbreviation": "Brain",
          "pubYear": 2018,
          "volume": "141",
          "issue": "12",
          "pageInfo": "3361-3376",
          "citedByCount": 115
        },
        {
          "source": "PPR",
          "id": "PPR63274",
          "citationType": "preprint",
          "title": "Brain network dynamics during spontaneous strategy shifts and incremental task optimization",
          "authorString": "Allegra M, Seyed-Allaei S, Schuck NW, Amati D, Laio A, Reverberi C.",
          "pubYear": 2018,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "30439509",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Differentiating guilt and shame in an interpersonal context with univariate activation and multivariate pattern analyses.",
          "authorString": "Zhu R, Feng C, Zhang S, Mai X, Liu C.",
          "journalAbbreviation": "Neuroimage",
          "pubYear": 2019,
          "volume": "186",
          "pageInfo": "476-486",
          "citedByCount": 45
        },
        {
          "source": "MED",
          "id": "30165082",
          "citationType": "meta-analysis; research support, non-u.s. gov't; journal article",
          "title": "Tracking the neurodynamics of insight: A meta-analysis of neuroimaging studies.",
          "authorString": "Shen W, Tong Y, Li F, Yuan Y, Hommel B, Liu C, Luo J.",
          "journalAbbreviation": "Biol Psychol",
          "pubYear": 2018,
          "volume": "138",
          "pageInfo": "189-198",
          "citedByCount": 38
        },
        {
          "source": "MED",
          "id": "30123818",
          "citationType": "review-article; review; journal article",
          "title": "State-change decisions and dorsomedial prefrontal cortex: the importance of time.",
          "authorString": "Kolling N, O'Reilly JX.",
          "journalAbbreviation": "Curr Opin Behav Sci",
          "pubYear": 2018,
          "volume": "22",
          "pageInfo": "152-160",
          "citedByCount": 20
        },
        {
          "source": "PPR",
          "id": "PPR7350",
          "citationType": "preprint",
          "title": "Dissociable forms of uncertainty-driven representational change across the human brain",
          "authorString": "Nassar MR, McGuire JT, Ritz H, Kable J.",
          "pubYear": 2018,
          "citedByCount": 0
        },
        {
          "source": "PPR",
          "id": "PPR9943",
          "citationType": "preprint",
          "title": "The macaque anterior cingulate cortex translates counterfactual choice value into actual behavioral change",
          "authorString": "Fouragnan E, Chau B, Folloni D, Kolling N, Verhagen L, Klein-Fl\u00fcgge M, Tankelevitch L, Papageorgiou G, Aubry J, Sallet J, Rushworth M.",
          "pubYear": 2018,
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "29866834",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Human midcingulate cortex encodes distributed representations of task progress.",
          "authorString": "Holroyd CB, Ribas-Fernandes JJF, Shahnazian D, Silvetti M, Verguts T.",
          "journalAbbreviation": "Proc Natl Acad Sci U S A",
          "pubYear": 2018,
          "volume": "115",
          "issue": "25",
          "pageInfo": "6398-6403",
          "citedByCount": 43
        },
        {
          "source": "MED",
          "id": "29753107",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The neural basis of free language choice in bilingual speakers: Disentangling language choice and language execution.",
          "authorString": "Reverberi C, Kuhlen AK, Seyed-Allaei S, Greulich RS, Costa A, Abutalebi J, Haynes JD.",
          "journalAbbreviation": "Neuroimage",
          "pubYear": 2018,
          "volume": "177",
          "pageInfo": "108-116",
          "citedByCount": 22
        },
        {
          "source": "MED",
          "id": "29650697",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Cell-Type-Specific Contributions of Medial Prefrontal Neurons to Flexible Behaviors.",
          "authorString": "Nakayama H, Iba\u00f1ez-Tallon I, Heintz N.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2018,
          "volume": "38",
          "issue": "19",
          "pageInfo": "4490-4504",
          "citedByCount": 72
        },
        {
          "source": "MED",
          "id": "28444633",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Distributed representations of action sequences in anterior cingulate cortex: A recurrent neural network approach.",
          "authorString": "Shahnazian D, Holroyd CB.",
          "journalAbbreviation": "Psychon Bull Rev",
          "pubYear": 2018,
          "volume": "25",
          "issue": "1",
          "pageInfo": "302-321",
          "citedByCount": 28
        },
        {
          "source": "MED",
          "id": "29374138",
          "citationType": "research support, non-u.s. gov't; research-article; review; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "A Shared Vision for Machine Learning in Neuroscience.",
          "authorString": "Vu MT, Adal\u0131 T, Ba D, Buzs\u00e1ki G, Carlson D, Heller K, Liston C, Rudin C, Sohal VS, Widge AS, Mayberg HS, Sapiro G, Dzirasa K.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2018,
          "volume": "38",
          "issue": "7",
          "pageInfo": "1601-1607",
          "citedByCount": 109
        },
        {
          "source": "MED",
          "id": "29247192",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Exploring Feature Dimensions to Learn a New Policy in an Uninformed Reinforcement Learning Task.",
          "authorString": "Choung OH, Lee SW, Jeong Y.",
          "journalAbbreviation": "Sci Rep",
          "pubYear": 2017,
          "volume": "7",
          "issue": "1",
          "pageInfo": "17676",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "29229706",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Causal Evidence for Learning-Dependent Frontal Lobe Contributions to Cognitive Control.",
          "authorString": "Muhle-Karbe PS, Jiang J, Egner T.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2018,
          "volume": "38",
          "issue": "4",
          "pageInfo": "962-973",
          "citedByCount": 34
        },
        {
          "source": "MED",
          "id": "29189018",
          "citationType": "research-article; journal article",
          "title": "The application of a rodent-based Morris water maze (MWM) protocol to an investigation of age-related differences in human spatial learning.",
          "authorString": "Zhong JY, Magnusson KR, Swarts ME, Clendinen CA, Reynolds NC, Moffat SD.",
          "journalAbbreviation": "Behav Neurosci",
          "pubYear": 2017,
          "volume": "131",
          "issue": "6",
          "pageInfo": "470-482",
          "citedByCount": 44
        },
        {
          "source": "PPR",
          "id": "PPR9821",
          "citationType": "preprint",
          "title": "A State Representation for Reinforcement Learning and Decision-Making in the Orbitofrontal Cortex",
          "authorString": "Schuck NW, Wilson R, Niv Y.",
          "pubYear": 2017,
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "28966147",
          "citationType": "research support, non-u.s. gov't; review-article; review; journal article",
          "title": "Understanding psychiatric disorder by capturing ecologically relevant features of learning and decision-making.",
          "authorString": "Scholl J, Klein-Fl\u00fcgge M.",
          "journalAbbreviation": "Behav Brain Res",
          "pubYear": 2018,
          "volume": "355",
          "pageInfo": "56-75",
          "citedByCount": 48
        },
        {
          "source": "MED",
          "id": "28867996",
          "citationType": "research-article; journal article",
          "title": "Neural Signatures of Rational and Heuristic Choice Strategies: A Single Trial ERP Analysis.",
          "authorString": "Wichary S, Magnuski M, Oleksy T, Brzezicka A.",
          "journalAbbreviation": "Front Hum Neurosci",
          "pubYear": 2017,
          "volume": "11",
          "pageInfo": "401",
          "citedByCount": 21
        },
        {
          "source": "MED",
          "id": "28729442",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Adaptive Encoding of Outcome Prediction by Prefrontal Cortex Ensembles Supports Behavioral Flexibility.",
          "authorString": "Del Arco A, Park J, Wood J, Kim Y, Moghaddam B.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2017,
          "volume": "37",
          "issue": "35",
          "pageInfo": "8363-8373",
          "citedByCount": 58
        },
        {
          "source": "MED",
          "id": "28365032",
          "citationType": "research support, non-u.s. gov't; journal article; research support, n.i.h., extramural",
          "title": "The Role of Mental Maps in Decision-Making.",
          "authorString": "Kaplan R, Schuck NW, Doeller CF.",
          "journalAbbreviation": "Trends Neurosci",
          "pubYear": 2017,
          "volume": "40",
          "issue": "5",
          "pageInfo": "256-259",
          "citedByCount": 59
        },
        {
          "source": "PPR",
          "id": "PPR25137",
          "citationType": "preprint",
          "title": "Intrinsic Hippocampal-Caudate Interaction Correlates with Human Navigation",
          "authorString": "Kong X, Pu Y, Wang X, Xu S, Hao X, Zhen Z, Liu J.",
          "pubYear": 2017,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "28253076",
          "citationType": "journal article",
          "title": "Major Thought Restructuring: The Roles of Different Prefrontal Cortical Regions.",
          "authorString": "Seyed-Allaei S, Avanaki ZN, Bahrami B, Shallice T.",
          "journalAbbreviation": "J Cogn Neurosci",
          "pubYear": 2017,
          "volume": "29",
          "issue": "7",
          "pageInfo": "1147-1161",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "28081125",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "The Neural Representation of Prospective Choice during Spatial Planning and Decisions.",
          "authorString": "Kaplan R, King J, Koster R, Penny WD, Burgess N, Friston KJ.",
          "journalAbbreviation": "PLoS Biol",
          "pubYear": 2017,
          "volume": "15",
          "issue": "1",
          "pageInfo": "e1002588",
          "citedByCount": 60
        },
        {
          "source": "MED",
          "id": "27879036",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "fMRI single trial discovery of spatio-temporal brain activity patterns.",
          "authorString": "Allegra M, Seyed-Allaei S, Pizzagalli F, Baftizadeh F, Maieron M, Reverberi C, Laio A, Amati D.",
          "journalAbbreviation": "Hum Brain Mapp",
          "pubYear": 2017,
          "volume": "38",
          "issue": "3",
          "pageInfo": "1421-1437",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "27899908",
          "citationType": "article-commentary; comment; journal article",
          "title": "Commentary: Incubation and Intuition in Creative Problem Solving.",
          "authorString": "Yuan Y, Shen W.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "1807",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "27653278",
          "citationType": "research-article; journal article",
          "title": "Representational changes of latent strategies in rat medial prefrontal cortex precede changes in behaviour.",
          "authorString": "Powell NJ, Redish AD.",
          "journalAbbreviation": "Nat Commun",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "12830",
          "citedByCount": 79
        },
        {
          "source": "MED",
          "id": "27657452",
          "citationType": "research-article; journal article",
          "title": "Human Orbitofrontal Cortex Represents a Cognitive Map of State Space.",
          "authorString": "Schuck NW, Cai MB, Wilson RC, Niv Y.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2016,
          "volume": "91",
          "issue": "6",
          "pageInfo": "1402-1412",
          "citedByCount": 492
        },
        {
          "source": "MED",
          "id": "27477632",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Predictive decision making driven by multiple time-linked reward representations in the anterior cingulate cortex.",
          "authorString": "Wittmann MK, Kolling N, Akaishi R, Chau BK, Brown JW, Nelissen N, Rushworth MF.",
          "journalAbbreviation": "Nat Commun",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "12327",
          "citedByCount": 121
        },
        {
          "source": "MED",
          "id": "26834581",
          "citationType": "review-article; review; journal article",
          "title": "The Monitoring and Control of Task Sequences in Human and Non-Human Primates.",
          "authorString": "Desrochers TM, Burk DC, Badre D, Sheinberg DL.",
          "journalAbbreviation": "Front Syst Neurosci",
          "pubYear": 2015,
          "volume": "9",
          "pageInfo": "185",
          "citedByCount": 27
        },
        {
          "source": "MED",
          "id": "26687618",
          "citationType": "review; journal article",
          "title": "Prefrontal executive function and adaptive behavior in complex environments.",
          "authorString": "Koechlin E.",
          "journalAbbreviation": "Curr Opin Neurobiol",
          "pubYear": 2016,
          "volume": "37",
          "pageInfo": "1-6",
          "citedByCount": 102
        },
        {
          "source": "MED",
          "id": "26321932",
          "citationType": "research-article; journal article",
          "title": "Improving memory following prefrontal cortex damage with the PQRST method.",
          "authorString": "Ciaramelli E, Neri F, Marini L, Braghittoni D.",
          "journalAbbreviation": "Front Behav Neurosci",
          "pubYear": 2015,
          "volume": "9",
          "pageInfo": "211",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "26034188",
          "citationType": "journal article",
          "title": "Kaleidoscope.",
          "authorString": "Tracy DK, Joyce DW, Shergill SS.",
          "journalAbbreviation": "Br J Psychiatry",
          "pubYear": 2015,
          "volume": "206",
          "issue": "6",
          "pageInfo": "528-529",
          "citedByCount": 0
        }
      ],
      "errors": [],
      "ncbi": {
        "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&linkname=pubmed_pubmed_citedin&id=25819613&retmode=json",
        "response_sha256": "0c90842bb1d3ee53835caf2872551ebe374e2c45e80111a1d53f77b78db94c3b",
        "linksets": [
          {
            "dbfrom": "pubmed",
            "ids": [
              "25819613"
            ],
            "linksetdbs": [
              {
                "dbto": "pubmed",
                "linkname": "pubmed_pubmed_citedin",
                "links": [
                  "42215782",
                  "41650240",
                  "41308940",
                  "40882180",
                  "40569931",
                  "39929102",
                  "39882026",
                  "39847600",
                  "39715747",
                  "39585903",
                  "39557563",
                  "39432516",
                  "39314386",
                  "39134298",
                  "38916598",
                  "38899521",
                  "38447579",
                  "38405946",
                  "38027474",
                  "37991007",
                  "37607820",
                  "37258534",
                  "36759690",
                  "36471828",
                  "36160553",
                  "36081853",
                  "36081729",
                  "35906880",
                  "35705077",
                  "35639714",
                  "35560155",
                  "35360631",
                  "35260845",
                  "35153653",
                  "34951662",
                  "34586489",
                  "34389808",
                  "34330775",
                  "34296121",
                  "33734733",
                  "33730510",
                  "33531416",
                  "33060292",
                  "32255423",
                  "31738167",
                  "31712574",
                  "31696233",
                  "31249030",
                  "30677046",
                  "30617208",
                  "30523066",
                  "30358821",
                  "30123818",
                  "29866834",
                  "29650697",
                  "29374138",
                  "29247192",
                  "29229706",
                  "29189018",
                  "28966147",
                  "28867996",
                  "28729442",
                  "28444633",
                  "28081125",
                  "27899908",
                  "27879036",
                  "27657452",
                  "27653278",
                  "27477632",
                  "26834581",
                  "26321932"
                ]
              }
            ]
          }
        ],
        "error": null
      }
    },
    "PowellRedish2016": {
      "pmid": "27653278",
      "europe_pmc_queries": [
        {
          "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/MED/27653278/citations?format=json&page=1&pageSize=1000",
          "response_sha256": "df84a65072d8b0565226ed86766068253613d8edaffc4d65b64c9ed8c11c0b66",
          "hitCount": 76
        }
      ],
      "records": [
        {
          "source": "PPR",
          "id": "PPR1285343",
          "citationType": "preprint",
          "title": "Learning stabilizes temporal activity but not neuronal selectivity in prefrontal cortex",
          "authorString": "Huang(\u9ec4\u5b87\u9633) Y, Mehrke LS, Bernklau TW, Busse L, Jacob SN.",
          "pubYear": 2026,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "42421588",
          "citationType": "review; journal article",
          "title": "The vicarious nature of hippocampal theta sequences.",
          "authorString": "Damphousse CC, Gagliardi CM, Peterson JG, Feng C, Schmidt B, Mugan U, Redish AD.",
          "journalAbbreviation": "Philos Trans R Soc Lond B Biol Sci",
          "pubYear": 2026,
          "volume": "381",
          "issue": "1954",
          "pageInfo": "20250242",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "42092148",
          "citationType": "journal article",
          "title": "Prefrontal to ventral tegmental area dynamics drive contingency degradation.",
          "authorString": "Hjort MM, Garrett ZQ, Gordon AG, Ancell E, Trzeciak M, Lu PY, Bruchas MR, Witten DM, Steinmetz NA, Stuber GD.",
          "journalAbbreviation": "Nature",
          "pubYear": 2026,
          "volume": "655",
          "issue": "8121",
          "pageInfo": "174-182",
          "citedByCount": 0
        },
        {
          "source": "PPR",
          "id": "PPR1181633",
          "citationType": "preprint",
          "title": "Shining Light into Adolescent HIV Neuroplasticity: A Study of the Prefrontal Cortex Using Functional Near Infrared Spectrometry",
          "authorString": "Zondo S, Cockcroft K, da Silva Ferreira Barreto C, Ferreira Correia A.",
          "pubYear": 2026,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "41620492",
          "citationType": "research-article; journal article",
          "title": "Uncertainty and reward histories have distinct effects on decisions after wins and losses.",
          "authorString": "Kalhan S, Magnard R, Zhang Z, Cheng Y, Janak PH.",
          "journalAbbreviation": "Sci Rep",
          "pubYear": 2026,
          "volume": "16",
          "issue": "1",
          "pageInfo": "6795",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "41525870",
          "citationType": "journal article",
          "title": "The mPFC-PAG in defensive coping: A correlational but not causal role in shifting strategy.",
          "authorString": "Li M, Wang Q, Li X, Wu Z, Li W, Ning Y, Zhang J, Jiang X, Wang K, Jing L.",
          "journalAbbreviation": "Behav Brain Res",
          "pubYear": 2026,
          "volume": "502",
          "pageInfo": "116037",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "40097186",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Ventral Tegmental Area Dopamine Neural Activity Switches Simultaneously with Rule Representations in the Medial Prefrontal Cortex and Hippocampus.",
          "authorString": "Ding M, Tomsick PL, Young RA, Jadhav SP.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2025,
          "volume": "45",
          "issue": "37",
          "pageInfo": "e1670242025",
          "citedByCount": 10
        },
        {
          "source": "MED",
          "id": "40562795",
          "citationType": "research-article; journal article",
          "title": "Abstract rule learning promotes cognitive flexibility in complex environments across species.",
          "authorString": "B\u00e4hner F, Popov T, Boehme N, Hermann S, Merten T, Zingone H, Koppe G, Meyer-Lindenberg A, Toutounji H, Durstewitz D.",
          "journalAbbreviation": "Nat Commun",
          "pubYear": 2025,
          "volume": "16",
          "issue": "1",
          "pageInfo": "5396",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "40097184",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Neural Correlates of Opioid-Induced Risk-Taking Behavior in the Prelimbic Prefrontal Cortex.",
          "authorString": "Quave CB, Vasquez AM, Aquino-Miranda G, Mar\u00edn M, Bora EP, Chidomere CL, Zhang XO, Engelke DS, Do-Monte FH.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2025,
          "volume": "45",
          "issue": "19",
          "pageInfo": "e2422242025",
          "citedByCount": 2
        },
        {
          "source": "PPR",
          "id": "PPR993990",
          "citationType": "preprint",
          "title": "Recasting adaptation as strategy inference",
          "authorString": "Beaumont S, Khamassi M, Domenech P.",
          "pubYear": 2025,
          "citedByCount": 2
        },
        {
          "source": "PPR",
          "id": "PPR989094",
          "citationType": "preprint",
          "title": "Adaptive learning via surprise gated attractor switching",
          "authorString": "He Q, Scott DN, Frank MJ, Calderon CB, Nassar MR.",
          "pubYear": 2025,
          "citedByCount": 0
        },
        {
          "source": "PPR",
          "id": "PPR981388",
          "citationType": "preprint",
          "title": "Rhythmic modulation of dorsal hippocampus across distinct behavioral timescales during spatial set-shifting",
          "authorString": "Bottoms M, Miles JT, Mizumori SJ.",
          "pubYear": 2025,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "39938512",
          "citationType": "research-article; journal article",
          "title": "Transformations in prefrontal ensemble activity underlying rapid threat avoidance learning.",
          "authorString": "Gabriel CJ, Gupta TA, S\u00e1nchez-Fuentes A, Zeidler Z, Wilke SA, DeNardo LA.",
          "journalAbbreviation": "Curr Biol",
          "pubYear": 2025,
          "volume": "35",
          "issue": "5",
          "pageInfo": "1128-1136.e4",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "39825081",
          "citationType": "research-article; journal article",
          "title": "Prefrontal cortex synchronization with the hippocampus and parietal cortex is strategy-dependent during spatial learning.",
          "authorString": "Garc\u00eda F, Torres MJ, Chacana-V\u00e9liz L, Espinosa N, El-Deredy W, Fuentealba P, Negr\u00f3n-Oyarzo I.",
          "journalAbbreviation": "Commun Biol",
          "pubYear": 2025,
          "volume": "8",
          "issue": "1",
          "pageInfo": "79",
          "citedByCount": 14
        },
        {
          "source": "MED",
          "id": "42222131",
          "citationType": "research-article; journal article",
          "title": "Shining Light into Adolescent HIV Neuroplasticity: A Study of the Prefrontal Cortex Using Functional Near Infrared Spectrometry.",
          "authorString": "Zondo S, Cockcroft K, da Silva Ferreira Barreto C, Ferreira Correia A.",
          "journalAbbreviation": "F1000Res",
          "pubYear": 2025,
          "volume": "14",
          "pageInfo": "1000",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "39715747",
          "citationType": "research-article; journal article",
          "title": "Broadscale dampening of uncertainty adjustment in the aging brain.",
          "authorString": "Kosciessa JQ, Mayr U, Lindenberger U, Garrett DD.",
          "journalAbbreviation": "Nat Commun",
          "pubYear": 2024,
          "volume": "15",
          "issue": "1",
          "pageInfo": "10717",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "39696528",
          "citationType": "research-article; journal article",
          "title": "Characterization of neuronal oscillations in the prelimbic cortex, nucleus accumbens and CA1 hippocampus during object retrieval task in rats predisposed to early life stress.",
          "authorString": "Sharma SS, Sasidharan A, Yoganarasimha D, Laxmi TR.",
          "journalAbbreviation": "Behav Brain Funct",
          "pubYear": 2024,
          "volume": "20",
          "issue": "1",
          "pageInfo": "34",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "39557563",
          "citationType": "research-article; journal article",
          "title": "Impulsive Choices Emerge When the Anterior Cingulate Cortex Fails to Encode Deliberative Strategies.",
          "authorString": "White SM, Morningstar MD, De Falco E, Linsenbardt DN, Ma B, Parks MA, Czachowski CL, Lapish CC.",
          "journalAbbreviation": "eNeuro",
          "pubYear": 2024,
          "volume": "11",
          "issue": "11",
          "pageInfo": "ENEURO.0379-24.2024",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "39313320",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "A Prefrontal\u2192Periaqueductal Gray Pathway Differentially Engages Autonomic, Hormonal, and Behavioral Features of the Stress-Coping Response.",
          "authorString": "Skog TD, Johnson SB, Hinz DC, Lingg RT, Schulz EN, Luna JT, Beltz TG, Romig-Martin SA, Gantz SC, Xue B, Johnson AK, Radley JJ.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2024,
          "volume": "44",
          "issue": "46",
          "pageInfo": "e0844242024",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "39476843",
          "citationType": "research-article; journal article",
          "title": "Environmental complexity modulates information processing and the balance between decision-making systems.",
          "authorString": "Mugan U, Hoffman SL, Redish AD.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2024,
          "volume": "112",
          "issue": "24",
          "pageInfo": "4096-4114.e10",
          "citedByCount": 13
        },
        {
          "source": "MED",
          "id": "39235662",
          "citationType": "review-article; review; journal article",
          "title": "Fiber photometry in neuroscience research: principles, applications, and future directions.",
          "authorString": "Kielbinski M, Bernacka J.",
          "journalAbbreviation": "Pharmacol Rep",
          "pubYear": 2024,
          "volume": "76",
          "issue": "6",
          "pageInfo": "1242-1255",
          "citedByCount": 15
        },
        {
          "source": "MED",
          "id": "39161082",
          "citationType": "journal article",
          "title": "Rat anterior cingulate neurons responsive to rule or strategy changes are modulated by the hippocampal theta rhythm and sharp-wave ripples.",
          "authorString": "Khamassi M, Peyrache A, Benchenane K, Hopkins DA, Lebas N, Douchamps V, Droulez J, Battaglia FP, Wiener SI.",
          "journalAbbreviation": "Eur J Neurosci",
          "pubYear": 2024,
          "volume": "60",
          "issue": "6",
          "pageInfo": "5300-5327",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "39038921",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Flexible decision-making is related to strategy learning, vicarious trial and error, and medial prefrontal rhythms during spatial set-shifting.",
          "authorString": "Miles JT, Mullins GL, Mizumori SJY.",
          "journalAbbreviation": "Learn Mem",
          "pubYear": 2024,
          "volume": "31",
          "issue": "7",
          "pageInfo": "a053911",
          "citedByCount": 11
        },
        {
          "source": "PPR",
          "id": "PPR850162",
          "citationType": "preprint",
          "title": "A novel dopaminergic critic signal triggered by erroneous strategy choices in mice training in operant tasks",
          "authorString": "Matsumoto J, Oberto VJ, Pompili MN, Todorova R, Papaleo F, Nishijo H, Venance L, Vandecasteele M, Wiener SI.",
          "pubYear": 2024,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "38638163",
          "citationType": "review-article; review; journal article",
          "title": "Large-scale coupling of prefrontal activity patterns as a mechanism for cognitive control in health and disease: evidence from rodent models.",
          "authorString": "Negr\u00f3n-Oyarzo I, Dib T, Chacana-V\u00e9liz L, L\u00f3pez-Quilodr\u00e1n N, Urrutia-Pi\u00f1ones J.",
          "journalAbbreviation": "Front Neural Circuits",
          "pubYear": 2024,
          "volume": "18",
          "pageInfo": "1286111",
          "citedByCount": 7
        },
        {
          "source": "MED",
          "id": "38426402",
          "citationType": "research-article; journal article",
          "title": "Tracking subjects' strategies in behavioural choice experiments at trial resolution.",
          "authorString": "Maggi S, Hock RM, O'Neill M, Buckley M, Moran PM, Bast T, Sami M, Humphries MD.",
          "journalAbbreviation": "Elife",
          "pubYear": 2024,
          "volume": "13",
          "pageInfo": "e86491",
          "citedByCount": 14
        },
        {
          "source": "PPR",
          "id": "PPR801503",
          "citationType": "preprint",
          "title": "Neural signatures of opioid-induced risk-taking behavior in the prelimbic prefrontal cortex",
          "authorString": "Quave CB, Vasquez AM, Aquino-Miranda G, Mar\u00edn M, Bora EP, Chidomere CL, Zhang XO, Engelke DS, Do-Monte FH.",
          "pubYear": 2024,
          "citedByCount": 0
        },
        {
          "source": "PPR",
          "id": "PPR792617",
          "citationType": "preprint",
          "title": "Rat anterior cingulate neurons responsive to rule or strategy changes are modulated by the hippocampal theta rhythm and sharp-wave ripples",
          "authorString": "Khamassi M, Peyrache A, Benchenane K, Hopkins D, Lebas N, Douchamps V, Droulez J, Battaglia F, Wiener S.",
          "pubYear": 2024,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "38050098",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Hippocampal Engrams Generate Variable Behavioral Responses and Brain-Wide Network States.",
          "authorString": "Dorst KE, Senne RA, Diep AH, de Boer AR, Suthard RL, Leblanc H, Ruesch EA, Pyo AY, Skelton S, Carstensen LC, Malmberg S, McKissick OP, Bladon JH, Ramirez S.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2024,
          "volume": "44",
          "issue": "2",
          "pageInfo": "e0340232023",
          "citedByCount": 17
        },
        {
          "source": "PPR",
          "id": "PPR773580",
          "citationType": "preprint",
          "title": "Flexible decision-making is related to strategy learning, vicarious trial and error, and medial prefrontal rhythms during spatial set-shifting",
          "authorString": "Miles JT, Mullins GL, Mizumori SJY.",
          "pubYear": 2023,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "37991007",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "ACC neural ensemble dynamics are structured by strategy prevalence.",
          "authorString": "Proskurin M, Manakov M, Karpova A.",
          "journalAbbreviation": "Elife",
          "pubYear": 2023,
          "volume": "12",
          "pageInfo": "e84897",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "37086556",
          "citationType": "research-article; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "A computational model of prefrontal and striatal interactions in perceptual category learning.",
          "authorString": "H\u00e9lie S, Lim LX, Adkins MJ, Redick TS.",
          "journalAbbreviation": "Brain Cogn",
          "pubYear": 2023,
          "volume": "168",
          "pageInfo": "105970",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "36822467",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Optogenetic disruption of the prelimbic cortex alters long-term decision strategy but not valuation on a spatial delay discounting task.",
          "authorString": "McLaughlin AE, Redish AD.",
          "journalAbbreviation": "Neurobiol Learn Mem",
          "pubYear": 2023,
          "volume": "200",
          "pageInfo": "107734",
          "citedByCount": 14
        },
        {
          "source": "MED",
          "id": "36652289",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Differential processing of decision information in subregions of rodent medial prefrontal cortex.",
          "authorString": "Diehl GW, Redish AD.",
          "journalAbbreviation": "Elife",
          "pubYear": 2023,
          "volume": "12",
          "pageInfo": "e82833",
          "citedByCount": 37
        },
        {
          "source": "PPR",
          "id": "PPR573706",
          "citationType": "preprint",
          "title": "ACC neural ensemble dynamics are structured by strategy prevalence",
          "authorString": "Proskurin M, Manakov M, Karpova AY.",
          "pubYear": 2022,
          "citedByCount": 1
        },
        {
          "source": "PPR",
          "id": "PPR571902",
          "citationType": "preprint",
          "title": "Species-conserved mechanisms of abstract rule learning promote cognitive flexibility in complex environments",
          "authorString": "B\u00e4hner F, Popov T, Boehme N, Hermann S, Merten T, Zingone H, Koppe G, Meyer-Lindenberg A, Toutounji H, Durstewitz D.",
          "pubYear": 2022,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "36306326",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Activity in a prefrontal-periaqueductal gray circuit overcomes behavioral and endocrine features of the passive coping stress response.",
          "authorString": "Johnson SB, Lingg RT, Skog TD, Hinz DC, Romig-Martin SA, Viau V, Narayanan NS, Radley JJ.",
          "journalAbbreviation": "Proc Natl Acad Sci U S A",
          "pubYear": 2022,
          "volume": "119",
          "issue": "44",
          "pageInfo": "e2210783119",
          "citedByCount": 30
        },
        {
          "source": "MED",
          "id": "36311857",
          "citationType": "brief-report; journal article",
          "title": "Dorsomedial prefrontal cortex activation disrupts Pavlovian incentive motivation.",
          "authorString": "Halbout B, Hutson C, Wassum KM, Ostlund SB.",
          "journalAbbreviation": "Front Behav Neurosci",
          "pubYear": 2022,
          "volume": "16",
          "pageInfo": "999320",
          "citedByCount": 6
        },
        {
          "source": "PPR",
          "id": "PPR538172",
          "citationType": "preprint",
          "title": "Tracking subjects\u2019 strategies in behavioural choice experiments at trial resolution",
          "authorString": "Maggi S, Hock RM, O\u2019Neill M, Buckley MJ, Moran PM, Bast T, Sami M, Humphries MD.",
          "pubYear": 2022,
          "citedByCount": 3
        },
        {
          "source": "PPR",
          "id": "PPR528836",
          "citationType": "preprint",
          "title": "Differential processing of decision information in subregions of rodent medial prefrontal cortex",
          "authorString": "Diehl GW, Redish AD.",
          "pubYear": 2022,
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "35422440",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Activity Subspaces in Medial Prefrontal Cortex Distinguish States of the World.",
          "authorString": "Maggi S, Humphries MD.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2022,
          "volume": "42",
          "issue": "20",
          "pageInfo": "4131-4146",
          "citedByCount": 16
        },
        {
          "source": "MED",
          "id": "34957854",
          "citationType": "review-article; journal article; research support, n.i.h., extramural",
          "title": "Computational validity: using computation to translate behaviours across species.",
          "authorString": "Redish AD, Kepecs A, Anderson LM, Calvin OL, Grissom NM, Haynos AF, Heilbronner SR, Herman AB, Jacob S, Ma S, Vilares I, Vinogradov S, Walters CJ, Widge AS, Zick JL, Zilverstand A.",
          "journalAbbreviation": "Philos Trans R Soc Lond B Biol Sci",
          "pubYear": 2022,
          "volume": "377",
          "issue": "1844",
          "pageInfo": "20200525",
          "citedByCount": 48
        },
        {
          "source": "MED",
          "id": "34035138",
          "citationType": "research-article; journal article",
          "title": "Prefrontal Cortical Neurons Are Selective for Non-Local Hippocampal Representations during Replay and Behavior.",
          "authorString": "Berners-Lee A, Wu X, Foster DJ.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2021,
          "volume": "41",
          "issue": "27",
          "pageInfo": "5894-5908",
          "citedByCount": 29
        },
        {
          "source": "MED",
          "id": "34184635",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Specialized coding patterns among dorsomedial prefrontal neuronal ensembles predict conditioned reward seeking.",
          "authorString": "Grant RI, Doncheck EM, Vollmer KM, Winston KT, Romanova EV, Siegler PN, Holman H, Bowen CW, Otis JM.",
          "journalAbbreviation": "Elife",
          "pubYear": 2021,
          "volume": "10",
          "pageInfo": "e65764",
          "citedByCount": 35
        },
        {
          "source": "MED",
          "id": "34077741",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Rapid suppression and sustained activation of distinct cortical regions for a delayed sensory-triggered motor response.",
          "authorString": "Esmaeili V, Tamura K, Muscinelli SP, Modirshanechi A, Boscaglia M, Lee AB, Oryshchuk A, Foustoukos G, Liu Y, Crochet S, Gerstner W, Petersen CCH.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2021,
          "volume": "109",
          "issue": "13",
          "pageInfo": "2183-2201.e9",
          "citedByCount": 94
        },
        {
          "source": "MED",
          "id": "33991700",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Subjective value, not a gridlike code, describes neural activity in ventromedial prefrontal cortex during value-based decision-making.",
          "authorString": "Lee S, Yu LQ, Lerman C, Kable JW.",
          "journalAbbreviation": "Neuroimage",
          "pubYear": 2021,
          "volume": "237",
          "pageInfo": "118159",
          "citedByCount": 19
        },
        {
          "source": "MED",
          "id": "33852896",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The anterior cingulate cortex directs exploration of alternative strategies.",
          "authorString": "Tervo DGR, Kuleshova E, Manakov M, Proskurin M, Karlsson M, Lustig A, Behnam R, Karpova AY.",
          "journalAbbreviation": "Neuron",
          "pubYear": 2021,
          "volume": "109",
          "issue": "11",
          "pageInfo": "1876-1887.e6",
          "citedByCount": 81
        },
        {
          "source": "MED",
          "id": "33836116",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Neural Representations of Task Context and Temporal Order During Action Sequence Execution.",
          "authorString": "Shahnazian D, Senoussi M, Krebs RM, Verguts T, Holroyd CB.",
          "journalAbbreviation": "Top Cogn Sci",
          "pubYear": 2022,
          "volume": "14",
          "issue": "2",
          "pageInfo": "223-240",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "33657434",
          "citationType": "research support, non-u.s. gov't; research-article; review; journal article",
          "title": "A salience misattribution model for addictive-like behaviors.",
          "authorString": "Kalhan S, Redish AD, Hester R, Garrido MI.",
          "journalAbbreviation": "Neurosci Biobehav Rev",
          "pubYear": 2021,
          "volume": "125",
          "pageInfo": "466-477",
          "citedByCount": 17
        },
        {
          "source": "MED",
          "id": "33593641",
          "citationType": "research support, non-u.s. gov't; review; journal article",
          "title": "The Best Laid Plans: Computational Principles of Anterior Cingulate Cortex.",
          "authorString": "Holroyd CB, Verguts T.",
          "journalAbbreviation": "Trends Cogn Sci",
          "pubYear": 2021,
          "volume": "25",
          "issue": "4",
          "pageInfo": "316-329",
          "citedByCount": 69
        },
        {
          "source": "MED",
          "id": "33531416",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Coordinated Prefrontal State Transition Leads Extinction of Reward-Seeking Behaviors.",
          "authorString": "Russo E, Ma T, Spanagel R, Durstewitz D, Toutounji H, K\u00f6hr G.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2021,
          "volume": "41",
          "issue": "11",
          "pageInfo": "2406-2419",
          "citedByCount": 18
        },
        {
          "source": "MED",
          "id": "33785153",
          "citationType": "journal article",
          "title": "The midcingulate cortex and temporal integration.",
          "authorString": "Procyk E, Fontanier V, Sarazin M, Delord B, Goussi C, Wilson CRE.",
          "journalAbbreviation": "Int Rev Neurobiol",
          "pubYear": 2021,
          "volume": "158",
          "pageInfo": "395-419",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "33442034",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Age affects procedural paired-associates learning in the grey mouse lemur (Microcebus murinus).",
          "authorString": "Schmidtke D.",
          "journalAbbreviation": "Sci Rep",
          "pubYear": 2021,
          "volume": "11",
          "issue": "1",
          "pageInfo": "1252",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "33785147",
          "citationType": "research-article; review; journal article",
          "title": "Potential roles of the rodent medial prefrontal cortex in conflict resolution between multiple decision-making systems.",
          "authorString": "McLaughlin AE, Diehl GW, Redish AD.",
          "journalAbbreviation": "Int Rev Neurobiol",
          "pubYear": 2021,
          "volume": "158",
          "pageInfo": "249-281",
          "citedByCount": 19
        },
        {
          "source": "PPR",
          "id": "PPR222063",
          "citationType": "preprint",
          "title": "Rapid suppression and sustained activation of distinct cortical regions for a delayed sensory-triggered motor response",
          "authorString": "Esmaeili V, Tamura K, Muscinelli SP, Modirshanechi A, Boscaglia M, Lee AB, Oryshchuk A, Foustoukos G, Liu Y, Crochet S, Gerstner W, Petersen CC.",
          "pubYear": 2020,
          "citedByCount": 1
        },
        {
          "source": "PPR",
          "id": "PPR167239",
          "citationType": "preprint",
          "title": "Anterior Cingulate Cortex Directs Exploration of Alternative Strategies",
          "authorString": "Tervo DGR, Kuleshova E, Manakov M, Proskurin M, Karlsson M, Lustig A, Behnam R, Karpova AY.",
          "pubYear": 2020,
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "32302586",
          "citationType": "research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "Secondary Motor Cortex Transforms Spatial Information into Planned Action during Navigation.",
          "authorString": "Olson JM, Li JK, Montgomery SE, Nitz DA.",
          "journalAbbreviation": "Curr Biol",
          "pubYear": 2020,
          "volume": "30",
          "issue": "10",
          "pageInfo": "1845-1854.e4",
          "citedByCount": 32
        },
        {
          "source": "MED",
          "id": "32276121",
          "citationType": "research-article; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "Dorsomedial prefrontal cortex and hippocampus represent strategic context even while simultaneously changing representation throughout a task session.",
          "authorString": "Hasz BM, Redish AD.",
          "journalAbbreviation": "Neurobiol Learn Mem",
          "pubYear": 2020,
          "volume": "171",
          "pageInfo": "107215",
          "citedByCount": 31
        },
        {
          "source": "PPR",
          "id": "PPR115144",
          "citationType": "preprint",
          "title": "Coordinated prefrontal state transition leads extinction of reward-seeking behaviors",
          "authorString": "Russo E, Ma T, Spanagel R, Durstewitz D, Toutounji H, K\u00f6hr G.",
          "pubYear": 2020,
          "citedByCount": 1
        },
        {
          "source": "PPR",
          "id": "PPR91553",
          "citationType": "preprint",
          "title": "Subjective value, not a gridlike code, describes neural activity in ventromedial prefrontal cortex during value-based decision-making",
          "authorString": "Lee S, Yu LQ, Lerman C, Kable JW.",
          "pubYear": 2019,
          "citedByCount": 0
        },
        {
          "source": "PPR",
          "id": "PPR76071",
          "citationType": "preprint",
          "title": "Dynamic changes in Anterior Cingulate Cortex ensembles mark the transition from exploration to exploitation",
          "authorString": "Emberly E, Seamans Jeremy K.",
          "pubYear": 2019,
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "30814311",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Medial Prefrontal Cortex Population Activity Is Plastic Irrespective of Learning.",
          "authorString": "Singh A, Peyrache A, Humphries MD.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2019,
          "volume": "39",
          "issue": "18",
          "pageInfo": "3470-3483",
          "citedByCount": 16
        },
        {
          "source": "MED",
          "id": "30523066",
          "citationType": "research-article; research support, u.s. gov't, non-p.h.s.; journal article; research support, n.i.h., extramural",
          "title": "Dissociable Forms of Uncertainty-Driven Representational Change Across the Human Brain.",
          "authorString": "Nassar MR, McGuire JT, Ritz H, Kable JW.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2019,
          "volume": "39",
          "issue": "9",
          "pageInfo": "1688-1698",
          "citedByCount": 63
        },
        {
          "source": "MED",
          "id": "30349472",
          "citationType": "methods-article; journal article",
          "title": "Detecting Multiple Change Points Using Adaptive Regression Splines With Application to Neural Recordings.",
          "authorString": "Toutounji H, Durstewitz D.",
          "journalAbbreviation": "Front Neuroinform",
          "pubYear": 2018,
          "volume": "12",
          "pageInfo": "67",
          "citedByCount": 11
        },
        {
          "source": "MED",
          "id": "30165082",
          "citationType": "meta-analysis; research support, non-u.s. gov't; journal article",
          "title": "Tracking the neurodynamics of insight: A meta-analysis of neuroimaging studies.",
          "authorString": "Shen W, Tong Y, Li F, Yuan Y, Hommel B, Liu C, Luo J.",
          "journalAbbreviation": "Biol Psychol",
          "pubYear": 2018,
          "volume": "138",
          "pageInfo": "189-198",
          "citedByCount": 38
        },
        {
          "source": "PPR",
          "id": "PPR7350",
          "citationType": "preprint",
          "title": "Dissociable forms of uncertainty-driven representational change across the human brain",
          "authorString": "Nassar MR, McGuire JT, Ritz H, Kable J.",
          "pubYear": 2018,
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "29915053",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Coordinated prefrontal-hippocampal activity and navigation strategy-related prefrontal firing during spatial memory formation.",
          "authorString": "Negr\u00f3n-Oyarzo I, Espinosa N, Aguilar-Rivera M, Fuenzalida M, Aboitiz F, Fuentealba P.",
          "journalAbbreviation": "Proc Natl Acad Sci U S A",
          "pubYear": 2018,
          "volume": "115",
          "issue": "27",
          "pageInfo": "7123-7128",
          "citedByCount": 66
        },
        {
          "source": "MED",
          "id": "29880806",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "An ensemble code in medial prefrontal cortex links prior events to outcomes during learning.",
          "authorString": "Maggi S, Peyrache A, Humphries MD.",
          "journalAbbreviation": "Nat Commun",
          "pubYear": 2018,
          "volume": "9",
          "issue": "1",
          "pageInfo": "2204",
          "citedByCount": 20
        },
        {
          "source": "MED",
          "id": "29866834",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Human midcingulate cortex encodes distributed representations of task progress.",
          "authorString": "Holroyd CB, Ribas-Fernandes JJF, Shahnazian D, Silvetti M, Verguts T.",
          "journalAbbreviation": "Proc Natl Acad Sci U S A",
          "pubYear": 2018,
          "volume": "115",
          "issue": "25",
          "pageInfo": "6398-6403",
          "citedByCount": 43
        },
        {
          "source": "MED",
          "id": "30090869",
          "citationType": "research-article; journal article",
          "title": "Dynamical networks: Finding, measuring, and tracking neural population activity using network science.",
          "authorString": "Humphries MD.",
          "journalAbbreviation": "Netw Neurosci",
          "pubYear": 2018,
          "volume": "1",
          "issue": "4",
          "pageInfo": "324-338",
          "citedByCount": 21
        },
        {
          "source": "MED",
          "id": "29058673",
          "citationType": "research-article; journal article; research support, n.i.h., extramural",
          "title": "Risk of punishment influences discrete and coordinated encoding of reward-guided actions by prefrontal cortex and VTA neurons.",
          "authorString": "Park J, Moghaddam B.",
          "journalAbbreviation": "Elife",
          "pubYear": 2017,
          "volume": "6",
          "pageInfo": "e30056",
          "citedByCount": 53
        },
        {
          "source": "MED",
          "id": "29034318",
          "citationType": "research-article; journal article",
          "title": "Mediodorsal Thalamic Neurons Mirror the Activity of Medial Prefrontal Neurons Responding to Movement and Reinforcement during a Dynamic DNMTP Task.",
          "authorString": "Miller RLA, Francoeur MJ, Gibson BM, Mair RG.",
          "journalAbbreviation": "eNeuro",
          "pubYear": 2017,
          "volume": "4",
          "issue": "5",
          "pageInfo": "ENEURO.0196-17.2017",
          "citedByCount": 16
        },
        {
          "source": "MED",
          "id": "28729442",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Adaptive Encoding of Outcome Prediction by Prefrontal Cortex Ensembles Supports Behavioral Flexibility.",
          "authorString": "Del Arco A, Park J, Wood J, Kim Y, Moghaddam B.",
          "journalAbbreviation": "J Neurosci",
          "pubYear": 2017,
          "volume": "37",
          "issue": "35",
          "pageInfo": "8363-8373",
          "citedByCount": 58
        },
        {
          "source": "MED",
          "id": "28688871",
          "citationType": "research support, non-u.s. gov't; research-article; review; journal article; research support, n.i.h., extramural",
          "title": "The Lateral Habenula and Adaptive Behaviors.",
          "authorString": "Mizumori SJY, Baker PM.",
          "journalAbbreviation": "Trends Neurosci",
          "pubYear": 2017,
          "volume": "40",
          "issue": "8",
          "pageInfo": "481-493",
          "citedByCount": 78
        },
        {
          "source": "MED",
          "id": "28081125",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "The Neural Representation of Prospective Choice during Spatial Planning and Decisions.",
          "authorString": "Kaplan R, King J, Koster R, Penny WD, Burgess N, Friston KJ.",
          "journalAbbreviation": "PLoS Biol",
          "pubYear": 2017,
          "volume": "15",
          "issue": "1",
          "pageInfo": "e1002588",
          "citedByCount": 60
        },
        {
          "source": "PPR",
          "id": "PPR28360",
          "citationType": "preprint",
          "title": "Medial prefrontal cortex population activity is plastic irrespective of learning",
          "authorString": "Singh A, Peyrache A, Humphries MD.",
          "pubYear": 2015,
          "citedByCount": 1
        }
      ],
      "errors": [],
      "ncbi": {
        "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&linkname=pubmed_pubmed_citedin&id=27653278&retmode=json",
        "response_sha256": "2cbab52c02873dc27958016a04f9c0e4bef75ab3e5bb9884658421723cad6372",
        "linksets": [
          {
            "dbfrom": "pubmed",
            "ids": [
              "27653278"
            ],
            "linksetdbs": [
              {
                "dbto": "pubmed",
                "linkname": "pubmed_pubmed_citedin",
                "links": [
                  "42222131",
                  "42092148",
                  "41620492",
                  "40562795",
                  "40097186",
                  "40097184",
                  "40027783",
                  "39938512",
                  "39825081",
                  "39715747",
                  "39696528",
                  "39557563",
                  "39476843",
                  "39314328",
                  "39313320",
                  "39235662",
                  "39038921",
                  "38638163",
                  "38426402",
                  "38370807",
                  "38050098",
                  "37991007",
                  "37086556",
                  "36822467",
                  "36652289",
                  "36311857",
                  "36306326",
                  "35422440",
                  "34957854",
                  "34184635",
                  "34077741",
                  "33991700",
                  "33785147",
                  "33657434",
                  "33531416",
                  "33442034",
                  "32276121",
                  "30814311",
                  "30523066",
                  "30349472",
                  "30090869",
                  "29915053",
                  "29880806",
                  "29866834",
                  "29058673",
                  "29034318",
                  "28729442",
                  "28688871",
                  "28081125"
                ]
              }
            ]
          }
        ],
        "error": null
      }
    },
    "Knoblich2001": {
      "pmid": "11820744",
      "europe_pmc_queries": [
        {
          "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/MED/11820744/citations?format=json&page=1&pageSize=1000",
          "response_sha256": "6abeeba4eccfdfa817768c3149d841b159c73bf286068aa9451748ac193c831d",
          "hitCount": 136
        }
      ],
      "records": [
        {
          "source": "MED",
          "id": "42646013",
          "citationType": "research-article; journal article",
          "title": "Comparing Aha! Moments in Problem Solving and Generative Ideation.",
          "authorString": "Chandolia VJ, Kidd MA, Paladino MS, Smith SM.",
          "journalAbbreviation": "J Intell",
          "pubYear": 2026,
          "volume": "14",
          "issue": "8",
          "pageInfo": "161",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "42092356",
          "citationType": "journal article",
          "title": "An Aha moment precedes the strategic response to a visuomotor rotation.",
          "authorString": "Townsend M, Warburton M, Campagnoli C, Mon-Williams M, Mushtaq F, Morehead JR.",
          "journalAbbreviation": "Curr Biol",
          "pubYear": 2026,
          "volume": "36",
          "issue": "10",
          "pageInfo": "2568-2580.e5",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "42019249",
          "citationType": "journal article",
          "title": "Aha! moments correspond to metacognitive prediction errors.",
          "authorString": "Dubey R, Ho M, Mehta H, Griffiths TL.",
          "journalAbbreviation": "Cognition",
          "pubYear": 2026,
          "volume": "274",
          "pageInfo": "106537",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "40963791",
          "citationType": "review-article; review; journal article",
          "title": "Creativity and aesthetic evaluation of AI-generated artworks: bridging problems and methods from psychology to AI.",
          "authorString": "Bianchi I, Branchini E, Uricchio T, Bongelli R.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2025,
          "volume": "16",
          "pageInfo": "1648480",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "40919409",
          "citationType": "research-article; journal article",
          "title": "Neural substrates associated with irrelevant information suppression in problem-solving: an fMRI study of the Remote Associates Test.",
          "authorString": "Ohkuma R, Kurihara Y, Osu R.",
          "journalAbbreviation": "Front Hum Neurosci",
          "pubYear": 2025,
          "volume": "19",
          "pageInfo": "1607193",
          "citedByCount": 0
        },
        {
          "source": "PPR",
          "id": "PPR1020886",
          "citationType": "preprint",
          "title": "An \u201cAha!\u201d moment precedes the strategic response to a visuomotor rotation",
          "authorString": "Townsend M, Warburton M, Campagnoli C, Mon-Williams M, Mushtaq F, Morehead JR.",
          "pubYear": 2025,
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "40334329",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The mechanism of chunk restructuring in the memory superiority effect of Insight: Dissociating the roles of decomposition and composition.",
          "authorString": "Zhang Z, Su Y, Gang Y, Xing Q.",
          "journalAbbreviation": "Conscious Cogn",
          "pubYear": 2025,
          "volume": "132",
          "pageInfo": "103877",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "40137068",
          "citationType": "research-article; journal article",
          "title": "Dissociable Effects of Verbalization on Solving Insight and Non-Insight Problems.",
          "authorString": "Macchi L, Poli F, Caravona L.",
          "journalAbbreviation": "J Intell",
          "pubYear": 2025,
          "volume": "13",
          "issue": "3",
          "pageInfo": "36",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "39833601",
          "citationType": "research-article; journal article",
          "title": "Can't help processing numbers with text: Eye-tracking evidence for simultaneous instead of sequential processing of text and numbers in arithmetic word problems.",
          "authorString": "Roth L, Nuerk HC, Cramer F, Daroczy G.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2025,
          "volume": "89",
          "issue": "1",
          "pageInfo": "50",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "39852414",
          "citationType": "editorial",
          "title": "Metareasoning: Theoretical and Methodological Developments.",
          "authorString": "Ball LJ, Richardson BH.",
          "journalAbbreviation": "J Intell",
          "pubYear": 2025,
          "volume": "13",
          "issue": "1",
          "pageInfo": "5",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "39135748",
          "citationType": "research-article; journal article",
          "title": "Insights into conscious cognitive information processing.",
          "authorString": "Dere E.",
          "journalAbbreviation": "Front Behav Neurosci",
          "pubYear": 2024,
          "volume": "18",
          "pageInfo": "1443161",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "38630293",
          "citationType": "journal article",
          "title": "The lack of Aha! experience can be dependent on the problem difficulty.",
          "authorString": "\u00d6zen-Ak\u0131n G, Cinan S.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2024,
          "volume": "88",
          "issue": "5",
          "pageInfo": "1522-1539",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "38425554",
          "citationType": "research-article; journal article",
          "title": "Ambient and focal attention during complex problem-solving: preliminary evidence from real-world eye movement data.",
          "authorString": "Guo Y, Pannasch S, Helmert JR, Kaszowska A.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2024,
          "volume": "15",
          "pageInfo": "1217106",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "38351525",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Funny? Think About It! Selective effect of cognitive mechanisms of humour on insight problems.",
          "authorString": "Korovkin SY, Morozova EN, Nikiforova OS.",
          "journalAbbreviation": "Cogn Emot",
          "pubYear": 2024,
          "volume": "38",
          "issue": "5",
          "pageInfo": "768-788",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "37998674",
          "citationType": "research-article; journal article",
          "title": "The Effects of Visual Cueing on Students with and without Math Learning Difficulties in Online Problem Solving: Evidence from Eye Movement.",
          "authorString": "Wei S, Lei Q, Chen Y, Xin YP.",
          "journalAbbreviation": "Behav Sci (Basel)",
          "pubYear": 2023,
          "volume": "13",
          "issue": "11",
          "pageInfo": "927",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "38035909",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Exploring the potential of eye tracking on personalized learning and real-time feedback in modern education.",
          "authorString": "da Silva Soares R, Oku AYA, Barreto CDSF, Sato JR.",
          "journalAbbreviation": "Prog Brain Res",
          "pubYear": 2023,
          "volume": "282",
          "pageInfo": "49-70",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "37790727",
          "citationType": "research-article; journal article",
          "title": "The Unconscious Tug-of-War: Exploring the Effect of Stimulus Selection Bias on Creative Problem Solving with Multiple Unconscious Stimuli.",
          "authorString": "Liu C, Tu S, Gong S, Guan J, Shi Z, Chen Y.",
          "journalAbbreviation": "Psychol Res Behav Manag",
          "pubYear": 2023,
          "volume": "16",
          "pageInfo": "3987-4002",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "38024571",
          "citationType": "research-article; journal article",
          "title": "Activity-Based Approach to the Teaching and Psychology of Insightful Problem Solving: Scientific Concepts as a Form of Constructive Criticism.",
          "authorString": "Romashchuk AN.",
          "journalAbbreviation": "Psychol Russ",
          "pubYear": 2023,
          "volume": "16",
          "issue": "3",
          "pageInfo": "14-29",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "37623545",
          "citationType": "research-article; journal article",
          "title": "Individuals with High Metacognitive Ability Are Better at Divergent and Convergent Thinking.",
          "authorString": "Jiang L, Yang C, Pi Z, Li Y, Liu S, Yi X.",
          "journalAbbreviation": "J Intell",
          "pubYear": 2023,
          "volume": "11",
          "issue": "8",
          "pageInfo": "162",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "37233335",
          "citationType": "research-article; journal article",
          "title": "Tracing Cognitive Processes in Insight Problem Solving: Using GAMs and Change Point Analysis to Uncover Restructuring.",
          "authorString": "Graf M, Danek AH, Vaci N, Bilali\u0107 M.",
          "journalAbbreviation": "J Intell",
          "pubYear": 2023,
          "volume": "11",
          "issue": "5",
          "pageInfo": "86",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "36732422",
          "citationType": "journal article",
          "title": "A comparative study of the cognitive load of basic-level category, superordinate category and subordinate category.",
          "authorString": "Ji M, Luo C, Ren J, Yang Y.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2023,
          "volume": "87",
          "issue": "7",
          "pageInfo": "2192-2203",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "36674221",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Mechanism Models of the Conventional and Advanced Methods of Construction Safety Training. Is the Traditional Method of Safety Training Sufficient?",
          "authorString": "Rafindadi AD, Shafiq N, Othman I, Miki\u0107 M.",
          "journalAbbreviation": "Int J Environ Res Public Health",
          "pubYear": 2023,
          "volume": "20",
          "issue": "2",
          "pageInfo": "1466",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "36551064",
          "citationType": "editorial",
          "title": "Emerging Wearable Biosensor Technologies for Stress Monitoring and Their Real-World Applications.",
          "authorString": "Wu JY, Ching CT, Wang HD, Liao LD.",
          "journalAbbreviation": "Biosensors (Basel)",
          "pubYear": 2022,
          "volume": "12",
          "issue": "12",
          "pageInfo": "1097",
          "citedByCount": 19
        },
        {
          "source": "MED",
          "id": "36374909",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Structure learning enhances concept formation in synthetic Active Inference agents.",
          "authorString": "Neacsu V, Mirza MB, Adams RA, Friston KJ.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2022,
          "volume": "17",
          "issue": "11",
          "pageInfo": "e0277199",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "37465144",
          "citationType": "research-article; journal article",
          "title": "Incorporation of prior knowledge and habits while solving anagrams.",
          "authorString": "Murray J, Sutter A, Lobifaro A, Cousens G, Kouh M.",
          "journalAbbreviation": "J Eye Mov Res",
          "pubYear": 2022,
          "volume": "15",
          "issue": "5",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "36081729",
          "citationType": "research-article; journal article",
          "title": "Differences in the distribution of attention to trained procedure between finders and non-finders of the alternative better procedure.",
          "authorString": "Ninomiya Y, Terai H, Miwa K.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2022,
          "volume": "13",
          "pageInfo": "934029",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "35751854",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Cognitive control of invalid predominant ideas in insight-like problem solving.",
          "authorString": "Zhou L, Yan H, Ren J, Li F, Luo J, Huang F.",
          "journalAbbreviation": "Psychophysiology",
          "pubYear": 2022,
          "volume": "59",
          "issue": "12",
          "pageInfo": "e14133",
          "citedByCount": 1
        },
        {
          "source": "PPR",
          "id": "PPR495142",
          "citationType": "preprint",
          "title": "Brain Activity During Constraint Relaxation in the Insight Problem-Solving Process: An fNIRS Study",
          "authorString": "Ohkuma R, Kurihara Y, Takahashi T, Osu R.",
          "pubYear": 2022,
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "35308608",
          "citationType": "research-article; journal article",
          "title": "Titles and Semantic Violations Affect Eye Movements When Viewing Contemporary Paintings.",
          "authorString": "Ganczarek J, Pietras K, Stoli\u0144ska A, Szubielska M.",
          "journalAbbreviation": "Front Hum Neurosci",
          "pubYear": 2022,
          "volume": "16",
          "pageInfo": "808330",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "35140344",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "Overcoming cognitive set bias requires more than seeing an alternative strategy.",
          "authorString": "Pope-Caldwell SM, Washburn DA.",
          "journalAbbreviation": "Sci Rep",
          "pubYear": 2022,
          "volume": "12",
          "issue": "1",
          "pageInfo": "2179",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "34985128",
          "citationType": "journal article",
          "title": "Visual behavior patterns of successful decision makers in crime scene photo investigation: An eye tracking analysis.",
          "authorString": "Chang RC, Tsai MJ.",
          "journalAbbreviation": "J Forensic Sci",
          "pubYear": 2022,
          "volume": "67",
          "issue": "3",
          "pageInfo": "1072-1083",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "34975690",
          "citationType": "review-article; review; journal article",
          "title": "Current Understanding of the \"Insight\" Phenomenon Across Disciplines.",
          "authorString": "Osuna-Mascar\u00f3 AJ, Auersperg AMI.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2021,
          "volume": "12",
          "pageInfo": "791398",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "33721581",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The Aha! moment: Is insight a different form of problem solving?",
          "authorString": "Stuyck H, Aben B, Cleeremans A, Van den Bussche E.",
          "journalAbbreviation": "Conscious Cogn",
          "pubYear": 2021,
          "volume": "90",
          "pageInfo": "103055",
          "citedByCount": 27
        },
        {
          "source": "MED",
          "id": "33543773",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Left-hemispheric predominance on appropriateness evaluation of restructuring during chunk decomposition problem solving.",
          "authorString": "Zhang Z, Lei Y, Xing Q, Li H.",
          "journalAbbreviation": "Psychophysiology",
          "pubYear": 2021,
          "volume": "58",
          "issue": "4",
          "pageInfo": "e13778",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "33387575",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Revealing the dynamics of prospective memory processes in children with eye movements.",
          "authorString": "Hartwig J, Kretschmer-Trendowicz A, Helmert JR, Jung ML, Pannasch S.",
          "journalAbbreviation": "Int J Psychophysiol",
          "pubYear": 2021,
          "volume": "160",
          "pageInfo": "38-55",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "32681861",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Stimulus complexity and chunk tightness interact to impede perceptual restructuring during problem solving.",
          "authorString": "Zhang Z, Warren CM, Lei Y, Xing Q, Li H.",
          "journalAbbreviation": "Biol Psychol",
          "pubYear": 2020,
          "volume": "155",
          "pageInfo": "107930",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "32564616",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The mental welfare effect of creativity: how does creativity make people happy?",
          "authorString": "Shen W, Hua M, Wang M, Yuan Y.",
          "journalAbbreviation": "Psychol Health Med",
          "pubYear": 2021,
          "volume": "26",
          "issue": "9",
          "pageInfo": "1045-1052",
          "citedByCount": 7
        },
        {
          "source": "MED",
          "id": "32655713",
          "citationType": "research-article; journal article",
          "title": "The late parietal event-related potential component is hierarchically sensitive to chunk tightness during chunk decomposition.",
          "authorString": "Zhang Z, Lu Z, Warren CM, Rong C, Xing Q.",
          "journalAbbreviation": "Cogn Neurodyn",
          "pubYear": 2020,
          "volume": "14",
          "issue": "4",
          "pageInfo": "501-508",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "32194284",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The function of the hippocampus and middle temporal gyrus in forming new associations and concepts during the processing of novelty and usefulness features in creative designs.",
          "authorString": "Ren J, Huang F, Zhou Y, Zhuang L, Xu J, Gao C, Qin S, Luo J.",
          "journalAbbreviation": "Neuroimage",
          "pubYear": 2020,
          "volume": "214",
          "pageInfo": "116751",
          "citedByCount": 67
        },
        {
          "source": "MED",
          "id": "31446653",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "When the Solution Is on the Doorstep: Better Solving Performance, but Diminished Aha! Experience for Chess Experts on the Mutilated Checkerboard Problem.",
          "authorString": "Bilali\u0107 M, Graf M, Vaci N, Danek AH.",
          "journalAbbreviation": "Cogn Sci",
          "pubYear": 2019,
          "volume": "43",
          "issue": "8",
          "pageInfo": "e12771",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "31191410",
          "citationType": "review-article; review; journal article",
          "title": "How Does Culture Shape Creativity? A Mini-Review.",
          "authorString": "Shao Y, Zhang C, Zhou J, Gu T, Yuan Y.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2019,
          "volume": "10",
          "pageInfo": "1219",
          "citedByCount": 21
        },
        {
          "source": "MED",
          "id": "31156488",
          "citationType": "research-article; journal article",
          "title": "An Eye-Tracking Study of Statistical Reasoning With Tree Diagrams and 2 \u00d7 2 Tables.",
          "authorString": "Bruckmaier G, Binder K, Krauss S, Kufner HM.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2019,
          "volume": "10",
          "pageInfo": "632",
          "citedByCount": 11
        },
        {
          "source": "MED",
          "id": "31068884",
          "citationType": "research-article; journal article",
          "title": "The Effect of Working Memory Updating Ability on Spatial Insight Problem Solving: Evidence From Behavior and Eye Movement Studies.",
          "authorString": "Xing Q, Lu Z, Hu J.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2019,
          "volume": "10",
          "pageInfo": "927",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "30728789",
          "citationType": "research-article; journal article",
          "title": "The Role of Motor Activity in Insight Problem Solving (the Case of the Nine-Dot Problem).",
          "authorString": "Spiridonov V, Loginov N, Ivanchei I, Kurgansky AV.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2019,
          "volume": "10",
          "pageInfo": "2",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "30631294",
          "citationType": "research-article; journal article",
          "title": "Virtual Reality as a New Approach for Risk Taking Assessment.",
          "authorString": "de-Juan-Ripoll C, Soler-Dom\u00ednguez JL, Guixeres J, Contero M, \u00c1lvarez Guti\u00e9rrez N, Alca\u00f1iz M.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2018,
          "volume": "9",
          "pageInfo": "2532",
          "citedByCount": 15
        },
        {
          "source": "MED",
          "id": "30534097",
          "citationType": "research-article; journal article",
          "title": "The Effect of the Embodied Guidance in the Insight Problem Solving: An Eye Movement Study.",
          "authorString": "Xing Q, Rong C, Lu Z, Yao Y, Zhang Z, Zhao X.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2018,
          "volume": "9",
          "pageInfo": "2257",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "30327635",
          "citationType": "research-article; journal article",
          "title": "How Working Memory Provides Representational Change During Insight Problem Solving.",
          "authorString": "Korovkin S, Vladimirov I, Chistopolskaya A, Savinova A.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2018,
          "volume": "9",
          "pageInfo": "1864",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "30258378",
          "citationType": "research-article; journal article",
          "title": "Virtual Reality as an Emerging Methodology for Leadership Assessment and Training.",
          "authorString": "Alca\u00f1iz M, Parra E, Chicchi Giglioli IA.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2018,
          "volume": "9",
          "pageInfo": "1658",
          "citedByCount": 12
        },
        {
          "source": "MED",
          "id": "30161187",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Neural correlates of creative insight: Amplitude of low-frequency fluctuation of resting-state brain activity predicts creative insight.",
          "authorString": "Lin J, Cui X, Dai X, Chen Y, Mo L.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2018,
          "volume": "13",
          "issue": "8",
          "pageInfo": "e0203071",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "30165082",
          "citationType": "meta-analysis; research support, non-u.s. gov't; journal article",
          "title": "Tracking the neurodynamics of insight: A meta-analysis of neuroimaging studies.",
          "authorString": "Shen W, Tong Y, Li F, Yuan Y, Hommel B, Liu C, Luo J.",
          "journalAbbreviation": "Biol Psychol",
          "pubYear": 2018,
          "volume": "138",
          "pageInfo": "189-198",
          "citedByCount": 38
        },
        {
          "source": "MED",
          "id": "30150953",
          "citationType": "research-article; journal article",
          "title": "Feelings-of-Warmth Increase More Abruptly for Verbal Riddles Solved With in Contrast to Without Aha! Experience.",
          "authorString": "Kizilirmak JM, Serger V, Kehl J, \u00d6llinger M, Folta-Schoofs K, Richardson-Klavehn A.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2018,
          "volume": "9",
          "pageInfo": "1404",
          "citedByCount": 14
        },
        {
          "source": "MED",
          "id": "30018576",
          "citationType": "research-article; journal article",
          "title": "\"The Penny Drops\": Investigating Insight Through the Medium of Cryptic Crosswords.",
          "authorString": "Friedlander KJ, Fine PA.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2018,
          "volume": "9",
          "pageInfo": "904",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "29951753",
          "citationType": "journal article",
          "title": "Quantifying insightful problem solving: a modified compound remote associates paradigm using lexical priming to parametrically modulate different sources of task difficulty.",
          "authorString": "Becker M, Wiedemann G, K\u00fchn S.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2020,
          "volume": "84",
          "issue": "2",
          "pageInfo": "528-545",
          "citedByCount": 15
        },
        {
          "source": "MED",
          "id": "29875645",
          "citationType": "research-article; journal article",
          "title": "Regional Homogeneity Predicts Creative Insight: A Resting-State fMRI Study.",
          "authorString": "Lin J, Cui X, Dai X, Mo L.",
          "journalAbbreviation": "Front Hum Neurosci",
          "pubYear": 2018,
          "volume": "12",
          "pageInfo": "210",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "29867650",
          "citationType": "research-article; journal article",
          "title": "The Mnemonic Effects of Novelty and Appropriateness in Creative Chunk Decomposition Tasks.",
          "authorString": "Wu X, Liu Y, Luo J.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2018,
          "volume": "9",
          "pageInfo": "673",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "29665228",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Ultra-high-field fMRI insights on insight: Neural correlates of the Aha!-moment.",
          "authorString": "Tik M, Sladky R, Luft CDB, Willinger D, Hoffmann A, Banissy MJ, Bhattacharya J, Windischberger C.",
          "journalAbbreviation": "Hum Brain Mapp",
          "pubYear": 2018,
          "volume": "39",
          "issue": "8",
          "pageInfo": "3241-3252",
          "citedByCount": 86
        },
        {
          "source": "MED",
          "id": "29416518",
          "citationType": "research-article; journal article",
          "title": "Pleasures of the Mind: What Makes Jokes and Insight Problems Enjoyable.",
          "authorString": "Canestrari C, Branchini E, Bianchi I, Savardi U, Burro R.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2017,
          "volume": "8",
          "pageInfo": "2297",
          "citedByCount": 7
        },
        {
          "source": "MED",
          "id": "29349507",
          "citationType": "journal article",
          "title": "Closing the gap: connecting sudden representational change to the subjective Aha! experience in insightful problem solving.",
          "authorString": "Danek AH, Williams J, Wiley J.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2020,
          "volume": "84",
          "issue": "1",
          "pageInfo": "111-119",
          "citedByCount": 26
        },
        {
          "source": "MED",
          "id": "29337998",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Cognitive mechanisms for inferring the meaning of novel signals during symbolisation.",
          "authorString": "Sulik J.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2018,
          "volume": "13",
          "issue": "1",
          "pageInfo": "e0189540",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "28540753",
          "citationType": "journal article",
          "title": "Learning from where 'eye' remotely look or point: Impact on number line estimation error in adults.",
          "authorString": "Gallagher-Mitchell T, Simms V, Litchfield D.",
          "journalAbbreviation": "Q J Exp Psychol (Hove)",
          "pubYear": 2018,
          "volume": "71",
          "issue": "7",
          "pageInfo": "1526-1534",
          "citedByCount": 3
        },
        {
          "source": "MED",
          "id": "29184525",
          "citationType": "research-article; journal article",
          "title": "Decomposing a Chunk into Its Elements and Reorganizing Them As a New Chunk: The Two Different Sub-processes Underlying Insightful Chunk Decomposition.",
          "authorString": "Wu X, He M, Zhou Y, Xiao J, Luo J.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2017,
          "volume": "8",
          "pageInfo": "2001",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "29031120",
          "citationType": "journal article",
          "title": "Enabling spontaneous analogy through heuristic change.",
          "authorString": "Ormerod TC, MacGregor JN.",
          "journalAbbreviation": "Cogn Psychol",
          "pubYear": 2017,
          "volume": "99",
          "pageInfo": "1-16",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "28966603",
          "citationType": "research-article; journal article",
          "title": "Role of Creativity in the Effectiveness of Cognitive Reappraisal.",
          "authorString": "Wu X, Guo T, Tang T, Shi B, Luo J.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2017,
          "volume": "8",
          "pageInfo": "1598",
          "citedByCount": 25
        },
        {
          "source": "MED",
          "id": "28777724",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Active Inference, Curiosity and Insight.",
          "authorString": "Friston KJ, Lin M, Frith CD, Pezzulo G, Hobson JA, Ondobaka S.",
          "journalAbbreviation": "Neural Comput",
          "pubYear": 2017,
          "volume": "29",
          "issue": "10",
          "pageInfo": "2633-2683",
          "citedByCount": 189
        },
        {
          "source": "MED",
          "id": "28611702",
          "citationType": "research-article; journal article",
          "title": "Search and Coherence-Building in Intuition and Insight Problem Solving.",
          "authorString": "\u00d6llinger M, von M\u00fcller A.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2017,
          "volume": "8",
          "pageInfo": "827",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "28520866",
          "citationType": "research support, non-u.s. gov't; research-article; journal article; research support, n.i.h., extramural",
          "title": "More Than the Verbal Stimulus Matters: Visual Attention in Language Assessment for People With Aphasia Using Multiple-Choice Image Displays.",
          "authorString": "Heuer S, Ivanova MV, Hallowell B.",
          "journalAbbreviation": "J Speech Lang Hear Res",
          "pubYear": 2017,
          "volume": "60",
          "issue": "5",
          "pageInfo": "1348-1361",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "28295482",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "What Am I Looking at? Interpreting Dynamic and Static Gaze Displays.",
          "authorString": "van Wermeskerken M, Litchfield D, van Gog T.",
          "journalAbbreviation": "Cogn Sci",
          "pubYear": 2018,
          "volume": "42",
          "issue": "1",
          "pageInfo": "220-252",
          "citedByCount": 10
        },
        {
          "source": "MED",
          "id": "28253076",
          "citationType": "journal article",
          "title": "Major Thought Restructuring: The Roles of Different Prefrontal Cortical Regions.",
          "authorString": "Seyed-Allaei S, Avanaki ZN, Bahrami B, Shallice T.",
          "journalAbbreviation": "J Cogn Neurosci",
          "pubYear": 2017,
          "volume": "29",
          "issue": "7",
          "pageInfo": "1147-1161",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "28082928",
          "citationType": "research-article; journal article",
          "title": "Can Contraries Prompt Intuition in Insight Problem Solving?",
          "authorString": "Branchini E, Bianchi I, Burro R, Capitani E, Savardi U.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "1962",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "27679592",
          "citationType": "research-article; journal article",
          "title": "Intuition and Insight: Two Processes That Build on Each Other or Fundamentally Differ?",
          "authorString": "Zander T, \u00d6llinger M, Volz KG.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "1395",
          "citedByCount": 22
        },
        {
          "source": "MED",
          "id": "27592343",
          "citationType": "research-article; journal article",
          "title": "Insight into the ten-penny problem: guiding search by constraints and maximization.",
          "authorString": "\u00d6llinger M, Fedor A, Brodt S, Szathm\u00e1ry E.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2017,
          "volume": "81",
          "issue": "5",
          "pageInfo": "925-938",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "27569687",
          "citationType": "journal article",
          "title": "Insight with hands and things.",
          "authorString": "Vall\u00e9e-Tourangeau F, Steffensen SV, Vall\u00e9e-Tourangeau G, Sirota M.",
          "journalAbbreviation": "Acta Psychol (Amst)",
          "pubYear": 2016,
          "volume": "170",
          "pageInfo": "195-205",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "27555833",
          "citationType": "review-article; review; journal article",
          "title": "Approaching the Distinction between Intuition and Insight.",
          "authorString": "Zhang Z, Lei Y, Li H.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "1195",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "27471485",
          "citationType": "research-article; journal article",
          "title": "Eye Movements during Art Appreciation by Students Taking a Photo Creation Course.",
          "authorString": "Ishiguro C, Yokosawa K, Okada T.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "1074",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "26887867",
          "citationType": "journal article",
          "title": "Persistent perceptual grouping effects in the evaluation of simple arithmetic expressions.",
          "authorString": "Rivera J, Garrigan P.",
          "journalAbbreviation": "Mem Cognit",
          "pubYear": 2016,
          "volume": "44",
          "issue": "5",
          "pageInfo": "750-761",
          "citedByCount": 4
        },
        {
          "source": "MED",
          "id": "26148823",
          "citationType": "validation study; journal article",
          "title": "Validation of Italian rebus puzzles and compound remote associate problems.",
          "authorString": "Salvi C, Costantini G, Bricolo E, Perugini M, Beeman M.",
          "journalAbbreviation": "Behav Res Methods",
          "pubYear": 2016,
          "volume": "48",
          "issue": "2",
          "pageInfo": "664-685",
          "citedByCount": 27
        },
        {
          "source": "MED",
          "id": "26913018",
          "citationType": "review-article; review; journal article",
          "title": "Looking for Creativity: Where Do We Look When We Look for New Ideas?",
          "authorString": "Salvi C, Bowden EM.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2016,
          "volume": "7",
          "pageInfo": "161",
          "citedByCount": 34
        },
        {
          "source": "AGR",
          "id": "IND605265669",
          "citationType": "journal article",
          "title": "Design factors influence consumers\u2019 gazing behaviour and decision time in an eye-tracking test: A study on food images",
          "authorString": "Vu TMH, Tu VP, Duerrschmid K.",
          "journalAbbreviation": "Food quality and preference.",
          "pubYear": 2016,
          "volume": "47",
          "pageInfo": "130-138",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "26529680",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Timing matters! The neural signature of intuitive judgments differs according to the way information is presented.",
          "authorString": "Horr NK, Braun C, Zander T, Volz KG.",
          "journalAbbreviation": "Conscious Cogn",
          "pubYear": 2015,
          "volume": "38",
          "pageInfo": "71-87",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "26300794",
          "citationType": "research-article; journal article",
          "title": "Problem solving stages in the five square problem.",
          "authorString": "Fedor A, Szathm\u00e1ry E, \u00d6llinger M.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2015,
          "volume": "6",
          "pageInfo": "1050",
          "citedByCount": 12
        },
        {
          "source": "MED",
          "id": "26257683",
          "citationType": "research-article; journal article",
          "title": "The influence of element type and crossed relation on the difficulty of chunk decomposition.",
          "authorString": "Zhang Z, Yang K, Warren CM, Zhao G, Li P, Lei Y, Li H.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2015,
          "volume": "6",
          "pageInfo": "1025",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "26167155",
          "citationType": "research-article; journal article",
          "title": "Enhancement of visual attention precedes the emergence of novel metaphor interpretations.",
          "authorString": "Terai A, Nakagawa M, Kusumi T, Koike Y, Jimura K.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2015,
          "volume": "6",
          "pageInfo": "892",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "26045566",
          "citationType": "journal article",
          "title": "Probing the Cognitive Mechanism of Mental Representational Change During Chunk Decomposition: A Parametric fMRI Study.",
          "authorString": "Tang X, Pang J, Nie QY, Conci M, Luo J, Luo J.",
          "journalAbbreviation": "Cereb Cortex",
          "pubYear": 2016,
          "volume": "26",
          "issue": "7",
          "pageInfo": "2991-2999",
          "citedByCount": 33
        },
        {
          "source": "MED",
          "id": "25957557",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Chunk decomposition contributes to forming new mental representations: An ERP study.",
          "authorString": "Zhang Z, Xing Q, Li H, Warren CM, Tang Z, Che J.",
          "journalAbbreviation": "Neurosci Lett",
          "pubYear": 2015,
          "volume": "598",
          "pageInfo": "12-17",
          "citedByCount": 1
        },
        {
          "source": "MED",
          "id": "25797834",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The neural basis of novelty and appropriateness in processing of creative chunk decomposition.",
          "authorString": "Huang F, Fan J, Luo J.",
          "journalAbbreviation": "Neuroimage",
          "pubYear": 2015,
          "volume": "113",
          "pageInfo": "122-132",
          "citedByCount": 64
        },
        {
          "source": "MED",
          "id": "25538658",
          "citationType": "research-article; journal article",
          "title": "It's a kind of magic-what self-reports can reveal about the phenomenology of insight problem solving.",
          "authorString": "Danek AH, Fraps T, von M\u00fcller A, Grothe B, \u00d6llinger M.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2014,
          "volume": "5",
          "pageInfo": "1408",
          "citedByCount": 65
        },
        {
          "source": "MED",
          "id": "25324804",
          "citationType": "research-article; journal article",
          "title": "Linking attentional processes and conceptual problem solving: visual cues facilitate the automaticity of extracting relevant information from diagrams.",
          "authorString": "Rouinfar A, Agra E, Larson AM, Rebello NS, Loschky LC.",
          "journalAbbreviation": "Front Psychol",
          "pubYear": 2014,
          "volume": "5",
          "pageInfo": "1094",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "25010653",
          "citationType": "journal article",
          "title": "Short-term induction of assimilation and accommodation.",
          "authorString": "Leipold B, Bermeitinger C, Greve W, Meyer B, Arnold M, Pielniok M.",
          "journalAbbreviation": "Q J Exp Psychol (Hove)",
          "pubYear": 2014,
          "volume": "67",
          "issue": "12",
          "pageInfo": "2392-2408",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "24759773",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Uniformity and nonuniformity of neural activities correlated to different insight problem solving.",
          "authorString": "Zhao Q, Li Y, Shang X, Zhou Z, Han L.",
          "journalAbbreviation": "Neuroscience",
          "pubYear": 2014,
          "volume": "270",
          "pageInfo": "203-211",
          "citedByCount": 10
        },
        {
          "source": "MED",
          "id": "24804429",
          "citationType": "journal article; english abstract",
          "title": "[Effect of positive and negative instances on rule discovery: investigation using eye tracking].",
          "authorString": "Matsumuro M, Miwa K.",
          "journalAbbreviation": "Shinrigaku Kenkyu",
          "pubYear": 2014,
          "volume": "85",
          "issue": "1",
          "pageInfo": "40-49",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "24300080",
          "citationType": "journal article",
          "title": "Working wonders? investigating insight with magic tricks.",
          "authorString": "Danek AH, Fraps T, von M\u00fcller A, Grothe B, Ollinger M.",
          "journalAbbreviation": "Cognition",
          "pubYear": 2014,
          "volume": "130",
          "issue": "2",
          "pageInfo": "174-185",
          "citedByCount": 60
        },
        {
          "source": "MED",
          "id": "24161281",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Neural pathway in the right hemisphere underlies verbal insight problem solving.",
          "authorString": "Zhao Q, Zhou Z, Xu H, Fan W, Han L.",
          "journalAbbreviation": "Neuroscience",
          "pubYear": 2014,
          "volume": "256",
          "pageInfo": "334-341",
          "citedByCount": 21
        },
        {
          "source": "MED",
          "id": "24124515",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "The mechanisms and boundary conditions of the Einstellung effect in chess: evidence from eye movements.",
          "authorString": "Sheridan H, Reingold EM.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2013,
          "volume": "8",
          "issue": "10",
          "pageInfo": "e75796",
          "citedByCount": 15
        },
        {
          "source": "MED",
          "id": "23532591",
          "citationType": "journal article",
          "title": "An eye for relations: eye-tracking indicates long-term negative effects of operational thinking on understanding of math equivalence.",
          "authorString": "Chesney DL, McNeil NM, Brockmole JR, Kelley K.",
          "journalAbbreviation": "Mem Cognit",
          "pubYear": 2013,
          "volume": "41",
          "issue": "7",
          "pageInfo": "1079-1095",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "23526396",
          "citationType": "research support, non-u.s. gov't; randomized controlled trial; journal article",
          "title": "Temporal dynamics of mental impasses underlying insight-like problem solving.",
          "authorString": "Shen W, Liu C, Yuan Y, Zhang X, Luo J.",
          "journalAbbreviation": "Sci China Life Sci",
          "pubYear": 2013,
          "volume": "56",
          "issue": "3",
          "pageInfo": "284-290",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "23555020",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Dynamic neural network of insight: a functional magnetic resonance imaging study on solving Chinese 'chengyu' riddles.",
          "authorString": "Zhao Q, Zhou Z, Xu H, Chen S, Xu F, Fan W, Han L.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2013,
          "volume": "8",
          "issue": "3",
          "pageInfo": "e59351",
          "citedByCount": 26
        },
        {
          "source": "MED",
          "id": "23534265",
          "citationType": "journal article; english abstract",
          "title": "[Facilitation and inhibition of insightful problem solving based on social comparison].",
          "authorString": "Ariga A.",
          "journalAbbreviation": "Shinrigaku Kenkyu",
          "pubYear": 2013,
          "volume": "83",
          "issue": "6",
          "pageInfo": "576-581",
          "citedByCount": 0
        },
        {
          "source": "MED",
          "id": "23007629",
          "citationType": "journal article",
          "title": "Aha! experiences leave a mark: facilitated recall of insight solutions.",
          "authorString": "Danek AH, Fraps T, von M\u00fcller A, Grothe B, Ollinger M.",
          "journalAbbreviation": "Psychol Res",
          "pubYear": 2013,
          "volume": "77",
          "issue": "5",
          "pageInfo": "659-669",
          "citedByCount": 65
        },
        {
          "source": "MED",
          "id": "22576927",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Association between methylene  tetrahydrofolate reductase and glutathione S-transferase M1 gene polymorphisms  and chronic myeloid leukemia in a Brazilian population.",
          "authorString": "Lordelo GS, Miranda-Vilela AL, Akimoto AK, Alves PC, Hiragi CO, Nonino A, Daldegan MB, Klautau-Guimar\u00e3es MN, Grisolia CK.",
          "journalAbbreviation": "Genet Mol Res",
          "pubYear": 2012,
          "volume": "11",
          "issue": "2",
          "pageInfo": "1013-1026",
          "citedByCount": 23
        },
        {
          "source": "MED",
          "id": "22328466",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "The role of chunk tightness and chunk familiarity in problem solving: evidence from ERPs and fMRI.",
          "authorString": "Wu L, Knoblich G, Luo J.",
          "journalAbbreviation": "Hum Brain Mapp",
          "pubYear": 2013,
          "volume": "34",
          "issue": "5",
          "pageInfo": "1173-1186",
          "citedByCount": 42
        },
        {
          "source": "MED",
          "id": "21316041",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Mindset changes lead to drastic impairments in rule finding.",
          "authorString": "Erel H, Meiran N.",
          "journalAbbreviation": "Cognition",
          "pubYear": 2011,
          "volume": "119",
          "issue": "2",
          "pageInfo": "149-165",
          "citedByCount": 7
        },
        {
          "source": "MED",
          "id": "21347990",
          "citationType": "randomized controlled trial; journal article",
          "title": "Using another's gaze as an explicit aid to insight problem solving.",
          "authorString": "Litchfield D, Ball LJ.",
          "journalAbbreviation": "Q J Exp Psychol (Hove)",
          "pubYear": 2011,
          "volume": "64",
          "issue": "4",
          "pageInfo": "649-656",
          "citedByCount": 17
        },
        {
          "source": "MED",
          "id": "21273095",
          "citationType": "journal article",
          "title": "Eye movements reveal solution knowledge prior to insight.",
          "authorString": "Ellis JJ, Glaholt MG, Reingold EM.",
          "journalAbbreviation": "Conscious Cogn",
          "pubYear": 2011,
          "volume": "20",
          "issue": "3",
          "pageInfo": "768-776",
          "citedByCount": 20
        },
        {
          "source": "MED",
          "id": "21181350",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Effective connectivity of dorsal and ventral visual pathways in chunk decomposition.",
          "authorString": "Wu Q, Wu L, Luo J.",
          "journalAbbreviation": "Sci China Life Sci",
          "pubYear": 2010,
          "volume": "53",
          "issue": "12",
          "pageInfo": "1474-1482",
          "citedByCount": 10
        },
        {
          "source": "MED",
          "id": "21046365",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The neural basis of breaking mental set: an event-related potential study.",
          "authorString": "Zhao Y, Tu S, Lei M, Qiu J, Ybarra O, Zhang Q.",
          "journalAbbreviation": "Exp Brain Res",
          "pubYear": 2011,
          "volume": "208",
          "issue": "2",
          "pageInfo": "181-187",
          "citedByCount": 8
        },
        {
          "source": "MED",
          "id": "22110327",
          "citationType": "review-article; journal article",
          "title": "Intuition, insight, and the right hemisphere: Emergence of higher sociocognitive functions.",
          "authorString": "McCrea SM.",
          "journalAbbreviation": "Psychol Res Behav Manag",
          "pubYear": 2010,
          "volume": "3",
          "pageInfo": "1-39",
          "citedByCount": 9
        },
        {
          "source": "MED",
          "id": "20121866",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Arithmetic word problem solving: a Situation Strategy First framework.",
          "authorString": "Brissiaud R, Sander E.",
          "journalAbbreviation": "Dev Sci",
          "pubYear": 2010,
          "volume": "13",
          "issue": "1",
          "pageInfo": "92-107",
          "citedByCount": 5
        },
        {
          "source": "MED",
          "id": "19933457",
          "citationType": "research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "The dynamics of insight: mathematical discovery as a phase transition.",
          "authorString": "Stephen DG, Boncoddo RA, Magnuson JS, Dixon JA.",
          "journalAbbreviation": "Mem Cognit",
          "pubYear": 2009,
          "volume": "37",
          "issue": "8",
          "pageInfo": "1132-1149",
          "citedByCount": 52
        },
        {
          "source": "MED",
          "id": "19695234",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "How perceptual processes help to generate new meaning: an EEG study of chunk decomposition in Chinese characters.",
          "authorString": "Wu L, Knoblich G, Wei G, Luo J.",
          "journalAbbreviation": "Brain Res",
          "pubYear": 2009,
          "volume": "1296",
          "pageInfo": "104-112",
          "citedByCount": 26
        },
        {
          "source": "MED",
          "id": "19449261",
          "citationType": "lecture; research support, n.i.h., extramural",
          "title": "Eye movements and attention in reading, scene perception, and visual search.",
          "authorString": "Rayner K.",
          "journalAbbreviation": "Q J Exp Psychol (Hove)",
          "pubYear": 2009,
          "volume": "62",
          "issue": "8",
          "pageInfo": "1457-1506",
          "citedByCount": 945
        },
        {
          "source": "MED",
          "id": "19309537",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Verbalization and problem solving: insight and spatial factors.",
          "authorString": "Gilhooly KJ, Fioratou E, Henretty N.",
          "journalAbbreviation": "Br J Psychol",
          "pubYear": 2010,
          "volume": "101",
          "issue": "pt 1",
          "pageInfo": "81-93",
          "citedByCount": 14
        },
        {
          "source": "MED",
          "id": "18834964",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "A generalization of the representational change theory from insight to non-insight problems: the case of arithmetic word problems.",
          "authorString": "Thevenot C, Oakhill J.",
          "journalAbbreviation": "Acta Psychol (Amst)",
          "pubYear": 2008,
          "volume": "129",
          "issue": "3",
          "pageInfo": "315-324",
          "citedByCount": 10
        },
        {
          "source": "MED",
          "id": "18723602",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Validity of eye movement methods and indices for capturing semantic (associative) priming effects.",
          "authorString": "Odekar A, Hallowell B, Kruse H, Moates D, Lee CY.",
          "journalAbbreviation": "J Speech Lang Hear Res",
          "pubYear": 2009,
          "volume": "52",
          "issue": "1",
          "pageInfo": "31-48",
          "citedByCount": 16
        },
        {
          "source": "MED",
          "id": "18565505",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Why good thoughts block better ones: the mechanism of the pernicious Einstellung (set) effect.",
          "authorString": "Bilali\u0107 M, McLeod P, Gobet F.",
          "journalAbbreviation": "Cognition",
          "pubYear": 2008,
          "volume": "108",
          "issue": "3",
          "pageInfo": "652-661",
          "citedByCount": 59
        },
        {
          "source": "MED",
          "id": "18604964",
          "citationType": "research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "Hindsight bias in insight and mathematical problem solving: evidence of different reconstruction mechanisms for metacognitive versus situational judgments.",
          "authorString": "Asa IK, Wiley J.",
          "journalAbbreviation": "Mem Cognit",
          "pubYear": 2008,
          "volume": "36",
          "issue": "4",
          "pageInfo": "822-837",
          "citedByCount": 11
        },
        {
          "source": "MED",
          "id": "17559716",
          "citationType": "research support, non-u.s. gov't; review; journal article",
          "title": "Intuition: a fundamental bridging construct in the behavioural sciences.",
          "authorString": "Hodgkinson GP, Langan-Fox J, Sadler-Smith E.",
          "journalAbbreviation": "Br J Psychol",
          "pubYear": 2008,
          "volume": "99",
          "issue": "pt 1",
          "pageInfo": "1-27",
          "citedByCount": 40
        },
        {
          "source": "MED",
          "id": "18213368",
          "citationType": "research support, non-u.s. gov't; research-article; journal article",
          "title": "Deconstructing insight: EEG correlates of insightful problem solving.",
          "authorString": "Sandk\u00fchler S, Bhattacharya J.",
          "journalAbbreviation": "PLoS One",
          "pubYear": 2008,
          "volume": "3",
          "issue": "1",
          "pageInfo": "e1459",
          "citedByCount": 101
        },
        {
          "source": "MED",
          "id": "18683624",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Investigating the effect of mental set on insight problem solving.",
          "authorString": "Ollinger M, Jones G, Knoblich G.",
          "journalAbbreviation": "Exp Psychol",
          "pubYear": 2008,
          "volume": "55",
          "issue": "4",
          "pageInfo": "269-282",
          "citedByCount": 50
        },
        {
          "source": "MED",
          "id": "17972730",
          "citationType": "research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "Moving eyes and moving thought: on the spatial compatibility between eye movements and cognition.",
          "authorString": "Thomas LE, Lleras A.",
          "journalAbbreviation": "Psychon Bull Rev",
          "pubYear": 2007,
          "volume": "14",
          "issue": "4",
          "pageInfo": "663-668",
          "citedByCount": 66
        },
        {
          "source": "MED",
          "id": "17296176",
          "citationType": "journal article",
          "title": "Eye movements and smart technology.",
          "authorString": "Freksa C, Bertel S.",
          "journalAbbreviation": "Comput Biol Med",
          "pubYear": 2007,
          "volume": "37",
          "issue": "7",
          "pageInfo": "983-988",
          "citedByCount": 2
        },
        {
          "source": "MED",
          "id": "17199627",
          "citationType": "journal article",
          "title": "Visual attention and expertise for forensic signature analysis.",
          "authorString": "Dyer AG, Found B, Rogers D.",
          "journalAbbreviation": "J Forensic Sci",
          "pubYear": 2006,
          "volume": "51",
          "issue": "6",
          "pageInfo": "1397-1404",
          "citedByCount": 17
        },
        {
          "source": "MED",
          "id": "17007804",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "Eye movement correlates of younger and older adults' strategies for complex addition.",
          "authorString": "Green HJ, Lemaire P, Dufau S.",
          "journalAbbreviation": "Acta Psychol (Amst)",
          "pubYear": 2007,
          "volume": "125",
          "issue": "3",
          "pageInfo": "257-278",
          "citedByCount": 31
        },
        {
          "source": "MED",
          "id": "16846967",
          "citationType": "journal article",
          "title": "Incentives improve performance on both incremental and insight problem solving.",
          "authorString": "Wieth M, Burns BD.",
          "journalAbbreviation": "Q J Exp Psychol (Hove)",
          "pubYear": 2006,
          "volume": "59",
          "issue": "8",
          "pageInfo": "1378-1394",
          "citedByCount": 6
        },
        {
          "source": "MED",
          "id": "17027779",
          "citationType": "comparative study; research support, non-u.s. gov't; journal article",
          "title": "Perceptual contributions to problem solving: Chunk decomposition of Chinese characters.",
          "authorString": "Luo J, Niki K, Knoblich G.",
          "journalAbbreviation": "Brain Res Bull",
          "pubYear": 2006,
          "volume": "70",
          "issue": "4-6",
          "pageInfo": "430-443",
          "citedByCount": 47
        },
        {
          "source": "MED",
          "id": "16822159",
          "citationType": "journal article",
          "title": "When shoes become hammers: Goal-derived categorization training enhances problem-solving performance.",
          "authorString": "Chrysikou EG.",
          "journalAbbreviation": "J Exp Psychol Learn Mem Cogn",
          "pubYear": 2006,
          "volume": "32",
          "issue": "4",
          "pageInfo": "935-942",
          "citedByCount": 13
        },
        {
          "source": "MED",
          "id": "16724770",
          "citationType": "research support, non-u.s. gov't; research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "The nature of restructuring in insight: an individual-differences approach.",
          "authorString": "Ash IK, Wiley J.",
          "journalAbbreviation": "Psychon Bull Rev",
          "pubYear": 2006,
          "volume": "13",
          "issue": "1",
          "pageInfo": "66-73",
          "citedByCount": 48
        },
        {
          "source": "MED",
          "id": "16610275",
          "citationType": "journal article",
          "title": "Effects of belief and logic on syllogistic reasoning: Eye-movement evidence for selective processing models.",
          "authorString": "Ball LJ, Phillips P, Wade CN, Quayle JD.",
          "journalAbbreviation": "Exp Psychol",
          "pubYear": 2006,
          "volume": "53",
          "issue": "1",
          "pageInfo": "77-86",
          "citedByCount": 25
        },
        {
          "source": "MED",
          "id": "16532856",
          "citationType": "research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "Question asking and eye tracking during cognitive disequilibrium: comprehending illustrated texts on devices when the devices break down.",
          "authorString": "Graesser AC, Lu S, Olde BA, Cooper-Pye E, Whitten S.",
          "journalAbbreviation": "Mem Cognit",
          "pubYear": 2005,
          "volume": "33",
          "issue": "7",
          "pageInfo": "1235-1247",
          "citedByCount": 12
        },
        {
          "source": "MED",
          "id": "16194960",
          "citationType": "research support, non-u.s. gov't; journal article",
          "title": "The strategic use of alternative representations in arithmetic word problem solving.",
          "authorString": "Thevenot C, Oakhill J.",
          "journalAbbreviation": "Q J Exp Psychol A",
          "pubYear": 2005,
          "volume": "58",
          "issue": "7",
          "pageInfo": "1311-1323",
          "citedByCount": 16
        },
        {
          "source": "MED",
          "id": "16026503",
          "citationType": "comparative study; research support, non-u.s. gov't; research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "Why won't you change your mind? Knowledge of operational patterns hinders learning and performance on equations.",
          "authorString": "McNeil NM, Alibali MW.",
          "journalAbbreviation": "Child Dev",
          "pubYear": 2005,
          "volume": "76",
          "issue": "4",
          "pageInfo": "883-899",
          "citedByCount": 58
        },
        {
          "source": "MED",
          "id": "15975944",
          "citationType": "validation study; journal article",
          "title": "Better without (lateral) frontal cortex? Insight problems solved by frontal patients.",
          "authorString": "Reverberi C, Toraldo A, D'Agostini S, Skrap M.",
          "journalAbbreviation": "Brain",
          "pubYear": 2005,
          "volume": "128",
          "issue": "pt 12",
          "pageInfo": "2882-2890",
          "citedByCount": 55
        },
        {
          "source": "MED",
          "id": "15673186",
          "citationType": "clinical trial; randomized controlled trial; journal article",
          "title": "The use of verbal protocols as data: an analysis of insight in the candle problem.",
          "authorString": "Fleck JI, Weisberg RW.",
          "journalAbbreviation": "Mem Cognit",
          "pubYear": 2004,
          "volume": "32",
          "issue": "6",
          "pageInfo": "990-1006",
          "citedByCount": 35
        },
        {
          "source": "MED",
          "id": "14736293",
          "citationType": "clinical trial; research support, non-u.s. gov't; randomized controlled trial; journal article",
          "title": "What makes an insight problem? The roles of heuristics, goal conception, and solution recoding in knowledge-lean problems.",
          "authorString": "Chronicle EP, MacGregor JN, Ormerod TC.",
          "journalAbbreviation": "J Exp Psychol Learn Mem Cogn",
          "pubYear": 2004,
          "volume": "30",
          "issue": "1",
          "pageInfo": "14-27",
          "citedByCount": 30
        },
        {
          "source": "MED",
          "id": "14736292",
          "citationType": "journal article",
          "title": "Multiple causes of difficulty in insight: the case of the nine-dot problem.",
          "authorString": "Kershaw TC, Ohlsson S.",
          "journalAbbreviation": "J Exp Psychol Learn Mem Cogn",
          "pubYear": 2004,
          "volume": "30",
          "issue": "1",
          "pageInfo": "3-13",
          "citedByCount": 55
        },
        {
          "source": "MED",
          "id": "12930477",
          "citationType": "research support, non-u.s. gov't; research support, u.s. gov't, non-p.h.s.; journal article",
          "title": "Eye movements and problem solving: guiding attention guides thought.",
          "authorString": "Grant ER, Spivey MJ.",
          "journalAbbreviation": "Psychol Sci",
          "pubYear": 2003,
          "volume": "14",
          "issue": "5",
          "pageInfo": "462-466",
          "citedByCount": 116
        },
        {
          "source": "MED",
          "id": "12915298",
          "citationType": "comparative study; research support, non-u.s. gov't; journal article",
          "title": "Acquiring an understanding of design: evidence from children's insight problem solving.",
          "authorString": "Defeyter MA, German TP.",
          "journalAbbreviation": "Cognition",
          "pubYear": 2003,
          "volume": "89",
          "issue": "2",
          "pageInfo": "133-155",
          "citedByCount": 71
        }
      ],
      "errors": [],
      "ncbi": {
        "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&linkname=pubmed_pubmed_citedin&id=11820744&retmode=json",
        "response_sha256": "0a499970bcaaca33afbef9791c51b8fa0e30035e780a8a0e9cee926c04ef2298",
        "linksets": [
          {
            "dbfrom": "pubmed",
            "ids": [
              "11820744"
            ],
            "linksetdbs": [
              {
                "dbto": "pubmed",
                "linkname": "pubmed_pubmed_citedin",
                "links": [
                  "42646013",
                  "40963791",
                  "40919409",
                  "40137068",
                  "39852414",
                  "39833601",
                  "39135748",
                  "38630293",
                  "38425554",
                  "38024571",
                  "37998674",
                  "37790727",
                  "37623545",
                  "37465144",
                  "37233335",
                  "36732422",
                  "36674221",
                  "36551064",
                  "36374909",
                  "36081729",
                  "35308608",
                  "35140344",
                  "34975690",
                  "32655713",
                  "31191410",
                  "31156488",
                  "31068884",
                  "30728789",
                  "30631294",
                  "30618985",
                  "30534097",
                  "30327635",
                  "30258378",
                  "30161187",
                  "30150953",
                  "30018576",
                  "29951753",
                  "29875645",
                  "29867650",
                  "29665228",
                  "29416518",
                  "29349507",
                  "29337998",
                  "29184525",
                  "28966603",
                  "28611702",
                  "28520866",
                  "28295482",
                  "28082928",
                  "27679592",
                  "27592343",
                  "27555833",
                  "27471485",
                  "26913018",
                  "26887867",
                  "26300794",
                  "26257683",
                  "26167155",
                  "25538658",
                  "25324804",
                  "24124515",
                  "23555020",
                  "23532591",
                  "23007629",
                  "22328466",
                  "22110327",
                  "21046365",
                  "19933457",
                  "18604964",
                  "18213368",
                  "17972730",
                  "16724770",
                  "16532856",
                  "15673186"
                ]
              }
            ]
          }
        ],
        "error": null
      }
    }
  },
  "coverage_notes": [
    "Raw returned records, not a date-filtered screened corpus. Publication years alone cannot validate the cutoff for every 2026 record.",
    "PubMed preprints and final articles may have distinct identifiers; 299 unique Europe PMC source/ID pairs are not 299 independent studies.",
    "Only the selected follow-up primary sources are date-checked and abstract-screened; other metadata are discovery/deferred records."
  ]
}
```


---

## File: CITATION_SCREENING_LOG.json

```json
{
  "date": "2026-09-30",
  "method": "15 priority/NCBI-only primary abstracts; selected follow-ups. Not dual screening or full screening of all returned metadata.",
  "abstract_query_template": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:{PMID}%20AND%20SRC:MED&format=json&resultType=core",
  "selected_records": [
    {
      "pmid": "32334091",
      "title": "Brain network dynamics during spontaneous strategy shifts and incremental task optimization.",
      "doi": "10.1016/j.neuroimage.2020.116854",
      "authors": "Allegra M, Seyed-Allaei S, Schuck NW, Amati D, Laio A, Reverberi C.",
      "firstPublicationDate": "2020-04-22",
      "primary_record_url": "https://europepmc.org/article/MED/32334091",
      "disposition": "included",
      "reason": "Selected author-PDF sections; shared-data and pre-correlation-state limits."
    },
    {
      "pmid": "37607820",
      "title": "Theta Signal Transfer from Parietal to Prefrontal Cortex Ignites Conscious Awareness of Implicit Knowledge during Sequence Learning.",
      "doi": "10.1523/jneurosci.2172-22.2023",
      "authors": "Lu Y, Guo X, Weng X, Jiang H, Yan H, Shen X, Feng Z, Zhao X, Li L, Zheng L, Liu Z, Men W, Gao JH.",
      "firstPublicationDate": "2023-08-22",
      "primary_record_url": "https://europepmc.org/article/MED/37607820",
      "disposition": "included provisional",
      "reason": "Primary abstract/excerpts only; failed full XML; intervention controls unverified."
    },
    {
      "pmid": "40097186",
      "title": "Ventral Tegmental Area Dopamine Neural Activity Switches Simultaneously with Rule Representations in the Medial Prefrontal Cortex and Hippocampus.",
      "doi": "10.1523/jneurosci.1670-24.2025",
      "authors": "Ding M, Tomsick PL, Young RA, Jadhav SP.",
      "firstPublicationDate": "2025-09-10",
      "primary_record_url": "https://europepmc.org/article/MED/40097186",
      "disposition": "included",
      "reason": "Relevant primary XML Methods/Results; Gaussian smoothing and small sample explicit."
    },
    {
      "pmid": "23526396",
      "title": "Temporal dynamics of mental impasses underlying insight-like problem solving.",
      "doi": "10.1007/s11427-013-4454-8",
      "authors": "Shen W, Liu C, Yuan Y, Zhang X, Luo J.",
      "firstPublicationDate": "2013-03-23",
      "primary_record_url": "https://europepmc.org/article/MED/23526396",
      "disposition": "excluded from core",
      "reason": "Primary abstract: impasse formation ERPs, not a solution-progress trajectory through impasse."
    },
    {
      "pmid": "36081729",
      "title": "Differences in the distribution of attention to trained procedure between finders and non-finders of the alternative better procedure.",
      "doi": "10.3389/fpsyg.2022.934029",
      "authors": "Ninomiya Y, Terai H, Miwa K.",
      "firstPublicationDate": "2022-08-23",
      "primary_record_url": "https://europepmc.org/article/MED/36081729",
      "disposition": "included",
      "reason": "Relevant primary XML; pre-expression gaze, no inferred smooth ramp; exclusions/equivalence bounds explicit."
    },
    {
      "pmid": "30814311",
      "title": "Medial Prefrontal Cortex Population Activity Is Plastic Irrespective of Learning.",
      "doi": "10.1523/jneurosci.1370-17.2019",
      "authors": "Singh A, Peyrache A, Humphries MD.",
      "firstPublicationDate": "2019-02-27",
      "primary_record_url": "https://europepmc.org/article/MED/30814311",
      "disposition": "included provisional",
      "reason": "Primary abstract; nonspecific plasticity counterexample, not neural solution ramp."
    },
    {
      "pmid": "33531416",
      "title": "Coordinated Prefrontal State Transition Leads Extinction of Reward-Seeking Behaviors.",
      "doi": "10.1523/jneurosci.2588-20.2021",
      "authors": "Russo E, Ma T, Spanagel R, Durstewitz D, Toutounji H, K\u00f6hr G.",
      "firstPublicationDate": "2021-02-02",
      "primary_record_url": "https://europepmc.org/article/MED/33531416",
      "disposition": "included provisional",
      "reason": "Primary abstract; extinction temporal Methods unchecked."
    },
    {
      "pmid": "40569931",
      "title": "N2 sleep promotes the occurrence of 'aha' moments in a perceptual insight task.",
      "doi": "10.1371/journal.pbio.3003185",
      "authors": "L\u00f6we AT, Petzka M, Tzegka MM, Schuck NW.",
      "firstPublicationDate": "2025-06-26",
      "primary_record_url": "https://europepmc.org/article/MED/40569931",
      "disposition": "background",
      "reason": "Primary abstract: sleep EEG/stage association with later insight, not decoded content progressing through impasse; full Methods unchecked."
    },
    {
      "pmid": "12930477",
      "title": "Eye movements and problem solving: guiding attention guides thought.",
      "doi": "10.1111/1467-9280.02454",
      "authors": "Grant ER, Spivey MJ.",
      "firstPublicationDate": "2003-09-01",
      "primary_record_url": "https://europepmc.org/article/MED/12930477",
      "disposition": "background",
      "reason": "Primary abstract: diagram fixations and visual cue intervention; no verified uninterrupted individual progress trajectory."
    },
    {
      "pmid": "38405946",
      "title": "Cost-benefit Tradeoff Mediates the Rule- to Memory-based Processing Transition during Practice.",
      "doi": "10.1101/2024.02.13.580214",
      "authors": "Yang G, Jiang J.",
      "firstPublicationDate": "2024-10-24",
      "primary_record_url": "https://europepmc.org/article/MED/38405946",
      "disposition": "deferred final Methods",
      "reason": "Primary preprint abstract; practice/cost-benefit selection alternative; final PMID39847600 already indexed; do not count as independent studies."
    },
    {
      "pmid": "39314386",
      "title": "Practice Reshapes the Geometry and Dynamics of Task-tailored Representations.",
      "doi": "10.1101/2024.09.12.612718",
      "authors": "Kikumoto A, Shibata K, Nishio T, Badre D.",
      "firstPublicationDate": "2024-09-15",
      "primary_record_url": "https://europepmc.org/article/MED/39314386",
      "disposition": "excluded from core",
      "reason": "Primary preprint abstract: routine practice EEG geometry, not specified impasse/sudden strategy discovery; final PMID40882180 in index."
    },
    {
      "pmid": "39314328",
      "title": "Ventral tegmental area dopamine neural activity switches simultaneously with rule representations in the prefrontal cortex and hippocampus.",
      "doi": "10.1101/2024.09.09.611811",
      "authors": "Ding M, Tomsick PL, Young RA, Jadhav SP.",
      "firstPublicationDate": "2025-02-11",
      "primary_record_url": "https://europepmc.org/article/MED/39314328",
      "disposition": "duplicate publication family",
      "reason": "Primary preprint abstract; use final Ding2025, not a separate replication."
    },
    {
      "pmid": "38370807",
      "title": "Neural signatures of opioid-induced risk-taking behavior in the prelimbic prefrontal cortex.",
      "doi": "10.1101/2024.02.05.578828",
      "authors": "Quave CB, Vasquez AM, Aquino-Miranda G, Mar\u00edn M, Bora EP, Chidomere CL, Zhang XO, Engelke DS, Do-Monte FH.",
      "firstPublicationDate": "2024-12-23",
      "primary_record_url": "https://europepmc.org/article/MED/38370807",
      "disposition": "excluded from core",
      "reason": "Primary preprint abstract: opioid-related risk/conflict group activity; not specified pre-breakthrough dynamics; final PMID40097184 indexed."
    },
    {
      "pmid": "40027783",
      "title": "Rhythmic modulation of dorsal hippocampus across distinct behavioral timescales during spatial set-shifting.",
      "doi": "10.1101/2025.02.19.639177",
      "authors": "Bottoms M, Miles JT, Mizumori SJY.",
      "firstPublicationDate": "2025-02-20",
      "primary_record_url": "https://europepmc.org/article/MED/40027783",
      "disposition": "deferred preprint lead",
      "reason": "Primary abstract reports hippocampal rhythmic changes during switching. Preprint status and timing/analysis unresolved; do not use as verified core evidence."
    },
    {
      "pmid": "30618985",
      "title": "Unconditional Perseveration of the Short-Term Mental Set in Chunk Decomposition.",
      "doi": "10.3389/fpsyg.2018.02568",
      "authors": "Huang F, Tang S, Hu Z.",
      "firstPublicationDate": "2018-12-11",
      "primary_record_url": "https://europepmc.org/article/MED/30618985",
      "disposition": "excluded from core",
      "reason": "Primary abstract: trained mental-set accuracy/RT across conditions, not within-impasse hidden progress."
    }
  ],
  "unselected_records": "deferred/title-level discovery only, not evidence or adjudicated exclusions",
  "web_queries": [
    {
      "service": "web search",
      "date": "2026-09-30",
      "exact_queries": [
        "site.pubmed.ncbi.nlm.nih.gov \"Medial prefrontal cortex predicts internally driven strategy shifts\"",
        "site.ncbi.nlm.nih.gov \"pubmed_pubmed_citedin\" cited by citations",
        "site.europepmc.org REST citations API",
        "\"Theta Signal Transfer\" \"2023\" precuneus",
        "\"Brain network dynamics during spontaneous strategy shifts\" Allegra",
        "\"Europe PMC\" \"citation data\" \"Crossref\""
      ],
      "purpose": "Resolve anchor PMID, primary API documentation, and author text for selected indexed leads."
    }
  ],
  "web_reader_access_failures": [
    "Europe PMC REST/help open returned 403; primary help was available in indexed text.",
    "Direct PubMed/PMC web opens for selected follow-ups returned empty pages or access checks. Primary abstracts were instead retrieved through Europe PMC core search."
  ]
}
```


---

## File: CITATION_INDEX_AUDIT.md

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


---

## File: CITATION_RETRIEVAL_ATTEMPTS.json

```json
{
  "retrieved_at_utc": "2026-09-30T23:26:44.172235+00:00",
  "note": "Follow-up full-text requests after indexed discovery; only relevant sections read as described in the ledger. Existing download cache manifest is unchanged.",
  "attempts": [
    {
      "id": "PMC10552945",
      "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10552945/fullTextXML",
      "status": "failed",
      "error": "500 Server Error:  for url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10552945/fullTextXML"
    },
    {
      "id": "PMC12424963",
      "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12424963/fullTextXML",
      "status": "retrieved",
      "sha256": "ecd77ab5641171ead4436619ee55ff3751d5a02d913cc18112231b99d03dbfe8"
    },
    {
      "id": "PMC9447375",
      "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9447375/fullTextXML",
      "status": "retrieved",
      "sha256": "00333237aba8649caad82d0d1756cfae36699cb598b389b20e83cf8f80555f77"
    }
  ]
}
```


---

## File: citation_index_audit.py

```python
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
```


---

## File: FRESH_DISCOVERY_TEMPLATE.md

# Fresh discovery template

For substantial literature research. Complete the brief before searching; freeze the discovery record before revealing the existing synthesis. This is a search for complementary evidence, not a competing polished answer or a guarantee of exhaustive coverage.

## Neutral brief to provide

> Research question: [original question, without the existing answer or selected papers].
>
> User constraints, populations/tasks, cutoff date, language and intended use: [fill].
>
> Declared scope/stopping bound: [fill; do not claim saturation from this bound].
>
> Search primary literature for materially different explanations, supporting, opposing and null findings. Choose routes from the question. Include overlooked populations, developmental groups/species, measures and timescales when relevant. Do not read the existing draft, chosen bibliography, ledger or reviewer omission lists before saving your discovery output. If you encounter them accidentally, record that exposure.
>
> Return a short candidate map, measured variables and generalization limits, contrary findings, exact queries/citation routes, identifiers, inspection depth and access failures. Verify author/title/publication version and DOI/PMID/URL against a primary record; keep unresolved identities as unverified leads. Distinguish findings, inference, analogy and unknowns. Do not call earlier activity useful progress without evidence of relevance, or treat a matching model as a measured biological mechanism.
>
> Save the brief, candidate map and search log before seeing the existing draft. Report the declared bound, actual yield, residual gaps and why you stopped. A no-new-lead result is valid. Do not invent search or reading history.

Adapt the last subject-specific examples to the question; source-checking and uncertainty rules apply to every task.

## Context and freeze record

- Inquiry/date/cutoff:
- Researcher/model/settings (unknown is acceptable):
- Status: fresh context / already-exposed exploratory search / externally supplied output with unknown exposure:
- Exact brief and visible materials:
- Existing draft/bibliography/ledger withheld:
- Accidental exposure and impact:
- Search scope/bound declared before searching:
- Saved output and search-log paths:
- Timestamp and output SHA256, or unavailable:
- External-output provenance that was not supplied:

A separate researcher with deliberately limited context can reduce anchoring. It does not establish independence between models' training data or a controlled experimental comparison. Do not call a same-conversation second pass fresh.

## Candidate map and source checks

| Candidate | Discovery route/query | Author/title/version/DOI or PMID match | Task/species/measure/timescale | Potential relevance or counterevidence | Inspection depth/access | Uncertainty |
|---|---|---|---|---|---|---|

Record exact engine/database, filters and query/citation URLs in the accompanying SEARCH_LOG. Preserve empty searches, access failures and mistaken identity mappings. Distinguish preprint/final versions and papers using the same data.

## Reconcile only after freezing discovery

| Candidate | Existing/new/duplicate/background/excluded/deferred | Reason and changed coverage | Primary verification completed | Current claim limit | Next check/owner/status |
|---|---|---|---|---|---|

Prioritize leads that could change the conclusion. Retain rejected/deferred leads with reasons; a candidate is not automatically a report finding. Display reading depth at the point of use. Do not let a smooth narrative erase contradictions.

## Outcome and handoff

- Added evidence, missing populations/measures, alternative mechanisms or contradictions:
- Citation corrections and false positives:
- No-new-evidence result, if applicable:
- Search/verification cost, if known:
- Remaining gaps and stopping reason:
- Reconciled report, ledger and notebook main sections:
- Short plain-language answer plus technical evidence:
- Later critic pass and its independence/status:

One paired answer cannot establish that this workflow causes better accuracy. For a performance claim, hold model/question/tools/budget fixed, compare across several questions and use blinded checks of citation precision, consequential omissions, unsupported claims, clarity and cost.


---

## File: LITERATURE_AUDIT_TEMPLATE.md

# Literature audit template

Copy into each substantial literature investigation and fill while working. Mark unavailable fields explicitly; do not reconstruct missing history as contemporaneous evidence.

## Scope and competing explanations

- Question and cutoff date:
- Focused assessment or systematic review:
- Inclusion/exclusion criteria:
- Coverage map (population, task, measure, timescale, mechanism):
- Anchors and why selected:
- Supporting, opposing and null findings sought:

## Fresh discovery and context record

Complete before showing the discovery researcher the existing draft. Use [FRESH_DISCOVERY_TEMPLATE.md](FRESH_DISCOVERY_TEMPLATE.md).

- Exact neutral brief, constraints/cutoff and declared search bound:
- Researcher/model/settings, or unknown:
- Fresh context, already-exposed search, or externally supplied output with unknown exposure:
- Visible/withheld material and accidental exposure:
- Preserved output/search log, timestamp/hash and missing provenance:
- Primary author/title/version/identifier checks and unresolved mappings:

## Reconciliation after freezing discovery

| Candidate and route | Same primary study/version confirmed? | Existing/new/duplicate/background/excluded/deferred | What it adds or contradicts | Reading depth | Verification or next check |
|---|---|---|---|---|---|

- New relevant studies, species/developmental groups, measures and mechanisms:
- Consequential omissions and false/unsupported leads:
- Remaining leads, access gaps, cost if known and reason for stopping:
- Existing synthesis revised, or no-new-evidence outcome recorded:
- Independence limitations; no uncontrolled workflow-performance claim:

## Search and selection log

| Batch/date | Engine/database and filters | Exact query or citation route | Candidates (DOI/PMID/URL) | Keep/drop/defer and reason | Access/result |
|---|---|---|---|---|---|

## Citation audit

| Anchor | Backward references checked | Forward service/date checked | New candidates/decision | Limitations |
|---|---|---|---|---|

## Claim extraction

| Claim/study | Population/task | Actual measure and resolution | Result and alternative explanations | Verification: sections/pages/figures or abstract only | Generalization |
|---|---|---|---|---|---|

## Retrieval reconciliation

- Declared source list and stable identifiers:
- Script/manifest version and historical differences:
- Cached repeat-run check and result:
- Refresh/attempt history and changed hashes:
- Extraction failures and visual checks:

## Stopping decision

- Final batch/citation-route yield:
- New evidence affecting conclusions:
- Remaining unfilled coverage and unresolved relevant candidates:
- Reason for stopping (demonstrated diminishing returns, scope, time, access):
- Conditions for reopening:

## Critic response

- Reviewer and independence, or clearly labelled self-check:
- Materials provided and checks performed:

| Criticism | Primary verification | Accept/qualify/reject/unresolved | Action | Rechecked/status |
|---|---|---|---|---|

## Handoff

- Plain-language opening and technical evidence/limitations:
- Notebook main sections reconciled and historical entries labelled:
- Report, fresh-discovery/reconciliation records, search/selection log, evidence/access ledger, notebook and exclusions included:
- Version, date, change log and publication status:
- Experiments run versus proposed:
- Remaining material limitations:


---

## File: DISCOVERY_RECONCILIATION.md

# Discovery reconciliation — method addition, version 2.2

30 September 2026. This applies the reconciliation portion to the already-received fresh Opus answer. It is **retrospective**, not a claim that the new prospective workflow generated that answer. The exact received text and SHA256 are preserved locally; the user reported a fresh run without our workflow. Its original prompt, settings, search/reading logs and prior exposure were not supplied.

Frozen received-text SHA256: `1e5ef4b0674a004ada6d7e6516f535db9c30024f435ed68c18ee213a84a1e5d6`. Baseline: [published v2.1](https://github.com/jorgy72/hidden-progress-insight-research/tree/b297a0aa3dbb26cc81aeeeb2061d53b145a5af19). Primary spot-checks were completed in the preceding comparison turn. This method update performs no further literature search or reading-depth upgrade. Version 2.1's report and ledger remain the scientific synthesis; these candidates have not been silently added as fully verified findings.

| Candidate | Primary identity and actual inspection | Classification and coverage added | Outstanding next check |
|---|---|---|---|
| [Siegler & Stern 1998](https://pubmed.ncbi.nlm.nih.gov/9857493/) | Primary abstract checked; arithmetic response times and verbal strategy reports. | New relevant developmental/implicit-expression lead. | Inspect full trial-level Methods and condition-specific results; the five-trial/80% result depends on relevant problems every trial. |
| [Stephen, Dixon & Isenhower 2009](https://pubmed.ncbi.nlm.nih.gov/19968438/) | Primary abstract checked; action dynamics during gear problem solving. | New behavioural-measure/early-warning lead. | Inspect entropy estimation, alignment and intervention controls; distinguish changing dynamics from useful solution content. |
| [Pasupathy & Miller 2005](https://pubmed.ncbi.nlm.nih.gov/15729344/) | Primary abstract checked; monkey PFC/striatal associative-learning activity. | New primate/region-timing lead that challenges an overly uniform PFC-switch account. | Inspect individual neural/behavioural trajectories and time resolution; task is associative learning, not verified conscious insight. |
| [Wirth et al. 2003](https://pubmed.ncbi.nlm.nih.gov/12791995/) | Primary abstract checked; monkey hippocampal selectivity around learning. | New primate timing lead; before/with/after changes reported. | Original temporal Methods/results needed to verify the fresh claim of gradual change; its bibliography linked a review. |
| [Bissonette & Roesch 2015](https://pubmed.ncbi.nlm.nih.gov/26500516/) | Relevant primary XML Methods/Discussion checked. Fresh answer attributed its rat mPFC finding to Jang. | New relevant rat rule-encoding lead and confirmed attribution correction. | Inspect full Results/figures and criterion/alignment analyses before a core evidence row. Preserve the original misattribution. |
| [Kumar et al., Do Mice Grok?](https://arxiv.org/abs/2411.03541) | Primary preprint abstract checked. | New adjacent overtraining lead: biological-data reanalysis plus artificial model. | Verify full reanalysis, dataset dependence and venue/version. Separate neural decoding after mastery from pre-insight dynamics. |
| [Ellis et al. 2011](https://doi.org/10.1016/j.concog.2010.12.007) | Existing limited-reading row; fresh DOI instead resolved to [Murray et al. 2022](https://pubmed.ncbi.nlm.nih.gov/37465144/). | Existing evidence with confirmed wrong-link correction, not new replication. | Full original Methods remain to be audited; the link correction does not upgrade reading depth. |
| Gallistel 2004; Wagner 2004/sleep follow-ups; Bowden 2003; Schaeffer 2023 | Leads identified in the supplied answer; detailed assertions not checked in this bounded comparison. | Deferred behavioural/methodological routes. Bowden 2003 is distinct from our 1998 anchor. | Resolve primary identities, relevance and reading depth before using specific numbers or replication claims. |

## Follow-up feedback and its limits

The user supplied a further Opus response accepting the Ellis link error, Bissonette/Jang attribution error and overgeneralization. Those concessions agree with the earlier primary checks; they do not replace them. Its coverage assessment is reasonable: the fresh answer added different strata while missing Rose/Townsend and other studies retained in our report. Its readability judgment is reviewer feedback rather than an objective metric.

Two explanations remain unverified: that absence of a reading record caused the citation errors, and that this workflow caused greater accuracy. The supplied output alone cannot establish its unseen execution or a causal workflow effect. Nor is a missing study necessarily harmless: consequential omissions can change a conclusion. Both citation mappings and coverage deserve checking.

## Adopted action and residual gap

Added a neutral, bounded discovery pass before exposure to the existing synthesis, with context disclosure, saved output/search history and candidate reconciliation. Kept primary author/title/version/identifier checks and actual inspection levels. The later critic pass remains a separate step. The short plain-language opening remains mandatory.

This addition is now operational in [WORKFLOW.md](WORKFLOW.md) and [the reusable template](FRESH_DISCOVERY_TEMPLATE.md). The unresolved leads above reopen developmental, primate and movement-dynamics coverage for a future substantive audit; this document does not claim that audit is complete. A controlled model/tool/budget-matched evaluation across several questions would be needed to estimate the method's benefit and cost.
