# Hidden progress before insight: complete research handoff

Prepared 2026-09-30. Start with FULL_RESEARCH.md: it contains the entire report, evidence ledger, inquiry notebook, experiment proposal, source manifest and retrieval script in one file.

This is a focused literature assessment, not an exhaustive systematic review. No new biological experiment was run. Source access limitations and failed retrievals are retained. Neural-network grokking is explicitly separated from biological evidence.

## For another model

Read FULL_RESEARCH.md in full. Audit the claims against the linked primary studies. Distinguish measurements from interpretations; distinguish solution-specific gradual progress, nonspecific precursors, abrupt sampled-population transitions, latent knowledge and artificial-system analogy. Pay particular attention to individual versus averaged trajectories, measurement filtering, causal evidence and generalization. Identify errors or unsupported claims before extending the proposed experiment. Source retrieval code is provided for reproducibility and should be reviewed before running; some sources may remain inaccessible.

## Contents

- REPORT.md: full research answer with specific-study citations and limitations.
- EVIDENCE_LEDGER.md: source-by-source measurements, findings, categories and access audit.
- LAB_NOTEBOOK.md: competing hypotheses, revisions, exclusions, uncertainty and stopping decision.
- NEXT_EXPERIMENT.md: proposed discriminating experiment; not executed.
- source_manifest.json: retrieval provenance, hashes and failed attempts. Paths identify locally retained source files, which are not included in this handoff.
- fetch_sources.py: optional retrieval/extraction script. Dependencies: Python 3, requests, pypdf. It writes a sources directory and appends retrieval records when run.
- FULL_RESEARCH.md: all the above as one self-contained text document.
- FILE_HASHES.json: integrity hashes for this handoff.

Third-party full papers are linked rather than rehosted. Unrelated prior lab work and private workspace history are outside this inquiry package.


---

## Full report

# Hidden progress before insight and abrupt strategy change

Prepared: 2026-09-30

Research question: During the stuck period before a sudden insight or abrupt strategy change, is there evidence of gradual, measurable change in the brain or behaviour, or is the transition abrupt at the neural level as well? Consider human and animal studies; specify measurements and generalization; separate direct evidence from analogy; end with unknowns and a discriminating experiment.

This is a focused, source-audited literature assessment, not a systematic review or a new biological experiment. The proposed experiment has not been run.

**Yes: measurable change can occur while someone appears stuck, before an abrupt insight or strategy change. But some transitions are also abrupt in the recorded neural population.** The evidence supports several mechanisms, sometimes operating together, rather than one universal “insight process.”

The crucial distinction is between:

- **Gradual progress:** solution-relevant information changes progressively.
- **A precursor:** something changes before the breakthrough, without demonstrating continuous progress toward the answer.
- **Latent knowledge:** useful information is already acquired but ordinary performance conceals it.
- **A neural transition:** the currently expressed population activity changes rapidly.

A precursor alone does not establish hidden progress; an abrupt neural transition does not rule out earlier learning elsewhere.

**Human behaviour provides direct evidence of gradual, partly hidden progress.**

1. **Eye movements can reveal partial solution knowledge before the answer is reported.** [Ellis, Glaholt & Reingold (2011)](https://doi.org/10.1016/j.concog.2010.12.007) presented five letters: four forming an anagram solution and one distractor. They measured viewing time on each letter. Several seconds before the response, attention to the distractor declined **gradually** relative to solution letters—even on trials participants described as insightful.

   **Scope:** direct evidence of a solution-relevant behavioural precursor in this anagram task. Gaze measures attention, not the complete answer; aggregated trajectories cannot establish that every individual trial contained a smooth buildup.

2. **Gradual and sudden trajectories can coexist within the same puzzle.** [Bilalić et al. (2021; published online in 2019)](https://doi.org/10.1080/13546783.2019.1705912) recorded eye movements during matchstick arithmetic and collected ratings of suddenness, surprise and other “Aha” dimensions. Among 26 solvers who solved the restructuring problem before hints, independently judged gaze trajectories included approximately **54% incremental and 27% sudden** patterns. Earlier attention to the crucial element was associated with a less sudden subjective solution.

   **Scope:** evidence against assuming that all restructuring is abrupt—or that all apparent insight conceals the same gradual process. It concerns particular puzzles and coarse gaze trajectories classified by observers, not neural activity.

3. **Solution-related information can be accessible while the problem remains unsolved.** [Bowden & Beeman (1998)](https://doi.org/10.1111/1467-9280.00082) let participants attempt verbal association problems, then presented solution or unrelated words. They measured naming latency and solution recognition. Even after unsuccessful attempts, solution words showed facilitation, particularly when initially presented to the left visual field, which preferentially projects to the right hemisphere.

   **Scope:** evidence of partial semantic accessibility without successful answer generation. This was a probe after an attempt, **not a measured ramp**, and does not establish that those unsolved problems would subsequently produce spontaneous insight.

The classic evidence for *subjective* suddenness remains relevant: [Metcalfe & Wiebe (1987)](https://doi.org/10.3758/BF03197722) collected perceived closeness-to-solution ratings at 15-second intervals. These increased less incrementally for insight problems than for algebra/noninsight problems. That establishes limited introspective access to progress in those tasks; it does not demonstrate an unchanged brain.

**Human neural evidence includes both earlier changes and a fast event near solution.**

| Specific study | What was actually measured and found | Generalization and limitation |
|---|---|---|
| **[Rose, Haider & Büchel, 2010](https://doi.org/10.1093/cercor/bhq025)** | Participants performed colour comparisons containing a hidden response regularity. An abrupt reaction-time decrease indicated discovery. In the preceding **ten trials**, task-specific BOLD activity increased in ventral striatum/right ventrolateral prefrontal cortex; a separate EEG experiment found increased inter-electrode coherence, including gamma frequencies. | Relatively direct evidence that neural processing changes before abrupt explicit rule use. But comparisons between time windows establish an **earlier change**, not monotonic accumulation throughout the whole preceding period. Small samples and the operational timing of awareness limit precision. |
| **[Schuck et al., 2015](https://doi.org/10.1016/j.neuron.2015.03.015)** | People initially responded using stimulus position; an unnoticed colour–response relationship later offered another strategy. Multivariate fMRI detected colour information in medial prefrontal cortex in two blocks—about **five minutes**—before behavioural switching. Eleven of 36 participants spontaneously adopted the colour strategy. | Strong evidence that information useful for a future strategy can be represented before that strategy is expressed. Blockwise BOLD decoding cannot determine whether each person’s neural change was smooth or stepwise. This was spontaneous strategy discovery during successful performance, not a verified classic puzzle impasse. |
| **[Jung-Beeman et al., 2004](https://doi.org/10.1371/journal.pbio.0020097)** | During verbal remote-associate solving, response-aligned EEG showed a right temporal **~39-Hz burst beginning ~0.3 seconds before the solution button press**. It was preceded by posterior alpha enhancement approximately **1.4–0.4 seconds** before the response. Separate fMRI implicated right anterior superior temporal cortex. | Evidence of a fast solution-associated neural event plus an earlier precursor. Alpha was interpreted as attentional gating; it did not decode accumulating answer content. Button-press time is not exact awareness onset, and averaged scalp signals do not prove a discrete whole-brain transition on every trial. |
| **[Kounios et al., 2006](https://doi.org/10.1111/j.1467-9280.2006.01798.x)** | EEG and fMRI activity **before the problem appeared** differed depending on whether the subsequent solution was reported as insightful or analytic. | Evidence that preparatory brain state influences solving mode. Because the problem had not appeared, this cannot demonstrate progress toward its particular solution. It is a useful warning against calling every early neural difference “hidden progress.” |

Thus, **neural precursors are well supported in selected human tasks; a continuous, solution-specific neural buildup throughout a verified impasse is less firmly established.** The strongest findings above concern different pieces of that claim.

**Animals provide direct evidence about learning and strategy transitions, but cannot report the human “Aha” experience.**

| Specific study | What was actually measured and found | Generalization and limitation |
|---|---|---|
| **[Durstewitz et al., 2010](https://doi.org/10.1016/j.neuron.2010.03.029)** | Simultaneous recordings from rat medial prefrontal neurons during rule learning/set shifting. Trial-by-trial ensemble trajectories often underwent **abrupt transitions between distinct, lasting states**, closely related to behavioural performance shifts. | Direct evidence that a measured neural population can change abruptly during acquisition of a new rule. Calling this an animal insight is an interpretation. It does not show that synapses, other regions, or earlier evidence accumulation were unchanged. |
| **[Karlsson, Tervo & Karpova, 2012](https://doi.org/10.1126/science.1226518)** | Rat medial prefrontal ensemble activity during changed environmental contingencies. Abandonment of the previous strategy accompanied coordinated, abrupt activity changes; increased neural volatility then diminished during exploration. | Direct evidence of an abrupt neural reset associated with strategy abandonment. Crucially, this marks **entry into uncertainty/exploration**, rather than necessarily discovery of the correct answer. “Belief change” is inferred from task behaviour. |
| **[Siniscalchi et al., 2016](https://doi.org/10.1038/nn.4342)** | Two-photon calcium imaging of mouse secondary motor cortex, alongside licking choices. Switching into sound-guided responding produced relatively abrupt ensemble transitions **before behavioural performance recovered**. Switching toward repetitive responding produced slower, delayed transitions. | Shows that neural and behavioural transition times can differ, and that transition direction matters even within one task. These were familiar sensorimotor mappings, not wholly novel creative solutions. Calcium filtering and fitted transition definitions constrain timing. |
| **[Kuchibhotla et al., 2019](https://doi.org/10.1038/s41467-019-10089-0)** | Discrimination performance in mice, rats and two ferrets, comparing reinforced trials with probes omitting reinforcement. Animals could discriminate substantially better in probes before ordinary reinforced performance reached expertise. | Direct evidence that **poor performance can conceal acquired knowledge**, across several tasks/species; ferret evidence was especially small. It does not establish gradual neural accumulation: biological neural weights were not recorded, and the accompanying network model was explanatory modelling. |
| **[Drieu et al., 2025](https://doi.org/10.1038/s41586-025-08730-8)** | Mouse auditory go/no-go performance, knowledge probes, auditory-cortical calcium imaging and optogenetic silencing. A reward-prediction signal emerged within **tens of trials**; distinct action-suppression signals supported slower performance improvement. Silencing at relevant times impaired acquisition or expression. | Stronger mechanistic evidence that knowledge acquisition and behavioural improvement have distinguishable neural contributions. It concerns associative learning, not subjective insight or a verified impasse. Early reward predictions can also accompany mistakes, so neural change is not automatically progress toward a correct understanding. |

These studies establish that **abrupt neural switching, earlier acquisition and delayed behavioural expression are compatible**. They need not be competing explanations of the same stage.

**What follows from the evidence—and what remains an interpretation.**

An evidence-consistent account is that information or associations change first, while the old strategy continues controlling behaviour; a later transition changes which representation or policy is expressed. Conscious recognition may occur at another point. This is a **reasonable organizing inference**, not a demonstrated universal sequence.

Two measurement problems prevent a stronger conclusion:

- **Averages can disguise individual transitions.** Schuck et al.’s average behavioural curve appeared gradual, while individual strategy onsets were abrupt. Bilalić et al. explicitly found both individual trajectory types.
- **“Abrupt” is always relative to the measured variable and resolution.** A rapid firing-pattern change does not establish abrupt synaptic learning. Conversely, a smooth BOLD or calcium curve may reflect temporal filtering or differently timed individual jumps.

**Grokking is an analogy with a demonstrated artificial mechanism.**

[Nanda et al. (2023)](https://arxiv.org/abs/2301.05217) studied small transformers learning modular addition. They measured weights and activations across training, identified a Fourier-based algorithm, and tested it with ablations. Mechanistic progress measures revealed circuit formation before the conspicuous improvement in generalization, followed by removal of memorizing components.

That is direct evidence of hidden progress **in those artificial networks**. It demonstrates that performance can conceal changing internal mechanisms. It does not establish that human insight uses the same mechanism, or that biological neural transitions must be gradual.

I preserved the primary-source evidence, access limitations and exclusions in the [Evidence ledger](#evidence-ledger).

**What remains unknown is the prevalence and causal role of these different trajectories.** We cannot yet say how often a prolonged human impasse contains useful accumulation, unproductive exploration, an already learned but suppressed solution, or little relevant change. We also lack a general account linking synaptic change, population activity, strategy adoption and conscious awareness. Generalization from short laboratory tasks to days or months of scientific, artistic or personal insight remains uncertain.

**The experiment that would discriminate the explanations** would combine prospective content decoding, individual-trial modelling and causal intervention:

1. **Measure a real impasse continuously.** Use human puzzles and matched human/rodent rule-discovery tasks; record eye movements, choices and high-resolution neural activity. Separate repeated failure, subjective stuckness, knowledge and eventual strategy use.
2. **Decode the specific emerging solution independently.** Train decoders on separate known-solution/instructed-rule trials, then predict held-out discoveries. Decode incorrect alternatives too. A generic effort or arousal signal would not count as progress.
3. **Compare competing trajectories on individual trials.** Test gradual accumulation, discrete state switching, gradual acquisition followed by switching, and contextual gating. Include unsolved and false-insight trials; model filtering and avoid relying solely on solution-aligned averages.
4. **Test causality in animals.** Randomly interrupt a decoded precursor during poor performance, with matched movement, reward and arousal controls. Then assess later knowledge and transfer—not merely immediate accuracy. Separately perturb the transition itself.
5. **Predefine decisive outcomes.** A solution-specific ramp that predicts content and timing, whose interruption delays later acquisition, would support hidden accumulation. A discrete jump with sufficiently sensitive measurements excluding a meaningful prior ramp would support abrupt change in the sampled populations. A ramp in one circuit followed by a jump in another would support a hybrid mechanism.

This could settle the mechanism **for the tested tasks and measurement scale**. Establishing a general theory would require replication across task families; no finite recording could prove that every unobserved synapse remained unchanged.




---

## Evidence ledger

# Hidden progress before insight or strategy change

Focused primary-source assessment, 2026-09-30. This is not a systematic review or a new biological experiment. Initial hypotheses and revisions are in LAB_NOTEBOOK.md. Retrieval URLs, hashes and failed attempts are in source_manifest.json. Downloaded full texts remain local and are not rehosted in this package.

Evidence categories: G = graded solution-relevant behavioral change; P = neural/behavioral precursor without demonstrated continuous accumulation; J = abrupt measured neural/behavioral transition; L = latent knowledge revealed by context; A = artificial-system analogy. Categories can coexist.

| Study | Measurement and result | Category and boundary | Inspection |
|---|---|---|---|
| [Metcalfe & Wiebe 1987](https://doi.org/10.3758/BF03197722) | Warmth ratings at 15-second intervals; insight problems showed less incremental perceived approach than algebra/noninsight problems. | Subjective abruptness, not neural or objective absence of progress. | Full author PDF; methods text. |
| [Bowden & Beeman 1998](https://doi.org/10.1111/1467-9280.00082) | After up to 15 seconds of solving, naming/recognizing laterally presented solution words was facilitated even for unsolved verbal problems, especially left visual field/right hemisphere. | P: solution-related accessibility; no within-problem ramp or guarantee of later spontaneous solution. | Full author PDF. |
| [Ellis, Glaholt & Reingold 2011](https://doi.org/10.1016/j.concog.2010.12.007) | Gaze to a distractor consonant declined relative to solution consonants several seconds before anagram response, both with and without reported insight. | G: attention proxy; aggregate trajectories do not establish a ramp on every trial. | Primary abstract and publisher preview, not full methods. |
| [Bilalic et al. 2021; online 2019](https://doi.org/10.1080/13546783.2019.1705912) | Matchstick problem gaze and Aha dimensions; among 26 unhinted solvers, rated gaze patterns were 54% incremental and 27% sudden. Earlier relevant attention predicted lower perceived suddenness. | G/J: both patterns in one task; coarse bins and observer classification, not a neural measurement. | Full author PDF, individual-results section. |
| [Rose, Haider & Buchel 2010](https://doi.org/10.1093/cercor/bhq025) | Hidden final-response regularity in color comparisons; ventral striatal/right VLPFC BOLD and task-specific EEG coherence increased in ten trials before abrupt RT drop. | P: neural precursor; not a whole-impasse ramp. Transition/awareness operationalization and small samples matter. | Full author PDF; Fig. 3 rendered; EEG and behavioral methods. |
| [Schuck et al. 2015](https://doi.org/10.1016/j.neuron.2015.03.015) | fMRI color decoding in MPFC in two pre-switch blocks (~5 minutes); 11/36 people spontaneously used a newly predictive color strategy. | P: new-strategy content precedes output, but blockwise BOLD decoding cannot establish smooth accumulation. Authors distinguish strategy discovery from classic insight. | Full author PDF; Figs. 2–3 rendered. |
| [Jung-Beeman et al. 2004](https://doi.org/10.1371/journal.pbio.0020097) | Self-rated insight during remote associates; right temporal ~39-Hz EEG burst ~0.3 seconds before button press, posterior alpha enhancement ~1.4–0.4 seconds beforehand; separate fMRI temporal effect. | P/J: fast solution-associated event plus earlier state change. Neither exact conscious onset nor content ramp measured; primarily response-aligned averages. | Full PLOS HTML and PDF. |
| [Kounios et al. 2006](https://doi.org/10.1111/j.1467-9280.2006.01798.x) | Pre-problem EEG/fMRI states differed before later self-reported insight versus analytic solutions. | P only: preparatory disposition cannot be evidence of progress on an unseen problem. | Primary abstract. |
| [Durstewitz et al. 2010](https://doi.org/10.1016/j.neuron.2010.03.029) | Simultaneously recorded rat mPFC neurons during set shifting; trialwise ensemble trajectories often changed abruptly near behavioral rule acquisition. | J: direct neural strategy-transition evidence in sampled population; no animal Aha report or synaptic measurement. | Primary abstract; full publisher access failed. |
| [Karlsson, Tervo & Karpova 2012](https://doi.org/10.1126/science.1226518) | Rat mPFC ensemble activity after environmental changes; coordinated abrupt reset on abandoning a prior policy, followed by elevated volatility that declined during exploration. | J: onset of uncertainty/exploration, not necessarily solution acquisition. Internal belief is inferred from task/behavior. | Primary author-lab abstract. |
| [Siniscalchi et al. 2016](https://doi.org/10.1038/nn.4342) | Two-photon M2 calcium and licking choices in mice; abrupt ensemble transitions preceded recovery of sound-guided performance; action-only transitions were slower/delayed. | P/J: transition direction and task matter; familiar mapping retrieval differs from novel insight. Calcium and fitted transition thresholds limit timing. | Full author PDF and methods. |
| [Kuchibhotla et al. 2019](https://doi.org/10.1038/s41467-019-10089-0) | Reinforced versus unrewarded probe performance in mice/rats/two ferrets: discrimination was better in probes well before reinforced performance reached expertise. | L: direct acquisition/expression dissociation across tasks; neural network was a model, not recorded biological weights. Ferret evidence especially small. | Full primary XML. |
| [Drieu et al. 2025](https://doi.org/10.1038/s41586-025-08730-8) | Mouse auditory go/no-go probes, two-photon auditory cortical calcium, optogenetic silencing: reward prediction emerged within tens of trials; separate suppression signals supported slower performance gains. | P/L: causal regional/timing evidence for associative acquisition/expression, not a subjective impasse or proof of monotonic correct-solution progress. | Final author-hosted image PDF: first two pages rendered/read. Text extraction empty; final PMC index used as corroboration. |
| [Nanda et al. 2023](https://arxiv.org/abs/2301.05217) | Small transformers on modular addition: checkpoints, Fourier mechanism measures and ablations identified circuit formation before delayed generalization. | A: mechanism in artificial networks, no biological or phenomenological evidence. | Primary paper PDF and abstract. |

## Important exclusion and access limitations

[Graf et al. 2023](https://doi.org/10.3390/jintelligence11050086) is useful methodological material. Its footnote 2 states that the illustrated abrupt gaze data are simulated and that the original Bilalic data show a gradual shift. The simulated example is excluded from direct biological evidence. The empirical post-hint analysis is a separate result and not an independent sample from Bilalic.

The Drieu 2024 preprint (PMC11195094) was an initial lead; the final 2025 paper is the source used. Failed PMC/publisher requests and an unsuccessful Gallistel author-PDF download are retained. Gallistel is not required for the final claims; Schuck's own averaged-versus-individual behavior supplies the averaging example.

## Adjudication

Established within these tasks: graded behavioral precursors exist; task-related neural changes can precede abrupt output; sampled ensembles can switch rapidly; poor performance can conceal acquired task knowledge.

Inference: different combinations of acquisition, representation, selection, and report explain why sudden experience and slow precursor measures can coexist. This is a useful organizing framework, not a universal demonstrated circuit.

Speculation: continuous synaptic accumulation enables a metastable state switch or awareness threshold. Existing activity measurements do not uniquely identify this mechanism.

Unknown: how often each trajectory occurs; whether measured precursors are necessary and solution-specific; the time course of synaptic changes; generalization to prolonged real-world impasses; conscious experience in animals.

Stop criterion: selected primary studies now discriminate the broad hypotheses; more general searching has low information gain. Next work should be prospective single-trial model comparison or data reanalysis, rather than accumulating more anecdotes.


---

## Inquiry notebook

# Lab Notebook

Investigation started 2026-09-30.

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

Primary evidence adjudicated in EVIDENCE_LEDGER.md. Strong behavioral graded precursors: Ellis 2011 and Bilalic 2021. Human neural precursors: Rose 2010 and Schuck 2015, with coarse time resolution and limited generalization. Fast neural events/transitions: Jung-Beeman 2004, Durstewitz 2010, Karlsson 2012, Siniscalchi 2016. Latent task knowledge and causal acquisition/expression dissociation: Kuchibhotla 2019 and Drieu 2025. Nanda 2023 kept as artificial-system analogy.

## Failed Approaches

Source access and extraction failures are documented in the audit updates below and source_manifest.json. Search snippets count only as leads; full text preferred, abstract-only limitations explicit.

## Surprises / Anomalies

A prominent illustrated abrupt gaze trajectory was simulated, not empirical; an image-only PDF required visual inspection. See the audit update below.

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

Prospective solution-content decoding with independent training data, individual-trial ramp/change-point/hybrid model comparison, context/no-report/probe controls, and randomized closed-loop rodent perturbations. Full proposal: NEXT_EXPERIMENT.md. A new toy simulation would not adjudicate biological mechanisms and was not run.

## Confidence / Remaining Uncertainty

High that both hidden precursors and abrupt sampled-population transitions exist within these task families; moderate on a mixed organizing interpretation; low on prevalence or a universal neural mechanism. Unknown whether each precursor is causal/necessary, whether synaptic changes are continuous, and how results generalize to long natural impasses.

## Audit update, 2026-09-30

- Verified Schuck 2015: color decoding in MPFC in two 84-trial blocks (~5 minutes) before behavioral switch; small switching subset (11/36); blockwise decoding does not establish a smooth single-trial ramp.
- Verified Rose 2010: VLPFC/ventral striatal BOLD and task-specific EEG coherence changes in ten pre-transition trials; early neural change, not proof of monotonic learning throughout impasse.
- Important negative result: Graf et al. 2023 uses simulated data to illustrate its abrupt pre-solution shift (footnote 2). Do not treat that illustration as biological evidence of abrupt insight. Original Bilalic data show gradual change; inspect original.
- Drieu 2025 author-hosted PDF downloaded, but pypdf extracted no substantive text (36 image pages). Retain as scanned source; render and inspect rather than treating file presence as verification. Earlier PMC11195094 is a 2024 preprint, not the final 2025 article.
- Full-text access failures: PMC browser checks, some publisher access failures, Gallistel author PDF timeout. Alternative author/repository sources used where possible; failures preserved in source_manifest.json.

## Completed source audit, 2026-09-30

Final synthesis uses a focused selection of primary studies, not an exhaustive systematic review. Full text was inspected for the key human neural-precursor papers. Ellis 2011, Kounios 2006, Durstewitz 2010 and Karlsson 2012 were verified at primary-abstract/preview level; no unavailable sample sizes or detailed dynamics are asserted. Bilalic 2021 (online 2019) supplies empirical individual gradual and sudden gaze patterns. Drieu final 2025 PDF first two pages were rendered and read, including final abstract and acquisition/expression figure. No new biological experiment or causal claim about human insight was made. Sources, hashes, exclusions and proposed experiment are preserved. This snapshot includes only the present inquiry.


---

## Detailed experiment proposal

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


---

## Source retrieval manifest

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
    "error": "HTTPSConnectionPool(host='nemenmanlab.org', port=443): Max retries exceeded with url: /~ilya/images/5/5e/Gallistel-etal-04.pdf (Caused by ConnectTimeoutError(<HTTPSConnection(host='nemenmanlab.org', port=443)>, 'Connection to nemenmanlab.org timed out. (connect timeout=30)'))"
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

## Retrieval script

```python
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
```
