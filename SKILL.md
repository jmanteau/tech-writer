---
name: tech-writer
description: Audit, write, and improve technical documentation with Plain Language (ISO 24495-1 and 24495-3 proxies, plus the unpublished ISO 24495-5 working draft) and Google's developer documentation style. Covers READMEs, guides, concept pages, API reference, CLI help, changelogs, migration guides, and reports, with noun-phrase headings and no AI writing tells.
when_to_use: When writing, auditing, or rewriting technical documentation, READMEs, reports, API reference, changelogs, or headings, even when no style guide is named
---

# Tech writer

Write for the reader's task. Start from who reads the page and what they must do next. Verify every fact against the code. Then apply the rules in severity order: structure before voice, voice before words.

## Core principle

**Write for the reader's task, not the product's feature list.** A developer reads docs to get something done. The prose must be precise, consistent, and plain enough to work read straight through, skimmed, or heard through a screen reader. Under ISO 24495-1, text must be relevant, findable, understandable, and usable.

- **Guidelines, not dogma.** Depart from a rule when that serves the reader better, for example when established domain terms are clearer. Stay consistent within the document.
- **Two layers.** Structure and content rules (headings, procedures, code samples, second person, active voice, timeless text, accessibility) apply in any language. Rules tagged `[EN]` (spelling, serial comma, contractions, the word list) apply to English only. Never translate a document unless asked.
- **No conformance claim.** The ISO rules here are proxies for the principles of ISO 24495-1, 24495-3, and 24495-5, not the standards' text. ISO 24495-5 is an unpublished working draft, so its rules are provisional.

## Precedence

When two rules conflict, the higher one wins:

1. **Technical accuracy.** Verified facts come first. Never alter code, logs, commands, or quoted output to satisfy a writing rule.
2. **The project's own style guide.** `CONTRIBUTING.md`, `STYLE.md`, `.vale.ini`, and the conventions the existing docs follow consistently.
3. **ISO 24495-3** for technical explanations.
4. **ISO 24495-1** for all prose.
5. **ISO 24495-5**, an unpublished working draft, for document design: heading depth, navigation, the opening block, and layout.
6. **Google's developer style**, then Merriam-Webster (spelling), the Chicago Manual of Style (general style), and the Microsoft Writing Style Guide (technical style).

Resolved conflicts:

- **Headings.** Concept headings are short noun phrases. Task headings over a procedure may be a bare imperative ("Create a webhook"). No sentence headings, no "What/How/Why" openers, no claims, no "-ing" openers.
- **Message headings.** The ISO 24495-5 draft asks for headings that state the section's message. For concept sections this skill keeps noun phrases, a deliberate departure. Task headings satisfy both.
- **Bold.** Bold lead-ins on explanatory bullets (ISO-1) and bold UI element names (Google). No other bold in prose. ISO-1 bolds the lead-in of every bullet. This skill bolds explanatory bullets only, so steps and short lists stay plain, a deliberate departure.
- **Sentence limits.** Average 15 to 20 words per sentence, none over 30. Paragraphs of 3 to 5 sentences, one topic each, and 4 sentences or fewer in a reply. Code blocks, commands, logs, and quotations are exempt (ISO-1 and ISO-3).
- **Structure.** ISO-3 progressive disclosure orders the body of concept pages, reference overviews, and code explanations inside the doc-type skeleton.

## Scoring

**Goal: 12/12.** The score is the number of Quick diagnostic rows passed: 12 rows, 1 point each, no partial credit. A row with no applicable content passes. The `[EN]` row passes automatically for a non-English document.

Bands: **11 to 12** ships as is. **8 to 10** needs word and voice edits only. **6 to 7** needs restructured sections, then a re-edit. **5 or less** needs a rewrite from the doc-type skeleton.

Blocking findings are a separate gate. Any one of them blocks shipping at any score: wrong or unverifiable facts, a procedure the reader cannot complete, or information that exists only in an image. An image without alt text counts too. Report the score, the failed rows, and the exact edits that reach 12/12.

## Framework

### 1. Reader and document job

**Core concept:** Every page serves one reader with one task. Name the audience, their level, and what they can do after reading. Then pick the document type that fits: tutorial (learn by doing), how-to (finish a task), concept (understand), reference (look up), or README (orient and start).

**Why it works:** Readers scan for their task. A page that mixes concept, procedure, and reference forces them to read everything to find anything.

**Key insights:**

- **Audience and scope.** Open with an audience statement and a scope statement plus a non-scope statement. The non-scope rescues readers who are on the wrong page.
- **Prerequisites first.** "Before you begin" lists prerequisites before step 1, not inside step 4 (convention).
- **Key points first.** The page or reply opens with the answer or main point, with no pleasantries. The introduction states what the reader gets, not the product's history. Open each paragraph with its main point.
- **Verification and next steps.** Every procedural page ends with a check ("Confirm that...") and "What's next" (convention).
- **Primary audience.** When a document has several audiences, name the primary one and let its needs settle conflicts. A runbook serves the engineer running it at 3 a.m. before the manager who audits it later.
- **Opening block and overview.** Open with the title, a one-line purpose that names the reader's task and scope, the primary audience, and a version or date. A document with 6 or more sections, or one whose conclusion readers need first, gets an overview under its own heading. The overview keeps the conclusion, the action, and essential qualifications.
- **Straight-through reading.** A tired reader, a second-language reader, or a listener cannot skim, so the page must also work read in order.

See [references/document-types.md](references/document-types.md) when you choose or restructure a doc type.

### 2. Voice

**Core concept:** Address the reader as "you" and name the actor of every sentence. Describe behavior in the present tense, and write as if the page will be read in five years.

**Key insights:**

- **Second person.** "We" hides who acts, and "the user" turns the reader into a third party. Both weaken an instruction. Use "we" only for the writing team when it really acts ("We deprecated the v1 endpoint").
- **Active voice.** Use the passive only when the actor is unknown, irrelevant, or deliberately secondary ("The file is encrypted at rest").
- **Present tense.** "Will" belongs only to effects that really come later: "The server sends an ack", not "will send".
- **Contractions `[EN]`.** Contractions are fine. Prefer "isn't" over "is not" for negations.
- **No anthropomorphism.** Software does not want, see, or think: "The API detects", not "the API sees".
- **No filler praise.** No "please" (keep it for asking permission), no "simply", "easily", or "just", no superlatives. If a step is easy, the reader will notice.
- **Timeless text.** Cut "currently", "new", and "soon". Never pre-announce unreleased features.
- **Positive framing.** Say what to do ("Keep the token secret"), not what to avoid, unless the warning itself is the point.

**Before and after:**

- "Please note that the new dashboard will simply be shown once the user has logged in." becomes "After you sign in, the dashboard appears."
- "We recommend that the token is refreshed by the client." becomes "Refresh the token from the client."

See [references/voice-and-words.md](references/voice-and-words.md) when a doc's tone is off or inconsistent.

### 3. Sentences and words

**Core concept:** Put the condition before the instruction, keep one idea per sentence, and choose the plain word.

**Key insights:**

- **Condition first.** "To delete the document, click **Delete**." Readers decide whether a step applies before they act, not after.
- **Sentence length.** Aim for an average of 15 to 20 words, and never exceed 30. Keep the subject close to its verb; do not wedge a clause between them.
- **Abbreviations.** Spell out an abbreviation on first use with the short form in parentheses. Skip only universally known ones (URL, HTML). Define domain terms on first use too.
- **Latin abbreviations `[EN]`.** They translate and scan poorly: "for example", not "e.g."; "that is", not "i.e."; omit "etc." or finish the list.
- **Modal verbs `[EN]`.** "can" means ability, "may" means permission, "might" means possibility.
- **Word list `[EN]`.** sign in (not log in), set up as a verb, lets you (not allows you to), through or by using (not via), after (not once), use (not leverage or utilize), checkbox, email.
- **Filler trims.** "to", not "in order to"; "because", not "due to the fact that"; "if", not "in the event that"; "now", not "at this point in time".
- **One term per concept.** Repeat the term instead of switching to a synonym. Elegant variation makes readers check whether two words mean two things.
- **Explicit connectors.** Use "because", "therefore", "if", "before", and "after" to state how two facts relate instead of leaving the reader to infer it.
- **Jargon.** Jargon is fine for the stated reader and a defect for anyone else. Define it or link it.

**Before and after:**

- "Click Save in order to persist the settings once you are done, i.e. when all fields are filled." becomes "After you fill in all fields, click **Save**."
- "The CLI utilizes the GCP SDK (e.g. for auth)." becomes "The CLI uses the Google Cloud SDK, for example for authentication."

See [references/voice-and-words.md](references/voice-and-words.md) when you audit word choice.

### 4. Structure: headings, lists, tables, notices

**Core concept:** Structure is the reader's map. Headings in sentence case read as a table of contents. Lists carry parallel items under a full introductory sentence. Tables have header rows. Notices are rare and mean something.

**Key insights:**

- **Noun-phrase headings.** A concept heading is a short noun phrase that names the topic. It is not a sentence, a claim, or a question, and it does not open with "What", "How", "Why", or an "-ing" word.
- **Task headings.** A heading over a procedure may be a bare imperative ("Create an instance").
- **Depth and contents.** Use at most 3 heading levels below the title, so `####` is the deepest. A document with 6 or more sections gets a table of contents worded exactly like its headings.
- **List introductions.** Three or more parallel items become a list. A list needs an introductory sentence ending in a colon, and every item in the same grammatical form. Number a list only when order matters.
- **Bold lead-ins.** Start each explanatory bullet with 2 to 4 bold words that name the item, then explain it. Use no other bold in prose except UI element names.
- **Description lists.** Term and definition pairs read better as a description list than as a two-column table.
- **Tables.** Give every table a header row and an introductory sentence, with no merged or empty cells. Screen readers depend on it.
- **Notices.** Note means useful but optional, Caution means proceed carefully, and Warning means harm or irreversible loss. Do not stack them; one per section is a practical ceiling (inferred).
- **Cross-references.** Say "see", never "above" or "below". Pages reflow and get translated.
- **Link text.** Link text names the target ("see Configure a custom domain"), never "click here".
- **Alt text.** Alt text states the image's purpose. Information must never live only in a picture, and no meaning may rest on bold, colour, or position alone.

See [references/structure-and-formatting.md](references/structure-and-formatting.md) when you fix page structure.

### 5. Technical explanations

**Core concept:** A technical explanation moves from intent to mechanism to code. The reader learns why the part exists before they see how it is wired, and sees the wiring before the lines.

**Key insights:**

- **Progressive disclosure.** Order the explanation in three stages. First the system purpose, in one sentence. Then the architecture and data flow, as a diagram or summary table. Last the implementation detail, with code and exact citations.
- **Stages only with content.** Use a diagram only when more than one component relates to another; a single mechanism, or steps an ordered list already shows, needs none. Omit a stage with no content and keep the order of the rest. A runbook or a decision record usually skips stages 2 and 3.
- **File and line citations.** When you explain code or a code change, cite the exact file and line range as a link, for example `[state_manager.rs:45-52](file:///src/state_manager.rs#L45-L52)`. Chat replies may use plain `path:line`. A guide that tells a user what to do needs no citation.
- **Consistent symbols.** Use the same symbol names in the text, the code samples, and the diagrams.
- **Diagram alternatives.** Put prose beside every diagram that says what it shows, not what it is. A listener receives Mermaid as source text, so the diagram's labels are not an alternative.

**Before and after:**

- "In order to prevent race conditions during concurrent state mutations within the execution pipeline, a mutex lock mechanism is introduced prior to updating the shared buffer." becomes "The state manager takes a mutex before each write, so concurrent writers cannot corrupt the shared buffer. The lock is in [state_manager.rs:45-52](file:///src/state_manager.rs#L45-L52):" followed by the code.

See [references/document-types.md](references/document-types.md) for progressive disclosure inside each skeleton, and [references/procedures-and-code.md](references/procedures-and-code.md) for citations and symbols.

### 6. Procedures and code

**Core concept:** A procedure is a numbered list of single imperative actions. Each step says where to act and what to expect. Code is set in code font, introduced by a sentence that ends in a colon, and uses placeholders the reader cannot mistake for literal values.

**Key insights:**

- **One action per step.** Prefix optional steps with "Optional:". A single step is a bullet, not "1.".
- **Forks.** A procedure that forks uses a decision table or labelled conditions, not one numbered list.
- **Sub-steps and the short path.** Sub-steps run a, b, c. Document the shortest path, not every alternative.
- **UI element names.** Set them in bold, matching the on-screen casing. Use click for a mouse, tap for touch, and select when the device does not matter.
- **Code font.** Use it for filenames, paths, commands, flags, parameters, and values, but not for product names.
- **Placeholders.** Write `ALL_CAPS_WITH_UNDERSCORES`, never `<your-key>` or `YOUR_API_KEY`. Explain each one right after the sample ("Replace `PROJECT_ID` with...").
- **Command syntax.** Use `[optional]`, `{a|b}` for exclusive choices, and `...` for repeatable arguments.
- **Sample quality.** Samples are runnable and minimal, wrap at 80 characters, and show the expected output.

**Before and after:**

- "Run the command below with your key: `shipit deploy --key=<your-key>`" becomes "To deploy, run the following command:", then a fenced `shipit deploy --key=API_KEY`, then "Replace `API_KEY` with the key from the **Settings** page."
- "1. You should now click on the Deploy button to deploy." becomes "1. Click **Deploy**. The status changes to **Deploying**."

See [references/procedures-and-code.md](references/procedures-and-code.md) when you write steps or samples.

### 7. Reference docs: API, docstrings, CLI help

**Core concept:** Reference text is descriptive, complete, and formulaic on purpose. Readers look things up, so every entry must exist and read the same way.

**Key insights:**

- **Complete coverage.** Document every public class, method, field, constant, and enum value. A missing entry reads as "unsupported".
- **Category verbs.** Open method descriptions with the category verb: "Gets the...", "Sets the...", "Checks whether...", "Creates a...", "Returns...". Never "This method...".
- **Parameters.** Non-boolean parameters start "The..." or "A...".
- **Boolean parameters.** Booleans read "If true, ... If false, ..." (action) or "True if ...; false otherwise" (state).
- **Returns and exceptions.** Document return values and exceptions ("Thrown when...") for every method that has them.
- **Deprecation.** A deprecated element names its replacement in the first sentence.
- **CLI help.** `--help` output (convention; Google has no `--help` page) has a usage line in `[optional]` syntax, a one-line synopsis, and every flag described with the same placeholder style.

**Before and after:**

- "This method is used for getting the customer." becomes "Gets the customer for the given `customerId`. Throws `NotFoundError` when no customer exists."
- "@param force - force flag" becomes "@param force If true, deletes the bucket even if it contains objects. If false, fails when the bucket isn't empty."

See [references/api-reference.md](references/api-reference.md) when you write or audit reference material.

### 8. Release notes, changelogs, migration guides

**Core concept:** A changelog is documentation for the reader who is about to upgrade. Each entry states what changed, what it means for them, and what to do. Use the structure of Keep a Changelog and the voice of the rest of the docs.

**Key insights:**

- **Order and dates.** Newest version first, an `Unreleased` section on top, ISO dates in version headings, version headings linked to diffs (Keep a Changelog).
- **Change groups.** Group entries under Added, Changed, Deprecated, Removed, Fixed, and Security. Never paste commit messages.
- **Breaking changes first.** Put them at the top of the version with a link to migration steps (convention).
- **Deprecation entries.** Name the replacement and the removal version or date.
- **Migration guides.** A migration guide is a procedure: "Before you begin" (versions, backups), numbered steps with before and after snippets, "Verify the migration", and rollback.
- **Same voice.** Second person for actions, no "currently" or "new", code font for flags and APIs, one tense throughout.

**Before and after:**

- "Various improvements to the auth module (#412)" becomes "Changed: `login()` now returns a `Session` instead of a token string. Update callers that read `.token`. See *Migrate to sessions*."

See [references/release-notes.md](references/release-notes.md) when you write release notes or a migration guide.

### 9. Running the audit, rewrite, or write

**Core concept:** Three modes share one protocol, and audits share one output shape.

**Protocol:**

1. **Intake.** Confirm the mode (audit, improve, or write), the document type, the reader and level, and the language. To write, you need the reader's task and the fact sources (code paths, existing docs). Do not start without them.
2. **Local style guide.** Look for `CONTRIBUTING.md`, `STYLE.md`, `docs/style-guide.md`, `.vale.ini`, and conventions the existing docs follow (for example, "log in" everywhere). They win over the rules here. Vale with the `Google` package automates the `[EN]` layer if the project wants a linter.
3. **Rule IDs.** Read [references/audit-checklist.md](references/audit-checklist.md) before any audit or improve pass. It holds the rule table, severities, non-English handling, a Vale configuration, and a worked mini-audit. Never cite an ID you have not read.
4. **Cold read and fact check.** Read the doc as the target reader. Then check every command, flag, parameter, and behavior against the code before you judge style. A stylish wrong doc is worse than an ugly right one.
5. **Machine pass.** Run Vale on each file: the project's own `.vale.ini` if it has one (precedence rule 2), else `vale --config <skill folder>/vale/.vale.ini --output=JSON <file>`, where the skill folder is the one that holds this SKILL.md. Map each alert to a rule ID through the Vale mapping table in [references/audit-checklist.md](references/audit-checklist.md#vale-for-the-en-layer). If `vale` is not installed, skip this step and say so on the `**Linter:**` line.

   An exact alert is a finding. Confirm or discard each candidate alert by reading the sentence, and never report a discarded one. Drop alerts the table does not map. Then do the LLM pass for every rule Vale cannot check.
6. **Severity order.** Blocking, then High (structure, accessibility, missing reference entries), then Medium (voice, notices, introductory sentences), then Low (word list, punctuation `[EN]`).
7. **Output.** Give each finding a location the reader can find: the heading path, plus the line number when you audit a file. Improve mode returns a one-line `Score before -> after`, the full rewritten document, and a `## Change log` table (Change | Rule ID + name | Why). Write mode returns the document with `TODO(verify)` for every gap.

Facts stay untouched. A fact stated in the source document counts as received from the user, so keep it (with `TODO(verify): ...` when no code confirms it) instead of deleting it. Never include a command, flag, or parameter you did not see in code or receive from the user.

Always output audits in this format:

```
# Documentation audit: [path or title]
**Score:** X/12 ([band])   **Shippable:** yes | no (blocking findings below)
**Diagnostic:** N/12, failed rows: [row numbers + one-line reason each]
**Doc type / reader:** [type] for [audience, level]   **Language:** [en | xx, [EN] rules skipped]
**Local style guide:** [file found and honored | none, default rules apply]
**Linter:** [vale: N alerts, K kept as findings | vale not installed, LLM pass only]
**Blocking:** [wrong or unverifiable facts, unfollowable steps, image-only information, or "none"]
**Findings:**
| # | Location | Rule (ID + name) | Before | After | Severity |
**Rewrite plan:** [ordered: structure, then voice, then words; what to do first to reach 12/12]
```

## AI tells

Model-written drafts carry habits that make readers distrust the text. Remove these in every mode.

| ID | Tell | Before | After |
|----|------|--------|-------|
| H1 | Not X but Y: a contrast against a claim nobody made | "It's not just a cache, it's a performance layer." | "The cache cuts repeat reads." |
| H2 | One-line closers that restate the paragraph | "Retries hide brief outages. That is the real win." | "Retries hide brief outages." |
| H3 | Staged run-up before the point | "Let's dive in. Here's what you need to know: the API is rate-limited." | "The API allows 100 requests per minute." |
| H4 | Forced triads: three items when the meaning has fewer | "The cache is fast, reliable, and scalable." | "The cache answers reads in under 2 ms." |
| H5 | Dashes as the universal connector, and their stand-ins: middle dots (`·`, `・`) as separators, a spaced hyphen (` - `) between words | `The token — issued at sign-in — expires`; `Docs · Slides · UI` | Commas, colons, periods, or parentheses; no em or en dashes in prose; "Docs, slides, and UI" |
| H6 | Stacked qualifiers | "could potentially possibly affect" | "may affect" |
| H7 | Inflated significance, vague links ("associated with"), shallow -ing tails ("ensuring", "highlighting") | "marks a pivotal moment, ensuring growth" | Name the real relation; end on the last concrete fact |
| H8 | Stock AI words: delve, crucial, pivotal, robust (figurative), showcase, underscore, landscape, key (adjective), additionally, testament, load-bearing, quietly, genuinely, honestly | "a crucial, robust solution" | "a solution that retries failed writes" |
| H9 | Sales language | "a groundbreaking, stunning dashboard" | "a dashboard that shows error rates per service" |
| H10 | Chatbot residue | "Great question! ... I hope this helps." | The content only |
| H11 | Text about itself: how it was compiled, what it replaced, a layout the reader can see | "The table below compares the options." | Introduce the table with its subject: "The following flags control output:" |
| H12 | Re-explaining what a reply's reader knows | A review reply that restates the bug and the diagnosis before the decision | Lead with the decision; keep one fact the reader lacks |
| H13 | Heading restated in the first sentence | "## Retries" then "Retries matter." | Start with the first fact |
| H14 | Knowledge-limit disclaimers and guesses | "Not widely documented, but it likely uses Redis." | Say what the source lacks, or cut it |
| H15 | Sayings that sound deep | "At its core, latency is the currency of trust." | The specific claim |
| H16 | Arguing with no one | "To be clear, this isn't about speed." | State the claim |
| H17 | Repeated sentence openings | "It reads the file. It parses it." | "It reads and parses the file." |
| H18 | Hyphenated pairs after the noun `[EN]` | "The API is well-documented." | "The API is well documented." |
| H19 | Borrowed authority | "Experts agree the design is sound." | Name the source, or cut it |
| H20 | Avoiding is, are, and has `[EN]` | "The gateway serves as the entry point." | "The gateway is the entry point." |
| H21 | Curly quotation marks | `“token”` | `"token"` |
| H22 | Decorative headings: a heading that sells, announces, or teases instead of naming the content | "## Why this changes everything" | "## Retry limits" |
| H23 | Bold as decoration: bold on phrases mid-sentence for emphasis (see S13) | "The cache is **very fast** and **easy to use**." | "The cache answers reads in under 2 ms." |
| H24 | Missing subjects `[EN]`: fragments that drop the actor | "Checked the logs. Found nothing." | "I checked the logs and found nothing." |
| H25 | Counts the reader can see or does not need | "The board must act on four points:" then four bullets; "all twenty-nine decisions" | "The board must act on these points:"; "all decisions". Keep counts that are the fact: limits, retries, "3 of 5 tests failed" |
| H26 | Staccato rhythm: short sentence, shorter one, pivot | "The tell isn't the words. It's the rhythm. Short sentence. Pivot." | "Readers recognize the rhythm of short sentences that end in a pivot." |
| H27 | Semicolons inside a sentence | "The cache is fast; the disk is slow." | "The cache is fast. The disk is slow." |

Leave a watched phrase alone inside a quotation, a proper name, or a passage that discusses the phrase. Mention a previous version only in changelogs, release notes, and migration guides.

## Common mistakes

| Mistake | Why it fails | Fix |
|---------|-------------|-----|
| Organizing by feature instead of reader task | Readers hunt across sections for one workflow | Name the reader's task; pick the doc type; one task per page |
| Fixing style before verifying facts | Polished wrong instructions are trusted longer | Check every command and parameter against code first |
| "Click here" and "see below" | Meaningless out of context, to screen readers, and after reflow | Link text names the target; cross-references say "see" |
| Steps buried in paragraphs, passive and future tense | The reader cannot tell who does what, or in what order | Numbered imperative steps, condition first, present tense |
| Stacked Note and Warning boxes | Everything shouts, so nothing is heard | One notice per section; the rest becomes body text |
| `<your-key>` or `YOUR_API_KEY` placeholders | The reader types the brackets or reads the prefix as a literal | `API_KEY` in caps, explained after the sample |
| Rewriting the meaning while fixing style | The reviewer approves prose and ships wrong behavior | Facts unchanged; unknowns become `TODO(verify)` |
| Sentence or question headings | The table of contents reads as prose and scans badly | Short noun phrases; bare imperatives over procedures |

## Quick diagnostic

| # | Question | If no | Action |
|---|----------|-------|--------|
| 1 | Does the opening give the title, who the doc is for, what they can do after reading, and a version or date, with an overview heading in a long doc? | Readers cannot tell if they are on the right page | Add audience, outcome, non-scope, and version; add an overview |
| 2 | Does the doc type match the reader's task (tutorial, how-to, concept, reference, README)? | Concept and steps interleave; nothing is findable | Split by type; link between pages |
| 3 | Is every command, flag, parameter, and behavior verified against code or the user? | The doc teaches something false | Verify or mark `TODO(verify)`; not shippable until fixed |
| 4 | Do headings read as a sentence-case table of contents: noun phrases for concepts, bare imperatives for tasks, no sentences or "What/How/Why/-ing" openers, `####` at most, and a contents list from 6 sections? | Scanning fails; headings argue instead of naming | Rewrite headings; add one where each new task starts; flatten deep levels; add a contents list |
| 5 | Are all sequences numbered steps, one imperative action each, condition first, with forks in a decision table? | Readers miss steps or act before checking | Convert paragraphs to steps; move conditions forward; put forks in a decision table |
| 6 | Is every code sample introduced by a colon sentence, with `ALL_CAPS` placeholders explained? | Readers paste literals or do not know what the sample does | Add introductory sentences; fix and explain placeholders |
| 7 | Is the text in second person, active voice, present tense, with sentences of 30 words or fewer, no filler, and no anthropomorphism? | Instructions read as narration | Rewrite sentence by sentence; trim filler; split long sentences |
| 8 | Are links descriptive, cross-references "see"-based, images and diagrams given text alternatives, tables headed? | Screen readers and reflow break the page | Fix each; move image-only information into text |
| 9 | Is it timeless, with no "currently/new/soon" and no pre-announced features? | The doc rots the day it ships | Remove time words; describe only shipped behavior |
| 10 | Do technical explanations run purpose, then architecture, then implementation with linked `file:line` citations and defined acronyms? | The reader meets code before knowing why it exists | Reorder by stage; add citations and definitions |
| 11 | Is the text free of AI tells H1 to H27? | Readers stop trusting the page | Apply the AI tells table |
| 12 | `[EN]` Does it follow the word list, serial comma, contractions, and American spelling, or the local guide? | Small inconsistencies erode trust | Apply the word list; run Vale if configured |

## Source

- **wondelai technical-documentation.** Structure, rule IDs R, V, W, S, P, A, and N, scoring, and the audit protocol are adapted from [wondelai/skills](https://github.com/wondelai/skills) `technical-documentation` (MIT, Copyright 2025 Wondel.ai sp. z o.o.).
- **Google developer documentation style.** wondelai adapts the [Google Developer Documentation Style Guide](https://developers.google.com/style) and the [Technical Writing One](https://developers.google.com/tech-writing/one) and [Two](https://developers.google.com/tech-writing/two) courses under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This is an independent adaptation, not endorsed by Google. Release notes follow [Keep a Changelog](https://keepachangelog.com/).
- **ISO 24495 proxies.** The I rules come from the iso-24495-1, iso-24495-3, and iso-24495-5 skills by Gareth Williams (MIT). They are proxies for the principles of ISO 24495-1:2023, ISO 24495-3:2026, and the ISO/WD 24495-5 working draft, not the standards' text, and following them is not a conformance claim. ISO 24495-5 is unpublished, so the I14 to I18 rows are provisional. The `TechWriter` Vale rules for I1 to I3, I7, I14, and parts of R6, S2, S3, S5, S6, S9, and S10 port the checks of the iso-24495 text audit (v0.7.0).
- **Wikipedia.** The AI tells H1 to H24 draw on [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), an advice page of WikiProject AI Cleanup (CC BY-SA 4.0). The page is descriptive advice, not Wikipedia policy. H rows with no section on that page are this skill's own.
- **vale-ai-tells.** The machine pass runs [vale-ai-tells](https://github.com/tbhb/vale-ai-tells) v1.37.0 by tbhb (MIT) and the [Google Vale package](https://github.com/vale-cli/Google) (MIT) through [Vale](https://vale.sh) (MIT).
- **Further reading.** *Docs for Developers* (Bhatti and others, Apress, 2021) and *Every Page Is Page One* (Mark Baker, 2013).
- **License.** This skill is MIT licensed, see [LICENSE](LICENSE). The upstream notices are in [THIRD_PARTY.md](THIRD_PARTY.md).
