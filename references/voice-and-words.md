# Voice and words

This file deepens SKILL.md, Voice (you, active, present, timeless) and Sentences and words. It owns rule IDs V1 to V10, W1 to W8, and I1 to I7. Cite these IDs in audit findings. S9 ("click here") and P8 (placeholders) are cited here but explained in their owner files.

## Contents
- [Second person](#second-person-v1) · [Active voice](#active-voice-v2) · [Present tense](#present-tense-v3)
- [Please, simply, and excessive claims](#please-simply-and-excessive-claims-v4-v5) · [Anthropomorphism](#anthropomorphism-v6)
- [Timeless documentation](#timeless-documentation-v7) · [Contractions \[EN\]](#contractions-en-v8)
- [Inclusive language](#inclusive-language-v9) · [Global audience](#global-audience-v10)
- [Condition before instruction](#condition-before-instruction-w1) · [Short sentences, one idea](#short-sentences-one-idea-w2) · [Sentence length](#sentence-length-i1)
- [Abbreviations](#abbreviations-w3-and-latin-abbreviations-en-w4) · [can/may/might \[EN\]](#canmaymight-en-w5)
- [Jargon](#jargon-w6) · [Word list \[EN\]](#word-list-en-w7)
- [American spelling and serial comma \[EN\]](#american-spelling-and-serial-comma-en-w8) · [Non-English documents](#non-english-documents)
- [Paragraphs](#paragraphs-i2) · [Familiar words and filler](#familiar-words-and-filler-i3) · [One term per concept](#one-term-per-concept-i4) · [Explicit connectors](#explicit-connectors-i5) · [Subject near verb](#subject-near-verb-i6) · [Positive framing](#positive-framing-i7)

## Second person (V1)

Address the reader as "you." Never use "we" or "the user" for the reader. "We" hides who has to act. "The user" turns the reader into a third party watching someone else's instructions.

Use "we" only for the writing team when it really acts. Default to the imperative for steps. The subject "you" is implied, not written.

| Avoid | Use instead | Why |
|---|---|---|
| "We recommend restarting the Nimbus CLI daemon after a config change." | "Restart the Nimbus CLI daemon after you change the config." | "We" hides who has to act |
| "The user must set an API key before calling the endpoint." | "Set an API key before you call the endpoint." | "The user" makes the reader a bystander in their own instructions |
| "You should click Deploy to start the build." | "Click **Deploy** to start the build." | Imperative drops the throat-clearing subject |

**The one allowed "we":** the writing team, or the team that owns the product, speaking as the actual actor (ISO 24495-1 direct address). It states what the team did or decided and does not give an instruction to the reader.
- Allowed: "We built the Vantage API to replace polling with webhooks." and "We deprecated the v1 endpoint."
- Not allowed: "We suggest you enable webhooks." becomes "Enable webhooks."

**"I" for the writer of a reply:** in a chat reply or a review comment, the writer is one person, so "I" names them ("I checked the logs").

Source: person, and ISO 24495-1 skill, direct address (V1, proxy)

## Active voice (V2)

**Spot it:** a form of "be" (is, was, are, were, been, being) followed by a past participle, with the actor missing or trailing in a "by" phrase.

| Passive | Active | Note |
|---|---|---|
| "The manifest is validated by the Kiln build server." | "The Kiln build server validates the manifest." | Actor is named, so there is no reason for passive |
| "Deployments are triggered when a tag is pushed." | "Pushing a tag triggers a deployment." | Actor recoverable, so rewrite active |

**Three allowed passive cases:**
1. Actor unknown: "The request was rejected by an upstream proxy." is allowed as "The request was rejected" when the Wayfinder SDK genuinely can't identify which proxy.
2. Actor irrelevant to the reader's task: "Sessions are rotated every 15 minutes." The reader needs the interval, not the internal job that does the rotating.
3. Actor deliberately secondary, to emphasize the object: "Expired records are purged nightly." The record is the point. Naming the cron job would bury it.

Before: "The `reaper` cron job in the Kiln scheduler purges expired records every night."

After: "Expired records are purged nightly."

Source: voice, and ISO 24495-1 skill, voice (V2, proxy)

## Present tense (V3)

Default to present tense for behavior. Reserve "will" for effects that are genuinely later than the action described, not for the next line of the same sequence.

| Rewrite to present | Legitimate "will" |
|---|---|
| "The server will send an ack." becomes "The server sends an ack." | "If you delete a project, Fleetlog will permanently remove its logs after a 90-day grace period." The effect is deferred by a stated delay, not immediate |
| "The Fleetlog service will purge logs older than 30 days nightly." becomes "The Fleetlog service purges logs older than 30 days nightly." | "After three consecutive failed health checks, the load balancer will mark the instance unhealthy." A threshold-triggered future event |

Rule of thumb: if the result follows directly from the action in the same step, use present tense. If it arrives after a stated delay or a later condition, "will" is accurate.

Source: tense

## Please, simply, and excessive claims (V4, V5)

**"Please" (V4):** omit it from instructions. Reserve it for asking the reader's permission or forgiveness, not for softening a command.
- "Please click Save to persist your changes." becomes "Click **Save** to persist your changes."
- Allowed: "Please allow up to 24 hours for DNS changes to propagate." This asks for patience and does not issue a step.

**"Simply / easily / just / quickly" (V5):** omit them. They grade the reader's experience for them. If a step really is easy, the reader notices without being told.
- "Just add the `--watch` flag to simply enable live reload." becomes "Add the `--watch` flag to enable live reload."

**Superlatives, absolutes, and competitor comparisons:** cut them, or replace them with a verifiable, specific claim.

| Avoid | Use instead |
|---|---|
| "The fastest way to deploy" | "One way to deploy", or a stated number: "deploys in under 10 seconds on the free tier" |
| "Never loses a message" | "Retries delivery up to five times before moving the message to a dead-letter queue" |
| "Faster than Relay's queue" | Cut the comparison, or link to a published benchmark |

Source: tone, excessive-claims

## Anthropomorphism (V6)

Software doesn't want, see, think, know, tell, or complain. Name what actually happens.

| Avoid | Use instead | Example |
|---|---|---|
| wants | requires, needs | "The build script wants a `NODE_ENV` value." becomes "The build script requires a `NODE_ENV` value." |
| sees | detects | "The linter sees an unused import." becomes "The linter detects an unused import." |
| thinks | determines, evaluates | "The scheduler thinks the job is stuck." becomes "The scheduler determines the job is stuck after a 10-minute timeout." |
| knows | stores, has | "The cache knows the last ETag." becomes "The cache stores the last ETag." |
| tells | notifies, reports | "The webhook tells the queue the job failed." becomes "The webhook reports the failure to the queue." |
| complains | returns an error, logs | "The parser complains about invalid syntax." becomes "The parser returns a syntax error." |

Source: anthropomorphism

## Timeless documentation (V7)

Cut "currently," "now," "new," "soon," and "at the time of writing." A doc that never refers to today stays correct for as long as the behavior holds. A doc anchored to today starts rotting the day it ships.

| Avoid | Use instead |
|---|---|
| "Currently, the Cortex API rate-limits requests to 100/min." | "The Cortex API rate-limits requests to 100/min." |
| "This new dashboard shows deploy history." | "The dashboard shows deploy history." |
| "Soon you'll be able to export CSV." | Cut it. Document only what has shipped |

**Never pre-announce.** A feature that isn't released yet doesn't belong in the docs, even hedged as "coming soon."

**Version differences are not a timeless-docs violation.** They name a fact tied to a version number, not to the calendar:
- "In Nimbus CLI 2.x and later, `--dry-run` prints a diff before applying changes." This is fine, because the boundary is the version, not "now."

Source: future, timeless-documentation

## Contractions [EN] (V8)

Contractions read as conversational, not sloppy, and Google's guide allows them. For negations, prefer the contraction over the two-word form.

| Prefer | Over |
|---|---|
| isn't | is not |
| don't | do not |
| won't | will not |

- "The API key is not valid for staging." becomes "The API key isn't valid for staging."
- "Do not delete the retention record." becomes "Don't delete the retention record."

Source: contractions

## Inclusive language (V9)

| Avoid | Use instead |
|---|---|
| master / slave | primary / replica, controller / worker |
| blacklist / whitelist | denylist / allowlist (or blocklist / safelist) |
| sanity check | final check |
| dummy (variable, value) | placeholder |
| crazy | unexpected, erratic |
| cripple | disable, degrade |
| guys | everyone, team, folks |
| he / she (generic) | they |

**Fix pairs together.** Replacing only "blacklist" with "denylist" while leaving "whitelist" untouched keeps the asymmetry the swap was meant to remove. Change both halves of a pair in the same edit, even when only one half appears on the page in front of you.

**Gender-neutral "they":** use it for a person of unspecified gender, singular or plural, instead of switching to "he or she" or alternating pronouns.
- "A developer must configure his API key before deploying." becomes "A developer must configure their API key before deploying."

Source: inclusive-documentation

## Global audience (V10)

| Avoid | Use instead | Why |
|---|---|---|
| "Once you deploy the service, health checks start." | "After you deploy the service, health checks start." | "Once" reads as a time word in some dialects and a conditional in others |
| "This endpoint hits the ground running with zero config." | "This endpoint works with no configuration." | Idioms don't translate |
| "Configure it like setting up a Thanksgiving dinner. Plan ahead." | Cut the analogy; describe the steps directly | Culture-bound reference |
| "the customer order fulfillment status notification service" | "the service that notifies customers about fulfillment status" | Long noun stacks don't parse for non-native readers |
| "The team, the config file having been updated, redeployed." | "The team updated the config file, then redeployed." | Keep subject-verb-object order |

Date, time, currency, and number formatting for a global audience are S11 (structure-and-formatting.md). This section covers sentence-level and word-choice habits only.

Source: translation, global-audience

## Condition before instruction (W1)

State the condition or goal first, so the reader can tell whether the step applies to them before they act on it.

1. "Click **Delete** if you want to remove the workspace." becomes "To remove the workspace, click **Delete**."
2. "Restart the Anchor auth service after you edit `config.yaml`." becomes "After you edit `config.yaml`, restart the Anchor auth service."
3. Multi-condition: "Retry the request if the response is a 503 and a `Retry-After` header is present, and otherwise fail immediately." becomes "If the response is a 503 and includes a `Retry-After` header, retry the request. Otherwise, fail immediately."

Source: sentence-structure

## Short sentences, one idea (W2)

One clause, one idea. When a sentence accumulates a "which" clause, a comma-and, and a second instruction, split it into separate sentences. Sentence length targets are in I1 below.

Before: "The Vantage API returns a 429 status code when you exceed the rate limit, which is 100 requests per minute for free-tier accounts, and you should back off using the Retry-After header."

After: "The Vantage API returns a 429 status code when you exceed the rate limit. Free-tier accounts are limited to 100 requests per minute. Back off using the value in the `Retry-After` header."

**Convert a "which" clause into a list when it enumerates items:**

Before: "The deploy command validates the manifest, which checks the schema, the image tag, and the resource limits."

After: "The deploy command validates the manifest. It checks:
- The schema
- The image tag
- The resource limits"

Source: tech-writing/one "Short sentences", and ISO 24495-1 skill, sentence limits (W2, proxy)

## Sentence length (I1)

Keep the document average between 15 and 20 words per sentence. No sentence may run over 30 words. Each sentence carries one main idea (W2). Short runs of short sentences are fine. A page of only 5-word sentences reads as choppy, so vary the length inside the limit.

Code blocks, commands, logs, and quotations are exempt from these limits (ISO 24495-1 and 24495-3 skills, scope).

- Before (38 words): "When the Shipit worker cannot reach the subscriber endpoint within the timeout window, which defaults to ten seconds, it records a failed attempt and schedules the next delivery according to the retry table."
- After (13 and 14 words): "If the subscriber endpoint doesn't answer within ten seconds, the Shipit worker records a failed attempt. It then schedules the next delivery from the retry table."

Source: ISO 24495-1 sentence limits (I1, proxy)

## Abbreviations (W3) and Latin abbreviations [EN] (W4)

**First use:** spell out the term with the abbreviation in parentheses, then use the abbreviation for the rest of the page.
- "Configure the command-line interface (CLI) before running the first build. The CLI reads `~/.nimbusrc` on startup."

**Universally known exceptions:** skip the spell-out for terms every reader already knows, such as URL and HTML, and similarly ubiquitous ones (inferred: API, CPU).

**Latin abbreviations** don't translate and scan poorly in the middle of a sentence. Spell out the meaning instead.

| Avoid | Use instead |
|---|---|
| e.g. | for example |
| i.e. | that is |
| etc. | omit, or finish the list |
| vs. | versus, or "compared with" |
| cf. (inferred) | see, or compare |

Source: abbreviations, word-list

## can/may/might [EN] (W5)

| Modal | Meaning | Example |
|---|---|---|
| can | ability | "Free-tier accounts can make up to 100 requests per minute." |
| may | permission | "You may cache a response for up to 60 seconds." |
| might | possibility | "The migration might take several minutes for databases over 10 GB." |

Don't use "may" for possibility. "The build may fail" reads as the build having permission to fail. Use "might."

Source: word-list

## Jargon (W6)

Jargon is a defect only for the reader who doesn't have it. Define, link, or replace it based on the reader named at intake.

| For this reader | Do this |
|---|---|
| Experienced backend engineers | Use the term as-is: "The write is idempotent." |
| Mixed technical audience | Define inline on first use: "The write is idempotent: repeating it produces the same result." |
| Non-technical or new readers | Link to a concept page, or replace with plain language: "Repeating the request is safe; it won't create duplicates." |

Source: jargon

## Word list [EN] (W7)

"Click here" is not a word-list row. It is rule S9 (structure-and-formatting.md), a link-text defect, not a word choice.

Entries owned by their own rule are not repeated here: please (V4), just/simply (V5), e.g./i.e./etc. (W4), the inclusive-language pairs (V9), and once to after (V10) live in their sections. Filler trims such as "in order to" are also in I3.

| Avoid | Use instead | Why |
|---|---|---|
| above / below | preceding / following | Breaks on reflow, print, and translation |
| abort / kill | stop, cancel, end | Violent connotation |
| log in | sign in (unless the product itself says "log in") | Google's preferred term |
| setup (as a verb) | set up | "Setup" is the noun; "set up" is the verb |
| check box | checkbox | One word |
| and/or | pick one | Ambiguous |
| in order to | to | Wordy |
| desire | want | Plainer |
| leverage | use | Jargon |
| utilize | use (inferred) | Plainer |
| pop-up / dialog box | dialog | Google's preferred term |
| e-mail | email (don't use it as a verb) | Modern spelling; not a verb |
| Internet | internet | Common noun now |
| back-end / front-end | backend / frontend | One word, no hyphen |
| file name | filename | One word |
| Id / id | ID | Always capitalized |
| admin | administrator (except literal UI labels) | Plainer, except where the UI itself reads "Admin" |
| application | app (for end-user programs) | Google's preferred term in consumer contexts |
| click and drag | drag | Simpler |
| via | through, by using | Latin-derived; doesn't localize |
| allows you to | lets you / you can | Wordy |
| wish | want | Plainer |
| terminate | end, stop | Plainer |
| enable (a person) | let, lets | "Enable" a feature, not a person |
| display (intransitive) | appears | "Display" needs an object |
| execute | run | Plainer |
| illegal | invalid, not allowed | "Illegal" implies law-breaking |
| foo / bar | meaningful names in samples | Realistic names read better and copy-paste safely |
| Note that | omit | Filler opener |
| going forward | omit | Filler; also a timeless-docs violation |
| it's / its | "it's" only for "it is"; "its" is possessive | Commonly confused |
| toggle (as a verb) | turn on, turn off | Plainer |
| uncheck | clear | Google's UI term |
| unselect | deselect | Google's UI term |

Source: word-list

## American spelling and serial comma [EN] (W8)

| UK | US (use this) |
|---|---|
| colour | color |
| behaviour | behavior |
| licence (noun) | license |
| centre | center |
| optimise | optimize |

**Serial comma:** place a comma before the final "and" or "or" in a list of three or more.
- "Install the CLI, configure the API key and run the migration." becomes "Install the CLI, configure the API key, and run the migration."

Source: highlights, commas

## Non-English documents

The authoritative split is in [audit-checklist.md](audit-checklist.md), "Non-English documents". The `[EN]` rules are skipped: contractions (V8), Latin abbreviations (W4), can/may/might (W5), the word list (W7), and spelling and the serial comma (W8). Every other rule in this file applies in any language. That includes spelling out abbreviations (W3) and the I rules. The one exception is the English word pairs in I3.

Never translate a document unless asked (skill rule). Edit or write in the language the source already uses, and flag translation as a separate task if one looks needed.

## Paragraphs (I2)

A paragraph has 3 to 5 sentences, one topic, and its main point first. A shorter paragraph is fine, and a one-sentence paragraph is fine for a single important point. A paragraph in a reply has 4 sentences or fewer. Split a paragraph when the topic changes. Document types (R6) shows the same rule with examples for page structure.

- Before: "Shipit retries failed webhook deliveries up to five times. Each retry waits longer than the last. Signing secrets rotate every 90 days, and old secrets stay valid for 24 hours after rotation. You can rotate a secret by hand from the project settings page."
- After: "Shipit retries failed webhook deliveries up to five times. Each retry waits longer than the last.

Signing secrets rotate every 90 days, and old secrets stay valid for 24 hours after rotation. You can rotate a secret by hand from the project settings page."

Source: ISO 24495-1 paragraph limits (I2, proxy)

## Familiar words and filler (I3)

Use the short, common word. Cut filler phrases that add no meaning.

| Avoid | Use instead |
|---|---|
| in order to | to |
| due to the fact that | because |
| in the event that | if |
| at this point in time | now |
| utilise / utilize | use |
| commence | start |
| prior to | before |

- Before: "In order to rotate the secret, commence the rotation prior to the expiry date, due to the fact that expired secrets reject all requests."
- After: "To rotate the secret, start the rotation before the expiry date, because expired secrets reject all requests."

Source: ISO 24495-1 wording (I3, proxy)

## One term per concept (I4)

Pick one term for each concept and repeat it. Do not vary the word for style. A reader who sees a new word assumes a new thing. This also applies to UI labels, API names, and product names.

- Before: "Create a webhook. The subscription must have an HTTPS URL. If the listener returns an error, Shipit retries the hook."
- After: "Create a webhook. The webhook must have an HTTPS URL. If the webhook returns an error, Shipit retries the delivery."

Source: ISO 24495-1 wording (I4, proxy)

## Explicit connectors (I5)

State the relation between two ideas with a word such as because, therefore, if, before, or after. Do not leave the reader to infer it.

- Before: "The secret is rotated. Old deliveries fail verification."
- After: "After Shipit rotates the secret, old deliveries fail verification."

- Before: "Use the new secret. Requests are rejected."
- After: "Use the new secret, because Shipit rejects requests signed with the old one."

Source: ISO 24495-1 wording (I5, proxy)

## Subject near verb (I6)

Keep the subject close to its verb. Do not wedge a clause between them. Move the extra detail before the subject or after the verb.

- Before: "The Shipit worker, after it finishes reading the stream and checking each message against the retry table, sends the delivery."
- After: "After it reads the stream and checks each message against the retry table, the Shipit worker sends the delivery."

Source: ISO 24495-1 proximity (I6, proxy)

## Positive framing (I7)

Say what to do, unless the warning itself is the point. A positive instruction is shorter and has one reading.

- Before: "Do not forget to verify the signature before you parse the body."
- After: "Verify the signature before you parse the body."

A warning stays negative when the harm is the point: "Don't commit the signing secret to source control. Anyone with the secret can forge events."

Source: ISO 24495-1 wording (I7, proxy)

Adapted from wondelai/skills technical-documentation (MIT) and the Google developer documentation style guide (CC BY 4.0); I rules from iso-24495 skills (MIT, proxies, no ISO conformance claim).
