# Document types

This file deepens SKILL.md, Know the reader and the document's job. It covers which document type fits a reader's question and the audience and scope statements that open a page. It also covers prerequisite and closing patterns, skeletons for the five common page types, body order, paragraph structure, and the self-editing pass for a full doc set. It owns rule IDs R1 to R6, I9, I13, I16, and I17.

## Document type choice (R2)

Every page answers one reader's question. Match the type to the question before you write a word. Mixing types on one page forces the reader to read everything to find their one task.

| Type | Reader's question | Signals it's the right type | Must not contain |
|---|---|---|---|
| Tutorial | "Walk me through building this, start to finish?" | Reader is new to the feature and wants one guaranteed win | Exhaustive option lists; alternate paths; unexplained jargon |
| How-to | "How do I do this one task?" | Reader already has a working setup and a specific goal | Onboarding scaffolding; the "why" behind the feature |
| Concept | "What is this, and why does it work this way?" | Reader wants a mental model before acting | Numbered steps; command output; UI clicks |
| Reference | "What are the exact parameters, fields, or flags?" | Reader already knows what they want and needs the exact facts | Narrative explanation; opinion; "why" content |
| README / getting started | "What is this, and how do I start?" | Reader is arriving for the first time, evaluating or installing | Deep conceptual explanations; exhaustive configuration matrices |

**One task per page (R2).** A page that answers two of these questions answers neither well. When a draft mixes types (a concept paragraph, then steps, then a reference table), split it along these lines. Do not add more headings to the same page.

This taxonomy is not in Google's guide itself. It is inferred from the guide's Procedures page and its concept-heading guidance (S2, structure-and-formatting.md), and generalized to the other common developer-doc shapes.

Source: procedures, headings (inferred taxonomy, R2)

## Audience and scope statements (R1, R4)

A page's first paragraph does two jobs before any instruction starts. It tells the reader whether they are on the right page, and it tells them what they can do afterward (R1). A scope and non-scope statement adds what the page deliberately leaves out, with a link to where that content lives (R4).

**Audience statement**
- Before: "This page describes the notification system."
- After: "This page is for backend developers adding Shipit webhook notifications to an existing service. It assumes you can deploy an HTTP endpoint and have admin access to a Shipit project."

**Scope and non-scope statement**
- Before: "This guide covers webhooks."
- After: "This guide shows how to subscribe to deployment events and verify webhook signatures. It doesn't cover configuring retry policies or building a custom event bus. See Webhook retry policies."

**"What you'll do" intro**
- Before: "Shipit is a deployment platform that many teams use to ship software faster and reduce risk across environments."
- After: "By the end of this page, you can configure Shipit to redeploy your app automatically whenever a build passes CI."

The non-scope sentence rescues a reader who followed a search result to the wrong page. Without it, they read the whole doc before they find that it doesn't cover their case. The non-scope names where to go instead: a related page, another language version, or a person to ask. Leave it out when no alternative exists.

Source: tech-writing/one "Documents" (R1, R4), ISO 24495-1 skill, know the reader (R1), and ISO 24495-5 skill, rule 9 (R4, working draft)

## More than one audience (I13)

When a page serves more than one audience, name the primary audience in the opening paragraph. The primary audience's needs decide every conflict about order, depth, and vocabulary. Serve the secondary audience with links or a short section, not by diluting the page.

- Before: "This runbook explains how to fail over the Shipit queue. Managers, auditors, and on-call engineers can use it."
- After: "This runbook is for the engineer running a Shipit queue failover, often at 3 a.m. It lists commands first and keeps background short. Auditors can find the control mapping in Failover audit evidence."

A runbook is written for the engineer running it at 3 a.m. first and for the auditing manager second.

Source: ISO 24495-1 skill, audiences (I13, proxy)

## Opening block (I16)

Open every document with the title, a one-line purpose, the primary audience, and a version or date. The purpose names the reader's task and the document's scope. The audience statement (R1) and the primary audience (I13) supply the reader line. With the version or date, a reader can check whether the page matches the software they run.

- Before: "# Queue failover" followed by three paragraphs of background.
- After:
  ```
  # Queue failover

  Fail over the Shipit queue to the standby region when the primary region is down. For planned moves, see Queue migration.

  For the on-call engineer. Version 2.3, 2026-05-04.
  ```

A README's title and first paragraph usually carry the purpose and the audience already. Add the version or date when the project publishes versions.

Source: ISO 24495-5 skill, rule 7 (I16, proxy, working draft)

## Overview (I17)

A document with 6 or more sections, or one whose conclusion readers need before the detail, gets an overview under its own heading, such as "Overview" or "Summary". That heading names the section, not its message, which agrees with S2. The overview keeps the conclusion, the action the reader must take, and any qualification that changes the action. A reader who stops there must still act correctly. Never mark the overview with bold text alone, because a listener reaches it only through the heading list.

- Before: a 9-section incident report that states the root cause and the required fix in section 7.
- After: an "Overview" section first: "An expired TLS certificate on the queue gateway caused the outage. Renew the certificate on every gateway before 2026-06-01. Gateways on version 1.x are not affected."

The ISO 24495-5 draft orders a document in three levels: overview, main body, and optional detail. When a technical explanation is the document, its purpose sentence (I9, stage 1) opens the overview, and stages 2 and 3 sit in the main body, in that order. Detail a reader can skip and still act on goes to an appendix or a collapsible block that the main path links to.

Source: ISO 24495-5 skill, rule 8, and ISO 24495-3 skill, rule 1 (I17, proxy, working draft)

## Prerequisites and closing (R3, R5)

**Before you begin (R3)** lists everything the reader needs before step 1, and nothing they discover along the way. It belongs there, not folded into step 4.

Belongs in prerequisites:
- Software and minimum versions ("Shipit CLI 4.2 or later")
- Required roles or permissions ("Admin role on the target project")
- Tools or SDKs that must already be installed
- Accounts, API keys, or a specific starting state ("A GitHub repository connected to Shipit")

Does not belong: conceptual background (link a concept page instead), and setup steps that belong to a different, already-linked page.

- Before: "4. Before running this command, make sure you've installed the Shipit CLI and have admin access on the project."
- After:
  ```
  ## Before you begin

  - Shipit CLI 4.2 or later
  - Admin role on the target project
  - A GitHub repository connected to Shipit
  ```

**Verification and What's next (R5).** A procedure that ends on the last action leaves the reader guessing whether it worked. Close with a verification step phrased as a check, with the expected output. Then point to the next task.

- Before: "4. Run `shipit deploy`. That's it, you're done."
- After:
  ````
  Confirm that the deployment succeeded:

  ```
  shipit status my-app
  ```

  The command prints `Status: healthy`.

  ## What's next

  - Configure automatic rollbacks
  - Send deployment events to Slack
  ````

The exact headings "Before you begin" and "What's next", and the "Confirm that..." verification phrasing, are not quoted rules in Google's guide. They are the convention this skill standardizes on, built from the guide's Procedures page and Google's own documentation practice.

Source: procedures; tech-writing/one "Documents" (R3, R5; heading wording and verification phrasing are convention)

## Skeletons (convention)

None of these page shapes are named in Google's guide. They are this skill's convention for applying R1 to R6 consistently. Use them as a starting outline, not a rigid template.

**README**
1. Project name and one-line purpose: what it does, in one sentence
2. Who it's for: the audience statement
3. Quick start: three steps (install, configure, run)
4. Links out: full docs, contributing guide, license

**Getting started (docs-site landing page)**
1. Title
2. What you'll do: the outcome statement (R1)
3. Before you begin: prerequisites (R3)
4. Install, first command, verify
5. What's next (R5)

**Tutorial**
1. Title stating the goal ("Build a webhook listener with Shipit")
2. What you'll build: one or two sentences, the end state
3. Before you begin: prerequisites (R3)
4. Numbered steps, each with the expected result stated after the action
5. Clean up: remove anything created only for the tutorial
6. What's next (R5)

**How-to**
1. Title as a bare imperative task ("Configure a webhook endpoint"). Heading form is S2 (structure-and-formatting.md)
2. One sentence of context, only if more than one approach exists
3. Before you begin: only what is specific to this task, not full onboarding
4. Numbered steps, condition before instruction
5. A short verification step (R5)

**Concept**
1. Title as a noun phrase ("Webhook signing"). Heading form is S2 (structure-and-formatting.md)
2. What it is: key point first (R6)
3. Why it works this way: the mechanism or trade-off
4. How it fits with other pieces
5. A link to the procedure that acts on this concept

Source: convention

## Progressive disclosure (I9)

For concept pages, reference pages, and code explanations, order the body in three stages. The order sets the body inside the doc-type skeleton above.

1. **Purpose:** one sentence on what the thing is and what it is for.
2. **Architecture and data flow:** a diagram or table, only when more than one component relates.
3. **Implementation detail:** the specifics, with file:line citations (I10, procedures-and-code.md).

Omit a stage that has no content. Keep the order of the stages that remain. A section that the document's genre needs sits beside the stages, not inside one: an incident report's timeline is its own section.

- Before: "The queue worker starts in `src/worker.rs:12-30`, reads from Redis, and, because Shipit wanted retries, uses a backoff table defined in `src/retry.rs:5-20`. The worker is the part of Shipit that delivers webhooks."
- After:
  ```
  The queue worker delivers webhooks to subscriber endpoints.

  | Component | Role |
  |---|---|
  | Redis stream | Holds pending deliveries |
  | Queue worker | Reads the stream and sends each delivery |
  | Retry table | Sets the delay between attempts |

  The worker starts in `src/worker.rs:12-30`. The retry table is in `src/retry.rs:5-20`.
  ```

A page with a single component skips stage 2 and goes from the purpose sentence to the detail.

Source: ISO 24495-3 skill, rule 1 (I9, proxy)

## Paragraphs and key points first (R6)

The page or reply opens with the answer or main point. Cut pleasantries and run-ups such as "Great question" or "This page will walk you through".

A paragraph carries one idea. Its lead sentence states that idea, and everything after supports it. Aim for three to five sentences. Put the information the reader needs before the background that explains it (R6). Voice and Words (I2) sets the same length target.

**Key information before background**
- Before: "Shipit's build system uses a layered cache to speed up repeated builds, an approach the team added after users on large monorepos reported slow CI times, and it now applies to every project by default."
- After: "Shipit caches build layers by default, so repeated builds finish faster. The team added this after users on large monorepos reported slow CI times."

**One idea per paragraph**
- Before: "Deployments run in isolated containers, so one project's build never affects another. You can also configure a custom domain for each environment, which requires DNS access and a verified certificate before Shipit will route traffic to it."
- After:
  ```
  Deployments run in isolated containers, so one project's build never
  affects another.

  You can configure a custom domain for each environment. This requires
  DNS access and a verified certificate before Shipit routes traffic to it.
  ```

A reader who skims only lead sentences should still get the page's argument. That is the test for whether the point comes first.

Source: tech-writing/one "Paragraphs" (R6), and ISO 24495-1 skill, rule 1 (no preamble) and rule 4 (front-loading) (R6, proxy)

## Self-editing and doc set organization

A single page needs a different check than a doc set spanning dozens of pages. Apply both.

**Self-editing a page:**

| Technique | What to do | Catches |
|---|---|---|
| Adopt the reader's persona | Reread as the stated audience, not as the author who already knows the system | Missing prerequisites, unexplained jargon |
| Read it aloud | Read every sentence out loud, one at a time | Run-ons, missing words, buried passive voice |
| Come back later | Leave a draft for a few hours or a day before the final pass | Errors invisible to a tired eye |
| Run the checklist | Walk the page against the Quick Diagnostic rows in SKILL.md | Systemic gaps a single read-through misses |
| Find a peer editor | Have someone unfamiliar with the feature follow the doc | Steps that only work because the author knows a hidden step |

**Organizing a doc set:**
- **Outline first.** Write the heading structure before any prose, and get it approved before you fill it in.
- **Purpose up front.** The landing page's first sentence says what the set covers, the same way a single page's first paragraph does (R1).
- **Headings as a table of contents.** A reader who reads only the headings across the set should be able to tell what is where and pick the right page.
- **Separate tutorials and how-tos.** A tutorial's teaching narrative and a how-to's task focus interfere with each other on the same page. This is R2's one-task-per-page rule applied across a whole set, not just one page.

Source: tech-writing/two "Self-editing" and "Organizing large documents"

## Worked example

A mixed page interleaves concept, steps, and reference. Here is one before a split:

```markdown
# Webhooks

Shipit webhooks let external services react to deployment events without
polling. Every payload is signed with an HMAC-SHA256 digest so subscribers
can verify the sender before trusting the contents; this became necessary
once webhook endpoints started appearing on the public internet, where
anyone could send forged events.

1. Open your project settings and click **Webhooks**.
2. Click **Add endpoint** and enter your HTTPS URL.
3. Copy the signing secret shown after you save.

The `event` field is one of `deploy.started`, `deploy.succeeded`, or
`deploy.failed`. The `signature` header holds the HMAC digest, and
`timestamp` is a Unix epoch integer used to reject replayed requests
older than five minutes.

4. Deploy your project and check your endpoint's logs for a request.
```

A reader who only wants to configure an endpoint has to read a security rationale and a payload reference to find steps 1 through 4, scattered across the page. Splitting by task (R2) gives two linked pages. The outlines show headings only, since the prose above already carries the content:

**Page 1, concept: "Webhook signing"**
1. Webhook signing
2. Why Shipit signs every payload
3. Payload fields (`event`, `signature`, `timestamp`): reference material about the payload sits with the concept, not the procedure
4. See "Configure a webhook endpoint" to set one up

**Page 2, how-to: "Configure a webhook endpoint"**
1. Configure a webhook endpoint
2. Before you begin: an HTTPS-reachable endpoint, admin role on the project
3. Numbered steps 1 to 3 (unchanged)
4. Confirm that your endpoint received a request: the stranded step 4 becomes a verification step, with the expected log line stated
5. What's next

Source: convention (applies R1 to R6 together)

Adapted from wondelai/skills technical-documentation (MIT) and the Google developer documentation style guide (CC BY 4.0); I rules from iso-24495 skills (MIT, proxies, no ISO conformance claim).
