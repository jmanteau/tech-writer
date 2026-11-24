# Structure and formatting

1. [Headings (S1, S2, S3)](#headings-s1-s2-s3)
2. [Lists (S4, S5)](#lists-s4-s5)
3. [Tables (S6)](#tables-s6)
4. [Notices (S7)](#notices-s7)
5. [Cross-references (S8)](#cross-references-s8)
6. [Link text (S9)](#link-text-s9)
7. [Images and alt text (S10)](#images-and-alt-text-s10)
8. [Numbers, dates, and units (S11)](#numbers-dates-and-units-s11-en)
9. [Text formatting summary (S12)](#text-formatting-summary-s12)
10. [Bold lead-ins (S13)](#bold-lead-ins-s13)
11. [Accessibility for any reader (I8)](#accessibility-for-any-reader-i8)
12. [Diagram text alternative (I12)](#diagram-text-alternative-i12)
13. [Heading depth (I14)](#heading-depth-i14)
14. [Table of contents (I15)](#table-of-contents-i15)
15. [Worked example](#worked-example)

This file deepens SKILL.md, Structure (headings, lists, tables, notices). It gives the full rule text, more before/after pairs, and the numbers, dates, and text-formatting rules that the skill summarizes. It owns **S1 to S13, I8, I12, I14, and I15**. Code-font specifics, placeholders, and UI-element bold live in `procedures-and-code.md` (P6, P8, P5). Paragraph rules live in `document-types.md` (R6).

## Headings (S1, S2, S3)

Headings are the reader's table of contents before they read a word of body text. A reader scans the heading list, finds their task, and jumps there. A heading that doesn't say what the section is about, or that breaks case or level conventions, breaks the scan.

### Sentence case (S1)

Capitalize the first word and proper nouns only. Leave common nouns lowercase even when a UI element shows them capitalized. Proper nouns, product and brand names, and code stay exactly as written: Google Cloud, Cascade, `README.md`.

- "Configuring The Database Connection" becomes "Configure the database connection"
- "API Reference For The Webhooks Endpoint" becomes "API reference for the Webhooks endpoint"

### Heading form (S2)

A concept heading is a short noun phrase that names the thing the reader is learning about: "Webhook lifecycle". A task heading over a procedure may be a bare imperative, the verb the reader performs: "Create a webhook". Nothing else is allowed:

- No sentence headings.
- No heading that opens with What, How, or Why.
- No claim as a heading (a heading names a topic, it does not assert a result).
- No "-ing" opener. A gerund hides whether the heading is a task or a concept.
- No wordplay, jokes, or puns.
- No term the page has not explained yet. A skimming reader meets the heading first.

ISO 24495-5 (working draft) asks for headings that state the section's message. This skill keeps noun phrases for concept sections, a deliberate departure: a noun phrase names the topic without asserting a result. Task headings meet both rules.

**Before and after pairs:**

- "What the delivery does well" becomes "Delivery strengths"
- "The three security GO conditions are not met yet" becomes "Unmet security Go conditions"
- "How we migrate the cluster" becomes "Cluster migration"
- "Understanding webhook retries" becomes "Webhook retries"
- "Creating a Webhook" (task, disguised as a gerund) becomes "Create a webhook"
- "Troubleshooting Deploy Failures" (task) becomes "Troubleshoot deploy failures"
- "Webhook Payload Format" (concept, wrong case) becomes "Webhook payload format"

On a wall-of-text page, insert a task heading wherever the task changes, for example "Install", "Configure", and "Verify".

### Levels, endings, and adjacency (S3)

Don't skip heading levels (H2 straight to H4 with no H3 in between). Screen readers announce level jumps as broken structure. Headings never end with a period. Also (inferred) avoid a heading immediately followed by another heading with no body text between them. A reader lands on the child heading with no idea what the parent section covers.

**Full outline, before:**

```markdown
# Cascade CLI Reference.

### Installing Cascade
#### Prerequisites
##### Supported platforms
### Deploying An App
### Troubleshooting Common Errors
```

Problems: a trailing period on the title. The outline jumps from H1 to H3 (no H2). "Prerequisites" is immediately followed by "Supported platforms" with nothing said in between. Every heading but the first is "-ing" and title case.

**After:**

```markdown
# Cascade CLI reference

## Install Cascade

### Prerequisites

Before you install Cascade, confirm you have Node.js 18 or later.

### Supported platforms

## Deploy an app

## Troubleshoot common errors
```

Source: headings, and ISO 24495-1 skill, house convention (single-topic headings, S2)

## Lists (S4, S5)

### Intro sentences and parallelism (S4)

Every list needs an intro sentence that is grammatically complete on its own and ends in a colon. A sentence that only works once you mentally append the first bullet ("Use the `--format` flag to:") breaks the moment an item doesn't start with a verb. Every item in a list takes the same grammatical form as the others: all imperatives, all nouns, or all noun phrases.

**Before (fragment intro, mixed forms):**

```markdown
Use the --format flag to:
- Print JSON
- Print YAML
- Print a table
```

**After (complete intro, parallel nouns):**

```markdown
The --format flag supports the following output types:
- JSON
- YAML
- Table
```

**Before (non-parallel steps):**

```markdown
Before you deploy, complete these steps:
- Installing the CLI
- You need an API key
- Configure the project
```

**After:**

```markdown
Before you deploy, complete these steps:
- Install the CLI
- Get an API key
- Configure the project
```

### Numbered, bulleted, and description lists (S5)

Three or more parallel items in a sentence become a list (ISO 24495-1). For example, "Set the region, the project ID, and the service account before you deploy." becomes an introductory sentence and three bullets. Number a list only when order matters: the reader must do item 1 before item 2. Everything else is bulleted, including options, flags, and requirements that stand independently of each other.

Keep each bullet to one paragraph with one idea, and nest bulleted lists at most 2 levels deep. Promote longer material to a subsection.

**Before (numbered, but the items aren't a sequence):**

```markdown
1. Enable verbose logging
2. Enable colorized output
3. Enable strict mode
```

**After:**

```markdown
- Enable verbose logging
- Enable colorized output
- Enable strict mode
```

For term-and-definition pairs, a description list beats a two-column table. The term reads as a heading, not a table cell, and there is no header row to skip. Markdown has no universal native syntax for this, but the widely supported Markdown Extra and Pandoc form is:

```markdown
`--dry-run`
:   Previews changes without applying them.

`--verbose`
:   Prints each step as it runs.
```

**Punctuation** `[EN]` (inferred): capitalize the first word of every item regardless of form. A complete sentence ends with a period. A fragment doesn't.

- Fragment, no period: "- Verbose output"
- Complete sentence, period: "- Verbose output is enabled by default."

Source: lists, ISO 24495-1 skill, house convention (lists, S5), and ISO 24495-5 skill, rule 4 (S5, working draft)

## Tables (S6)

A table needs a header row and an intro sentence that states what it lists, such as "The following table lists the `cascade deploy` flags:". A reader (and a screen reader) then knows what they are about to scan before they hit the grid.

Never merge cells and never leave one empty. An empty cell reads to assistive tech as if nothing is there at all, not as "not applicable". Write "None" or "Not applicable" instead (convention). Keep cell phrasing parallel down a column: if one description is a sentence, they all are.

Use a bulleted or description list instead of a table in two cases. One is a single dimension of comparison, such as a plain list of flags with no second attribute. The other is when most cells would carry long prose. A table earns its header row only when the data is genuinely tabular across two or more attributes. When readers compare 2 or more items across shared attributes, use a table rather than prose.

**Before:**

```markdown
| Flag | |
|------|--|
| --verbose | |
| --dry-run | Preview changes |
```

**After:**

```markdown
The following table lists the `cascade deploy` flags:

| Flag | Description |
|------|-------------|
| `--verbose` | Prints each step as it runs. |
| `--dry-run` | Previews changes without applying them. |
```

Source: tables, accessibility, and ISO 24495-5 skill, rules 4 and 6 (S6, working draft)

## Notices (S7)

A notice interrupts the reader's flow, so it earns that interruption only when the information changes what the reader does next.

- **Note:** useful, optional information the reader can act on or skip. "Cascade caches build artifacts in `.cascade/cache`. Delete this directory to force a clean build."
- **Caution:** proceed carefully; the mistake is recoverable but costly. "Changing the region after deployment migrates your database and can take up to 30 minutes."
- **Warning:** serious harm or irreversible loss. "Running `cascade reset --hard` permanently deletes all environments and can't be undone."

Don't stack them. (Inferred) one notice per section is a practical ceiling. Three boxes in a row train the reader to skip all three, including the one that matters.

Fold a notice into body text whenever it doesn't change the reader's next action. A plain sentence in the paragraph carries the same information without the visual interruption.

**Before:**

```markdown
Run `cascade deploy` to publish your app.

> **Note:** This command requires an active internet connection.
```

**After:**

```markdown
Run `cascade deploy` to publish your app. This command requires an internet connection.
```

Source: notices

## Cross-references (S8)

Point to other content with "see", never "refer to" or "check out". Never say "above" or "below". Pages reflow, get translated into languages that reorder content, and get read out of order by screen readers and search results. Use "the following" for what comes immediately after on the same page, "the preceding" for what came immediately before, and a named link for anything farther away.

Link when the referenced material lives on another page, or is optional depth the current task doesn't require. Inline the fact instead (repeat the one sentence the reader needs) when sending them away would interrupt a procedure they are midway through.

- "For more info, check out the docs above." becomes "For more information, see Configure authentication."
- "As mentioned below, you'll need an API key." becomes "You need an API key; see Get an API key."
- "Refer to the table above for exit codes." becomes "See the preceding table for exit codes."

Source: cross-references

## Link text (S9)

Link text should read as the destination's title, or a close description of it, so it makes sense pulled out of the sentence. Many screen readers list a page's links with no surrounding text at all. Never link "click here", "this link", or a bare pasted URL. Put the link on the words that name the target, not on a filler verb.

- "To learn about rate limits, click here." becomes "For rate limit details, see [Rate limits](#)."
- "Read more at https://docs.cascade.dev/webhooks." becomes "For webhook payload formats, see [Webhook payloads](#)."
- "This link explains how authentication works." becomes "See [How authentication works](#) for the full flow."

Source: link-text, accessibility

## Images and alt text (S10)

Alt text states what the image communicates in this context, not what it literally shows. Skip "Image of" and "Screenshot of", because the screen reader already announces that it is an image. Keep it to one concise phrase or sentence, not a full transcription of every pixel.

Information must never live only in an image. If a diagram is the sole place a required value, flag, or step appears, the doc is broken. It fails anyone who can't see the diagram and anyone who needs to copy that value. This is a shippability gate (Blocking): put the same fact in the surrounding text.

Use a screenshot to show where something sits in a UI or to confirm a visual result, such as a filled-in form or a chart the reader compares theirs against. Use text or a code block for anything the reader types, copies, or runs. Text is copyable, searchable, and translatable. A screenshot of a command is none of those.

Write the caption first: naming the figure's one idea before you draw or crop it keeps the image on message (tech-writing/two). Never let the caption alone carry a detail that is missing from the alt text.

**Before:**

```markdown
![Screenshot of the dashboard](dashboard.png)

Click the button to deploy.
```

**After:**

```markdown
![The Deploy button in the top-right corner of the Cascade dashboard, next to the environment selector](dashboard.png)

Click **Deploy** in the top-right corner of the dashboard.
```

Diagrams also need prose that says what they show (I12 below).

Source: images, accessibility

## Numbers, dates, and units (S11) `[EN]`

Spell out zero through nine. Use numerals for 10 and up. Always use numerals with units, versions, and measurements, no matter how small the number: "3 MB", "version 2 of the API", "5 retries".

Dates must be unambiguous: "2026-08-29" or "August 29, 2026", never "08/29/26" or "29/08/26", which read as different dates depending on the reader's locale. Include a time zone whenever a time matters across regions: "2:00 PM UTC", not "2:00 PM".

Units get a space and the standard symbol, never a spelled-out or invented abbreviation: "10 MB", not "10MB" or "10 megs". The time-zone and unit-spacing forms are inferred. The sourced pages cover number and date formats.

- "The free tier includes 3 projects and up to 100mb of storage." becomes "The free tier includes three projects and up to 100 MB of storage."
- "The migration finished on 08/09/26 at 2pm." becomes "The migration finished on 2026-08-09 at 2:00 PM UTC."
- "This feature requires SDK version two." becomes "This feature requires SDK version 2."

Source: numbers, dates-times

## Text formatting summary (S12)

| Format | Use for | Example |
|--------|---------|---------|
| **Bold** | UI element names, matching on-screen casing (P5); bold lead-ins on explanatory bullets (S13) | Click **Deploy**. |
| `Code font` | Commands, flags, filenames, code, values (P6) | Run `cascade deploy --dry-run`. |
| *Italics* | A new term on its first use; emphasis, used sparingly | A *webhook* is an HTTP callback that Cascade sends when an event occurs. |

Give each visual device one meaning per document. If bold marks UI names and lead-ins, it marks nothing else, and two devices never share one meaning.

Don't format product names. Write them as plain text, matching the vendor's own capitalization (P6). See `procedures-and-code.md` for the full code-font, placeholder, and UI-element rules behind P5 and P6.

Source: text-formatting, and ISO 24495-5 skill, rule 5 (S12, working draft)

## Bold lead-ins (S13)

On an explanatory bullet, bold the first 2 to 4 words that name the item, then write the explanation after them. The bold words let a skimming reader find the item. Use bold otherwise only for UI element names (S12, P5). Do not bold other words in prose, and do not bold whole sentences.

- Before: "- The retry table sets the delay between attempts and is read at worker start."
- After: "- **Retry table:** sets the delay between attempts. The worker reads it at start."

The bold lead-in is a skimming aid only. The bullet must still make sense when read straight through (I8).

Source: ISO 24495-1 skill, house convention (S13)

## Accessibility for any reader (I8)

The page must work read straight through and through a screen reader. No meaning may be carried by bold, colour, or position alone.

- Before: "The red rows in the following table failed. See the column on the right."
- After: "The following table lists each check. Rows with the status Failed need a fix. The Status column is the last column."

Also check that:
- Each link makes sense out of context (S9).
- Each image has alt text that states what it communicates (S10).
- Each table has a header row (S6).
- Heading levels do not skip (S3).
- Reading order is document order. A sidebar or a floating callout gets its own heading in the flow.

Source: ISO 24495-1 skill, intended readers (I8, proxy), and ISO 24495-5 skill, rules 5 and 6 (I8, working draft)

## Diagram text alternative (I12)

Put prose beside each diagram that says what the diagram shows, not what it is. A Mermaid or other diagram source is not a text alternative. A reader who cannot see the figure must get the same facts from the text.

- Before: "Figure 3: Architecture diagram."
- After: "Figure 3: The queue worker reads pending deliveries from the Redis stream, sends each to the subscriber endpoint, and writes the result back to the stream."

Keep the same symbol names in the prose and the diagram (I11, procedures-and-code.md).

Source: ISO 24495-3 skill, rule 4 (I12, proxy)

## Heading depth (I14)

Use at most 3 heading levels below the title, so `####` is the deepest. A fifth level means the section holds a hierarchy that a list or a table carries better, or a page that should be split. Flatten the deepest level into a list or a table, or move it to its own page.

- Before: "##### Supported platforms" under "#### Prerequisites".
- After: "#### Prerequisites", with the platforms as a bulleted list under it.

Number headings only when readers must cite a section by its number, and never below `####`.

Source: ISO 24495-5 skill, rule 1 (I14, proxy, working draft)

## Table of contents (I15)

A document with 6 or more sections gets a table of contents or a link list at the top. Word each entry exactly like the heading it points to, so a reader who jumps from the list finds the same words on arrival. The contents list at the top of this file is an example.

Source: ISO 24495-5 skill, rule 2 (I15, proxy, working draft)

## Worked example

**Before:** headings break case and nest wrong. The list has a fragment intro and non-parallel items. The table has no intro sentence and has empty cells. Two notices stack back to back:

```markdown
# Configuring Webhooks.

## Setting Up

To set up webhooks you can:
- signing secret
- Choose a delivery URL
- pick which events to send

## The Payload

Below is a table of fields you might get back:

| Field | |
|-------|--|
| event | |
| id | The event's ID |

Note: Webhook retries happen automatically.
Caution: If your endpoint returns a non-2xx status the delivery is marked failed and won't retry.
```

**After:** headings use sentence case (a bare imperative for the task, a noun phrase for the concept). One parallel bulleted list has a complete intro. The table has a header row and no empty cells. The routine fact is folded into body text, and a single notice remains:

```markdown
# Configure webhooks

## Set up a webhook

To set up a webhook, complete these steps:

- Generate a signing secret.
- Choose a delivery URL.
- Select which events to send.

## Webhook payload fields

The following table lists the fields in every webhook payload:

| Field | Description |
|-------|-------------|
| `event` | The event type, for example `payment.succeeded`. |
| `id` | The event's unique ID. |

Cascade retries a failed delivery up to five times before it gives up.

**Caution:** Changing the delivery URL cancels any retries already queued for the old URL.
```

Adapted from wondelai/skills technical-documentation (MIT) and the Google developer documentation style guide (CC BY 4.0); I rules from iso-24495 skills (MIT, proxies, no ISO conformance claim).
