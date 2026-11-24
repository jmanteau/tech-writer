# Audit checklist: rule IDs, severity, and scoring

This file holds the fixed rule table the skill cites, plus the mechanics that turn it into a score and a ship or no-ship decision.

1. [Checklist use](#checklist-use)
2. [Rule table](#rule-table)
3. [Severity rubric and the shippability gate](#severity-rubric-and-the-shippability-gate)
4. [Scoring mechanics](#scoring-mechanics)
5. [Local style guide](#local-style-guide)
6. [Non-English documents](#non-english-documents)
7. [Vale for the `[EN]` layer](#vale-for-the-en-layer)
8. [Worked mini-audit](#worked-mini-audit)

---

## Checklist use

Read this file before any audit or improve pass. Rule IDs are stable identifiers. Cite an ID only after you read its row. IDs fill the Findings column "Rule (ID + name)" and, in improve mode, the change-log column "Rule ID + name".

- **One ID per finding.** Pair two IDs (`P7 / P8`) only when one edit fixes both. The pair takes the higher severity.
- **Severity from the table.** Take severity from the rule table, not from how annoying the defect felt.
- **Owner files.** Explanations and Before/After pairs live in the owner file named in the last column. Here each rule is one row.

Use the audit output block in SKILL.md, section "Running the audit, rewrite, or write", unchanged.

Source: skill rule (SKILL.md, section 9).

---

## Rule table

The table has 106 rules in nine groups. Groups R, V, W, S, P, A, and N come from wondelai's `technical-documentation` skill, which adapts Google's guide. Group I holds the ISO 24495-1, 24495-3, and 24495-5 proxies (ISO 24495-5 is an unpublished working draft, so its rows are provisional), and group H holds the AI tells. The `(inferred)` and `(convention)` labels mark rows that are not verbatim Google guidance; keep the label when you cite them. Source slugs are pages under `developers.google.com/style` unless another origin is named.

**R: reader and document type**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| R1 | The first paragraph states who the doc is for and what they will accomplish | High | none | tech-writing/one "Documents"; ISO 24495-1 skill, know the reader | document-types.md |
| R2 | The doc type matches the reader's task: tutorial, how-to, concept, reference, or README | High | none | (inferred taxonomy; Google covers procedures and concept-heading style) | document-types.md |
| R3 | Prerequisites listed before the first step ("Before you begin") | High | none | procedures and Google docs practice (convention) | document-types.md |
| R4 | Scope and non-scope stated; the non-scope names where to go instead | Medium | none | tech-writing/one "Documents"; ISO 24495-5 skill, rule 9 (draft) | document-types.md |
| R5 | Ends with verification, "What's next", or both | Medium | none | (convention) | document-types.md |
| R6 | Key points first: the page or reply opens with the answer, no pleasantries; one idea per paragraph, and the lead sentence carries it | Medium | none | paragraphs, tech-writing/one "Paragraphs"; ISO 24495-1 skill, rule 1 (no preamble) and rule 4 (front-loading) | document-types.md |

**V: voice**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| V1 | Second person "you"; never "we" or "the user" for the reader; "we" only for the writing team when it really acts; "I" for the writer of a reply | Medium | none | person; ISO 24495-1 skill, direct address | voice-and-words.md |
| V2 | Active voice unless the actor is unknown, irrelevant, or deliberately secondary | Medium | none | voice; ISO 24495-1 skill, voice | voice-and-words.md |
| V3 | Present tense; "will" only for effects that really come later | Medium | none | tense | voice-and-words.md |
| V4 | No "please" outside asking permission or forgiveness | Low | none | tone | voice-and-words.md |
| V5 | No "simply", "easily", "just", "quickly", superlatives, or absolutes | Low | none | excessive-claims | voice-and-words.md |
| V6 | No anthropomorphism (software does not want, see, or think) | Medium | none | anthropomorphism | voice-and-words.md |
| V7 | Timeless: no "currently", "now", "new", or "soon"; no pre-announcing | Medium | none | future, timeless-documentation | voice-and-words.md |
| V8 | Contractions allowed; negations prefer "isn't" and "don't" | Low | `[EN]` | contractions | voice-and-words.md |
| V9 | Inclusive language (no master/slave, blacklist/whitelist, sanity check, or gendered generic pronouns) | Medium | none | inclusive-documentation | voice-and-words.md |
| V10 | Global audience: no idioms, culture-bound examples, or "once" meaning "after" | Low | none | translation | voice-and-words.md |

**W: words and sentences**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| W1 | Condition or goal before the instruction | Medium | none | sentence-structure | voice-and-words.md |
| W2 | One idea per sentence; short sentences (limits in I1) | Low | none | tech-writing/one "Short sentences"; ISO 24495-1 skill, sentence limits | voice-and-words.md |
| W3 | Abbreviations and domain terms spelled out or defined on first use | Medium | none | abbreviations; ISO 24495-3 skill, rule 3 | voice-and-words.md |
| W4 | No e.g., i.e., etc., or vs. | Low | `[EN]` | abbreviations | voice-and-words.md |
| W5 | can, may, and might used for ability, permission, and possibility | Low | `[EN]` | word-list | voice-and-words.md |
| W6 | Jargon defined or avoided for the stated reader | Medium | none | jargon | voice-and-words.md |
| W7 | Word-list compliance (one rule; entries live in voice-and-words.md) | Low | `[EN]` | word-list | voice-and-words.md |
| W8 | American spelling; serial comma | Low | `[EN]` | highlights, commas | voice-and-words.md |

**S: structure and formatting**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| S1 | Sentence case for titles and headings | Low | none | headings | structure-and-formatting.md |
| S2 | Concept headings are short noun phrases; task headings over a procedure may be bare imperatives; no sentence, claim, or question headings, no "What/How/Why" openers, no "-ing" openers; no wordplay, and no term the page has not yet explained | Medium | none | headings; user rule for this skill; ISO 24495-1 skill, house convention (single-topic headings); ISO 24495-5 skill, rule 1 (draft; its message headings are not taken, see SKILL.md, Precedence) | structure-and-formatting.md |
| S3 | No skipped heading levels; no trailing period; (inferred) no heading immediately followed by a heading | Low | none | headings | structure-and-formatting.md |
| S4 | Lists: a complete introductory sentence ending in a colon; parallel items | Medium | none | lists | structure-and-formatting.md |
| S5 | Three or more parallel items become a list; numbered lists only for sequences; bullets otherwise; description lists for pairs; each bullet one paragraph, nested at most 2 levels | Medium | none | lists; ISO 24495-1 skill, house convention (lists); ISO 24495-5 skill, rule 4 (draft) | structure-and-formatting.md |
| S6 | Tables: header row, introductory sentence, no merged or empty cells; comparisons of 2 or more items across attributes go in a table | High | none | tables, accessibility; ISO 24495-5 skill, rules 4 and 6 (draft) | structure-and-formatting.md |
| S7 | Notices: do not stack; Note, Caution, and Warning semantics; (inferred) one per section | Medium | none | notices; ISO 24495-5 skill, rule 4 (draft) | structure-and-formatting.md |
| S8 | Cross-references use "see"; never "above" or "below" | Medium | none | cross-references | structure-and-formatting.md |
| S9 | Descriptive link text; never "click here" or "this link" | High | none | link-text, accessibility; ISO 24495-5 skill, rule 6 (draft) | structure-and-formatting.md |
| S10 | Purposeful alt text; information never only in an image | Blocking | none | images, accessibility; ISO 24495-5 skill, rule 6 (draft) | structure-and-formatting.md |
| S11 | Unambiguous dates; numbers zero to nine spelled out, 10 and up as numerals | Low | `[EN]` | dates-times, numbers | structure-and-formatting.md |
| S12 | Bold for UI elements, code font for code, italics sparingly for terms; one meaning per visual device | Low | none | text-formatting; ISO 24495-5 skill, rule 5 (draft) | structure-and-formatting.md |
| S13 | Explanatory bullets open with 2 to 4 bold lead-in words; no other bold in prose except UI names | Low | none | ISO 24495-1 skill (house convention) | structure-and-formatting.md |

**P: procedures and code**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| P1 | Steps numbered, one imperative action per step; a missing required step escalates to Blocking | High | none | procedures | procedures-and-code.md |
| P2 | A single step is a bullet; sub-steps run a, b, c, then i, ii, iii | Low | none | procedures | procedures-and-code.md |
| P3 | Optional steps prefixed "Optional:" | Low | none | procedures | procedures-and-code.md |
| P4 | Each step says where to act and what result to expect | Medium | none | procedures | procedures-and-code.md |
| P5 | UI names bold, casing matches the UI; click, tap, or select by device | Low | none | ui-elements | procedures-and-code.md |
| P6 | Code font for filenames, paths, commands, flags, parameters, and values, not product names | Medium | none | code-in-text | procedures-and-code.md |
| P7 | Every code sample introduced by a sentence ending in a colon | Medium | none | code-samples | procedures-and-code.md |
| P8 | Placeholders in `ALL_CAPS_WITH_UNDERSCORES`, no MY_ or YOUR_ prefix, explained after the sample | Medium | none | placeholders | procedures-and-code.md |
| P9 | Command-line syntax: `[optional]`, `{a\|b}`, `...` | Low | none | code-syntax | procedures-and-code.md |
| P10 | Samples runnable and minimal, lines of 80 characters or fewer, expected output shown | Medium | none | code-samples, tech-writing/two "Sample code" | procedures-and-code.md |
| P11 | Every command, flag, parameter, and behavior verified in code or given by the user | Blocking | none | (skill rule) | procedures-and-code.md |

**A: API reference, docstrings, CLI help**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| A1 | Every public class, method, field, and constant documented | High | none | api-reference-comments | api-reference.md |
| A2 | Method descriptions open with the category verb (Gets, Sets, Checks whether, Creates, Returns); no "This method..." | Medium | none | api-reference-comments | api-reference.md |
| A3 | Non-boolean parameters start "The..." or "A..."; booleans read "If true, ... If false, ..." or "True if ...; false otherwise" | Medium | none | api-reference-comments | api-reference.md |
| A4 | Return values and exceptions documented ("Thrown when...") | High | none | api-reference-comments | api-reference.md |
| A5 | Deprecated elements name the replacement in the first sentence | High | none | api-reference-comments | api-reference.md |
| A6 | CLI help: usage line, one-line synopsis, every flag described, placeholders in caps | Medium | none | code-syntax and (convention; Google has no `--help` page) | api-reference.md |
| A7 | Reference text is descriptive third-person present; guides are imperative | Low | none | reference-verbs | api-reference.md |

**N: release notes, changelogs, migration**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| N1 | Newest version first; `Unreleased` section; ISO dates in version headings | Medium | none | keepachangelog.com | release-notes.md |
| N2 | Entries grouped under Added, Changed, Deprecated, Removed, Fixed, and Security | Medium | none | keepachangelog.com | release-notes.md |
| N3 | Each entry states what changed, the reader impact, and the action; never raw commit messages | High | none | keepachangelog.com | release-notes.md |
| N4 | Breaking changes called out first with a link to migration steps | High | none | (convention) | release-notes.md |
| N5 | Deprecation entries name the replacement and the removal version or date | High | none | keepachangelog.com, api-reference-comments | release-notes.md |
| N6 | A migration guide is a procedure with before and after snippets and a verify step | High | none | procedures (applied) | release-notes.md |

**I: Plain Language (ISO 24495-1, 24495-3, and 24495-5 proxies)**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| I1 | Sentences average 15 to 20 words; none over 30; one main idea each | Medium | none | ISO 24495-1 skill, sentence limits | voice-and-words.md |
| I2 | Paragraphs of 3 to 5 sentences, one topic, main point first; shorter is fine; 4 sentences or fewer in a reply | Low | none | ISO 24495-1 skill, paragraph limits | voice-and-words.md |
| I3 | Familiar words and filler trims ("to", not "in order to"; "because", not "due to the fact that") | Low | `[EN]` | ISO 24495-1 skill, wording | voice-and-words.md |
| I4 | One term per concept; no elegant variation | Medium | none | ISO 24495-1 skill, wording | voice-and-words.md |
| I5 | Explicit connectors (because, therefore, if, before, after) state how facts relate | Low | none | ISO 24495-1 skill, wording | voice-and-words.md |
| I6 | Subject close to its verb; no clause wedged between them | Low | none | ISO 24495-1 skill, proximity | voice-and-words.md |
| I7 | Positive framing: say what to do, unless the warning itself is the point | Low | none | ISO 24495-1 skill, wording | voice-and-words.md |
| I8 | The page works read straight through and through a screen reader; no meaning carried by bold, colour, or position alone; reading order is document order | High | none | ISO 24495-1 skill, intended readers; ISO 24495-5 skill, rules 5 and 6 (draft) | structure-and-formatting.md |
| I9 | Progressive disclosure: purpose, then architecture and data flow, then implementation; omit empty stages, keep the order | Medium | none | ISO 24495-3 skill, rule 1 | document-types.md |
| I10 | Code explanations cite the exact file and line range as a link, `[file.rs:45-52](file:///src/file.rs#L45-L52)`; plain `path:line` in chat replies | High | none | ISO 24495-3 skill, rule 2 | procedures-and-code.md |
| I11 | Same symbol names across text, code samples, and diagrams | Medium | none | ISO 24495-3 skill, rule 3 | procedures-and-code.md |
| I12 | Every diagram has prose beside it that says what it shows; diagram source or labels are not an alternative | High | none | ISO 24495-3 skill, rule 4 | structure-and-formatting.md |
| I13 | Several audiences: the primary audience is named, and its needs settle conflicts | Medium | none | ISO 24495-1 skill, audiences | document-types.md |
| I14 | At most 3 heading levels below the title (`####` is the deepest) | Low | none | ISO 24495-5 skill, rule 1 (draft) | structure-and-formatting.md |
| I15 | A document with 6 or more sections has a table of contents worded exactly like its headings | Medium | none | ISO 24495-5 skill, rule 2 (draft) | structure-and-formatting.md |
| I16 | Opening block: title, one-line purpose with the reader's task and scope, the primary audience, and a version or date | Medium | none | ISO 24495-5 skill, rule 7 (draft) | document-types.md |
| I17 | A document with 6 or more sections, or whose conclusion readers need first, has an overview under its own heading that keeps the conclusion, the action, and essential qualifications | Medium | none | ISO 24495-5 skill, rule 8 (draft) | document-types.md |
| I18 | A procedure that forks uses a decision table or labelled conditions, not one numbered list | Medium | none | ISO 24495-5 skill, rule 4 (draft) | procedures-and-code.md |

I14 to I18 apply to documents. They skip chat replies and review comments, which ISO 24495-3 treats as explanations that Part 5 does not govern (ISO 24495-3 skill, scope).

**H: AI tells**

| ID | Rule | Severity | [EN] | Source | Owner file |
|----|------|----------|------|--------|-----------|
| H1 | No "not X but Y" contrast against a claim nobody made | Medium | none | WP "Negative parallelisms" | SKILL.md |
| H2 | No one-line closer that restates the paragraph | Medium | none | WP "Section summaries" | SKILL.md |
| H3 | No staged run-up before the point | Medium | none | (this skill's own) | SKILL.md |
| H4 | No forced triads; list as many items as the meaning has | Low | none | WP "Rule of three" | SKILL.md |
| H5 | No em or en dashes in prose, and no stand-ins for them (middle dots `·` `・` as separators, a spaced ` - ` between words); use commas, colons, periods, or parentheses | Low | none | WP "Overuse of em dashes" | SKILL.md |
| H6 | No stacked qualifiers | Low | none | (this skill's own) | SKILL.md |
| H7 | No inflated significance, vague "associated with" links, or shallow -ing tails ("ensuring", "highlighting"); end on the last concrete fact | Medium | none | WP "Undue emphasis on significance, legacy, and broader trends"; "Vague expression of connection or association"; "Superficial analyses"; "Outline-like conclusions about challenges and future prospects" | SKILL.md |
| H8 | No stock AI words (delve, crucial, pivotal, robust in its figurative sense, showcase, underscore, landscape, key as an adjective, additionally, testament, load-bearing, quietly, genuinely, honestly) | Low | `[EN]` | WP "High density of AI vocabulary words" | SKILL.md |
| H9 | No sales language | Low | none | WP "Promotional and advertisement-like language" | SKILL.md |
| H10 | No chatbot residue (greetings, praise, offers, "I hope this helps") | Medium | none | WP "Collaborative communication"; "Phrasal templates and placeholder text"; "Prompt refusal"; "utm_source=" | SKILL.md |
| H11 | No text about the document itself: how it was compiled, what it replaced, or a layout the reader can see | Medium | none | WP "Collaborative communication" | SKILL.md |
| H12 | A reply leads with the decision and does not rebuild context its reader has | Medium | none | (this skill's own) | SKILL.md |
| H13 | No heading restated in the first sentence | Medium | none | (this skill's own) | SKILL.md |
| H14 | No knowledge-limit disclaimers or guesses; say what the source lacks, or cut it | Medium | none | WP "Hedging disclaimers about source availability and recommended usage"; "Statements about knowledge cutoffs" | SKILL.md |
| H15 | No sayings that sound deep; state the specific claim | Medium | none | (this skill's own) | SKILL.md |
| H16 | No arguing with an objection or option the text never raised | Medium | none | WP "Negative parallelisms" | SKILL.md |
| H17 | No run of sentences with the same opening | Low | none | (this skill's own) | SKILL.md |
| H18 | No hyphen in a compound modifier after the noun ("is well documented") | Low | `[EN]` | (this skill's own) | SKILL.md |
| H19 | No borrowed authority; name the source and what it said, or cut the claim | Medium | none | WP "Vague attributions and overgeneralization of opinions"; "Undue emphasis on notability, attribution, and media coverage" | SKILL.md |
| H20 | Use is, are, and has instead of "serves as", "boasts", or "features" | Low | `[EN]` | WP "Avoidance of basic copulatives" | SKILL.md |
| H21 | Straight quotation marks unless the target format uses curly ones | Low | none | WP style signs (curly quotation marks) | SKILL.md |
| H22 | Headings name the content; no selling, announcing, or teasing headings | Low | none | WP "Outline-like conclusions about challenges and future prospects"; "Awards and recognition section"; title case in section titles | SKILL.md |
| H23 | No bold for emphasis in prose; bold only for S13 lead-ins and UI names | Low | none | WP style signs (overuse of boldface) | SKILL.md |
| H24 | No fragments that drop the subject ("Checked the logs."); passive voice stays under V2 | Low | `[EN]` | (this skill's own) | SKILL.md |
| H25 | No count before a list the reader sees, or a total that drives no decision; keep counts that are the fact | Low | none | (this skill's own) | SKILL.md |
| H26 | No staccato rhythm: a run of short sentences that ends in a pivot | Low | none | (this skill's own) | SKILL.md |
| H27 | No semicolons in prose; split into sentences or use a comma and a conjunction | Low | none | (this skill's own) | SKILL.md |

Source: Google Developer Documentation Style Guide (slug per row), Google Technical Writing One and Two, and keepachangelog.com for N1 to N5, through wondelai's skill. I rows come from the iso-24495 skills. H rows come from Wikipedia's Signs of AI writing (WP = that page's section), except the rows labelled this skill's own.

---

## Severity rubric and the shippability gate

Severity says what breaks for the reader, not how many words change. Each rule carries its own severity in the table.

| Severity | Definition |
|----------|-----------|
| Blocking | Facts wrong or unverifiable; a procedure the reader cannot complete; information carried only by an image, or an image with no alt text |
| High | Wrong doc type, missing audience or prerequisites, steps buried in paragraphs, vague link text, headerless tables, undocumented API elements, changelog entries with no reader impact, code explained without citations, diagrams without a prose alternative |
| Medium | Passive voice, future tense, "we" or "the user", anthropomorphism, time-bound wording, unexplained abbreviations, misused notices, missing introductory sentences, placeholder style, long sentences, sentence headings, the stronger AI tells |
| Low (mostly `[EN]`) | Word list, serial comma, contractions, spelling, UI-label casing, Latin abbreviations, numbers and dates, filler phrases, bold lead-ins, the weaker AI tells |

Blocking is a gate, not a deduction. One Blocking finding makes a doc `Shippable: no` at 11/12, and a doc with none is shippable at 7/12. Report them on separate lines.

Work from Blocking to High to Medium to Low. Within each level, fix structure before voice and voice before words. Sentences polished in a section you later delete are wasted, and word edits made before a restructure get made twice.

Source: skill rule, severity rubric and protocol step 6 in SKILL.md, section 9.

---

## Scoring mechanics

The score is the number of Quick diagnostic rows passed: 12 rows, one point each, no partial credit. A row passes only if the whole document satisfies it. A row with no applicable content passes; for example, a concept page with no procedures passes rows 5 and 6, and a how-to that explains no code passes row 10.

A and N findings affect `Shippable` and the Rewrite plan, not the score. Row 12 passes automatically for a non-English doc. Name the band from SKILL.md's Scoring section; do not restate it. Findings cite the rule ID, not the row number.

The following table maps each row to its rule IDs:

| Row | Checks | Rule IDs |
|-----|--------|----------|
| 1 | Audience, outcome, and opening block up front | R1 / R4 / I13 / I16 |
| 2 | Doc type fits the task | R2 |
| 3 | Facts verified against code | P11 |
| 4 | Headings scan as a contents list; depth, contents list, and overview | S1 / S2 / I14 / I15 / I17 |
| 5 | Numbered imperative steps, condition first; forks as decision tables | P1 / W1 / I18 |
| 6 | Samples introduced, placeholders explained | P7 / P8 |
| 7 | Second person, active, present, short sentences, no filler | V1 to V6 / I1 / I3 |
| 8 | Links, cross-references, images, diagrams, and tables accessible | S6 / S8 / S9 / S10 / I8 / I12 |
| 9 | Timeless | V7 |
| 10 | Technical explanations ordered and cited | I9 / I10 / I11 / W3 |
| 11 | No AI tells | H1 to H27 |
| 12 | `[EN]` word list, serial comma, contractions, spelling | W7 / W8 / V8 |

The `**Diagnostic:**` line repeats the number and names the failures: `N/12, failed rows: <n> (<one-line reason>), ...`. Write one clause per failed row, phrased as the observed defect. Do not list passing rows.

Source: skill rule (SKILL.md, Scoring and Quick diagnostic).

---

## Local style guide

A project's conventions outrank the rules here. Find them before you file a finding against a deliberate choice.

The following files usually settle the house style:

| Look for | Usually settles |
|----------|-----------------|
| `CONTRIBUTING.md` | Docs workflow, tone, required sections |
| `STYLE.md`, `STYLEGUIDE.md`, `docs/style-guide.md` | Explicit house style |
| `docs/contributing/*.md` | Per-docs-set conventions |
| `.vale.ini` | Linter package and word list in force |
| `.markdownlint*` | Heading levels, line length, list markers |
| `.github/PULL_REQUEST_TEMPLATE.md` | The docs checklist the team applies |

When no file states the rules, the docs still show them:

- **Preferred terms.** Run `grep -rin "log in\|sign in" docs/`. The term with more hits is the house term.
- **Heading case.** Sample a dozen `^#{1,3} ` lines. Title case throughout is a convention, not twelve findings.
- **Placeholders.** Run `grep -rn "YOUR_\|<[a-z-]*>" docs/`. A consistent house form beats P8.
- **Notices.** Match the toolchain's syntax (`> **Note**`, `:::note`, `{: .note }`).

Precedence: verified facts, then the project guide, then ISO 24495-3, then ISO 24495-1, then the ISO 24495-5 working draft, then Google. After Google come Merriam-Webster (spelling), Chicago (general), and the Microsoft Writing Style Guide (technical). A convention wins in its scope only if it is consistent. An inconsistent habit is a finding.

Record the result on the report's `**Local style guide:**` line. Write the file and that you honored it, any rule you deferred (`STYLE.md, title-case headings, S1 not applied`), or `none, default rules apply`.

Source: developers.google.com/style/about for precedence; the file list and grep probes are convention.

---

## Non-English documents

Structure and content rules apply unchanged: all of R, S1 to S10, S12, S13, P1 to P11, A1 to A6, N1 to N6, I1, I2, and I4 to I18. The same holds for H1 to H7, H9 to H17, H19, H21 to H23, and H25 to H27, plus V1, V2, V3, V6, V7, V9 and W1, W3, W6. A Japanese how-to still needs an audience statement, numbered steps, and verified flags.

Skip the `[EN]` rules (V8, W4, W5, W7, W8, S11, I3, H8, H18, H20, H24), which encode English spelling, word choice, and punctuation. V4, V5, V10, W2, S1, S2, and A7 sit in between: the intent transfers, but the exact test does not.

Record the language and the skipped layer on the report's `**Language:**` line: `de, [EN] rules skipped (V8, W4, W5, W7, W8, S11, I3, H8, H18, H20, H24)`. Row 12 then passes automatically, out of the same 12. For a mixed-language doc, apply the `[EN]` rows to the English passages only and record `mixed (en/pl), [EN] applied to English text`.

Never translate a document unless asked. A translation hides the page from its readers and turns a style audit into a content change.

Source: skill rule (SKILL.md, Core principle) with translation and global-audience guidance.

---

## Vale for the `[EN]` layer

Vale with the Google package catches most Low-severity English findings mechanically. Put this minimal configuration at the repo root:

```ini
StylesPath = .vale/styles
MinAlertLevel = suggestion
Packages = Google

[*.md]
BasedOnStyles = Vale, Google
```

Run `vale sync` to fetch the package into `.vale/styles`, then run `vale docs/`.

Coverage, mapped to these IDs (inferred; the package's rule names are Google's, not this skill's): roughly V2 to V5, V8, W4, W7, W8, and S1. That covers passive voice, "will", "please", "simply" and "just", contractions, e.g. and i.e., the word list, spelling and the serial comma, exclamation marks, and heading case.

Vale cannot check every R, A, N, I, and H rule, P11, S2 heading shape, S6 table semantics, S10 image-only information, or P1 step decomposition. Those still need a human pass. A green run is evidence for row 12, not a passing audit.

### The skill's machine pass

The skill ships its own configuration at `~/.claude/skills/tech-writer/vale/.vale.ini`, used only when the project has no `.vale.ini`. It adds the vale-ai-tells package and one custom style, `TechWriter`. Run `make vale-sync` in the skill's repo to download the packages, which are not committed.

The `TechWriter` AI-tell rules cover H1 (`Reversal`), H3 (`Teasers`), H5 (`DashSubstitutes`), H7 (`Significance`), H8 (`AIVocabulary`), H10 (`ChatbotArtifacts`), H14 (`SourceDisclaimers`), H19 (`NotabilityClaims`), H21 (`CurlyQuotes`), H25 (`NeedlessCount`), and H26 (`Staccato`). Its other rules port the mechanical checks of the ISO 24495 text audit (GaZmagik/iso-24495 v0.7.0) to Vale. For the I rules they cover I1 (`SentenceLength`, `SentenceAverage`), I2 (`ParagraphLength`), I3 (`PlainWords`, `WordyPhrases`), I7 (`DoubleNegatives`), and I14 (`HeadingDepth`). For the R and S rules they cover R6 (`FillerOpenings`), S2 (`HeadingLength`), S3 (`HeadingSkip`), S5 (`ProseEnumeration`), S6 (`TableHeader`), S9 (`LinkText`), and S10 (`ImageAlt`).

```ini
StylesPath = styles
MinAlertLevel = suggestion

Packages = Google, https://github.com/tbhb/vale-ai-tells/releases/download/v1.37.0/ai-tells.zip

[*.md]
BasedOnStyles = Vale, Google, ai-tells, TechWriter
```

Each mapped check is exact or a candidate. An exact alert is a finding unless it sits in a quotation, a proper name, or a passage that discusses the phrase (the AI tells exception in SKILL.md). A candidate alert is a finding only after you read the sentence and confirm the rule applies; discard it otherwise, and do not report discarded alerts.

| Vale check | ID | Kind |
|---|---|---|
| ai-tells.EmDashUsage, Google.EmDash | H5 | exact |
| TechWriter.DashSubstitutes | H5 | exact (candidate for the spaced hyphen: a minus sign in "5 - 3" is not a dash) |
| ai-tells.DoubleHyphen | H5 | candidate (a `--flag` outside backticks is a code-format finding, not H5) |
| ai-tells.OverusedVocabulary, ai-tells.OverusedVocabularyVerbs | H8 | exact (candidate for "robust": H8 covers only the figurative sense) |
| TechWriter.AIVocabulary | H8 | exact |
| ai-tells.PromotionalPuffery, ai-tells.StrategyBuzzwords | H9 | exact |
| ai-tells.ClosingPleasantries, ai-tells.SycophancyMarkers | H10 | exact |
| TechWriter.ChatbotArtifacts | H10 | exact |
| ai-tells.HollowAcknowledgment | H10 | candidate |
| ai-tells.ServesAsDodge | H20 | exact |
| TechWriter.CurlyQuotes | H21 | exact |
| TechWriter.NeedlessCount | H25 | candidate (keep limits, retries, versions, and totals of lists the reader cannot see) |
| ai-tells.ContrastiveNegation, ai-tells.StrawmanContrast, ai-tells.NegatedPair, ai-tells.ContrastiveFormulas | H1 | candidate |
| TechWriter.Reversal | H1 | candidate |
| TechWriter.Teasers | H3 | candidate |
| ai-tells.ParallelStaccato, TechWriter.Staccato | H26 | candidate (a short run of real steps or facts is fine) |
| ai-tells.SemicolonUsage, Google.Semicolons | H27 | exact |
| ai-tells.MicDrop, ai-tells.ConclusionMarkers | H2 | candidate |
| ai-tells.StackedHedges, ai-tells.HedgingPhrases | H6 | candidate |
| ai-tells.ConsequenceParticiple | H7 | candidate |
| TechWriter.Significance | H7 | candidate |
| TechWriter.SourceDisclaimers | H14 | candidate |
| ai-tells.Metacommentary, ai-tells.SelfReference, ai-tells.StructureAnnouncements | H11 | candidate |
| ai-tells.VagueAttributions | H19 | candidate |
| TechWriter.NotabilityClaims | H19 | candidate |
| ai-tells.MarketingHeadings, ai-tells.AnnouncementHeadings, ai-tells.ExplainerHeadings, ai-tells.WrapUpHeadings, ai-tells.MicDropHeadings | H22 | candidate |
| ai-tells.VerbTricolon | H4 | candidate |
| Google.Passive | V2 | candidate (the actor may be unknown or irrelevant) |
| Google.Will | V3 | candidate |
| Google.ExcessiveClaims | V5 | candidate |
| Google.Anthropomorphism | V6 | candidate |
| Google.Timeless | V7 | exact |
| Google.Latin | W4 | exact |
| Google.WordList, Google.WordListCase | W7 | candidate (the word list in voice-and-words.md and the local guide win over Google's) |
| Google.OxfordComma | W8 | candidate (it also fires on a comma before a trailing phrase that is not a list) |
| Google.Spelling, Vale.Spelling | W8 | candidate (product names and code terms are not misspellings) |
| Google.Headings | S1 | exact |
| Google.HeadingPunctuation | S3 | exact |
| TechWriter.SentenceLength | I1 | exact (candidate when a sentence ends in a link or a quotation, which Vale can join to the next sentence; words inside inline code are not counted, the ISO audit counts them) |
| TechWriter.SentenceAverage | I1 | candidate (reported on line 1, for documents of 10 or more sentences) |
| TechWriter.ParagraphLength | I2 | candidate (the period of an abbreviation counts as a sentence end; the limit in a reply is 4) |
| TechWriter.PlainWords, TechWriter.WordyPhrases | I3 | exact |
| TechWriter.DoubleNegatives | I7 | exact |
| TechWriter.HeadingDepth | I14 | exact |
| TechWriter.FillerOpenings | R6 | candidate (it checks every sentence; R6 covers the opening of a page or reply) |
| TechWriter.HeadingLength | S2 | candidate |
| TechWriter.HeadingSkip | S3 | candidate |
| TechWriter.ProseEnumeration | S5 | candidate |
| TechWriter.TableHeader | S6 | exact |
| TechWriter.LinkText | S9 | exact |
| TechWriter.ImageAlt | S10 | exact |
| Google.Acronyms | W3 | candidate (it checks 3 to 5 capitals; a term the reader knows needs no definition) |

Every other check is unmapped and dropped. That includes the remaining ai-tells checks (the `Figurative*` and `*Metaphors` families, `ColonUsage`) and the Google checks this skill has no rule for (`Parens`, `Quotes`, `Colons`, `Ellipses`). This skill uses colons to introduce code and lists, so a colon alert is never a finding.

Judgment only, no Vale check: H12, H13, H15, H16, H17, H18, H23, H24, and the vague-link part of H7 ("associated with"). H2, H3, and H4 alerts are candidates at most; the LLM pass still reads for them.

Source: Vale, vale-cli/Google package, tbhb/vale-ai-tells v1.37.0 (MIT).

---

## Worked mini-audit

The following README excerpt is for `shipd`, a fictional deploy CLI:

```markdown
# Getting Started With Shipd

Shipd is the fastest way to deploy your app. Currently, we are excited to
announce that our new dashboard will be shown once the user has logged in.

## Installing The CLI

Please simply run the install script below. After that you should click on the
Deploy button in order to deploy, and the status will be changed. For
configuration options, click here.

`curl -sL get.shipd.io | sh && shipd deploy --key=<your-key> --turbo`

| shipd deploy | shipd rollback |
| --- | --- |
```

Report header (full template in SKILL.md, section 9):

```
**Score:** 2/12 (5 or less band)   **Shippable:** no (Blocking below)
**Diagnostic:** 2/12, failed rows: 1 (no audience or outcome), 3 (`--turbo`
unverifiable), 4 (title case, "-ing" headings), 5 (steps in prose), 6 (no intro,
`<your-key>`), 7 ("we", passive, "please", "in order to"), 8 ("click here",
headerless table), 9 ("Currently", pre-announced dashboard), 11 ("fastest",
"excited to announce"), 12 ("log in")
```

**Findings:**

| # | Location | Rule (ID + name) | Before | After | Severity |
|---|----------|------------------|--------|-------|----------|
| 1 | Headings | S1 sentence case; S2 heading shape | "Getting Started With Shipd", "Installing The CLI" | "Get started with Shipd", "Install the CLI" | Medium |
| 2 | Intro | V7 timeless; V1 second person | "Currently, we are excited to announce..." | "After you sign in, the dashboard appears." | Medium |
| 3 | Intro | H9 sales language | "the fastest way to deploy your app" | "Shipd deploys an app from the command line." | Low |
| 4 | Install paragraph | V4 no please; V5 no simply | "Please simply run the install script" | "To install the CLI, run the following command:" | Low |
| 5 | Install paragraph | P1 numbered steps; W1 condition first | "you should click on the Deploy button" | "1. Click **Deploy**. The status changes to **Deploying**." | High |
| 6 | Command line | P7 colon intro; P8 placeholders | `--key=<your-key>`, no intro | `--key=API_KEY`, explained after the sample | Medium |
| 7 | `--turbo` flag | P11 facts verified in code | In no source file or help output | `TODO(verify): --turbo not in cmd/deploy.go` | **Blocking** |
| 8 | "click here" | S9 descriptive link text | "For configuration options, click here." | "see Configure Shipd" | High |
| 9 | Command table | S6 header row and intro | Commands used as the header row | Introductory sentence and a `Command` / `Description` header | High |

**Score.** Row 2 passes because a README is the right type for a first deploy. Row 10 passes because the excerpt explains no code. The other ten fail as the Diagnostic line lists.

That is **2/12**, the "5 or less" band: rewrite from the README skeleton. The doc stays `Shippable: no` until finding 7 is resolved.

Source: skill rule, a worked example of the rule IDs above.

Adapted from wondelai/skills technical-documentation (MIT) and the Google developer documentation style guide (CC BY 4.0). I rules come from iso-24495 skills (MIT, proxies, no ISO conformance claim). H rules come from Wikipedia:Signs of AI writing (WikiProject AI Cleanup advice page, CC BY-SA 4.0), which holds descriptive observations, not policy.
