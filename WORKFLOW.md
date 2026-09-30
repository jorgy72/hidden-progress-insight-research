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

### Search provenance and coverage

- Define inclusion/exclusion criteria and a coverage map before searching: populations/species, tasks, measures, timescales, competing mechanisms, supporting and opposing findings. Search for each materially different explanation rather than following only the first promising papers.
- Maintain a structured SEARCH_LOG alongside the notebook. For each batch record the date, exact queries, search engine/database and filters, candidate identifiers/URLs, discovery route, inclusion/exclusion/defer reasons and access failures. Raw search results and download manifests supplement this log; they do not replace it. Mark retrospective reconstruction as retrospective, and unknown queries as unknown.
- Use available citation indexes (for example NCBI ELink citedin or Europe PMC citations) for forward retrieval; author-name web searches are only a fallback. Record complete returned-page retrieval separately from relevance screening; check publication dates and preprint/final duplicates before treating records as cutoff-qualified independent studies. Every index has coverage limits.
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
