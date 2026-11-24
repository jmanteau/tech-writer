# Release notes, changelogs, and migration guides

A changelog is read with a version bump half-typed. This file owns rules **N1 to N6**: the file skeleton, the entry pattern, breaking-change placement, deprecation wording, and the migration-guide procedure. Structure comes from Keep a Changelog. The sentences inside each entry follow the same rules as the rest of the docs set. Examples use a fictional analytics client, Meridian SDK (`meridian-js`) and its CLI `meridian`.

## Table of contents

- [Changelog readers](#changelog-readers)
- [Keep a Changelog skeleton (N1, N2)](#keep-a-changelog-skeleton-n1-n2)
- [Entry format (N3)](#entry-format-n3)
- [Breaking changes (N4)](#breaking-changes-n4)
- [Deprecations (N5)](#deprecations-n5)
- [Google language layer on entries](#google-language-layer-on-entries)
- [Release notes and changelog compared](#release-notes-and-changelog-compared)
- [Migration guides (N6)](#migration-guides-n6)

## Changelog readers

The reader is upgrading. They arrived from a dependency-bot pull request, a pinned version they are about to unpin, or a bug that appeared after someone else upgraded. They read one version block, maybe two, and leave. They bring three questions:

| Reader question | The entry answers it with | The entry fails when it says |
|---|---|---|
| What changed? | The named API, flag, file, or behavior | "Various fixes and improvements" |
| Does it affect me? | The condition under which behavior differs | "Refactored the query internals" |
| What do I do? | The concrete action, or nothing at all | "See the diff for details" |

A generated commit log answers none of them. It is written for the committer, with one line per commit rather than per user-visible change. It names internal modules the reader never imports, and it has no impact statement because the author already knew the impact.

**Before:** the release section pasted from `git log --oneline`:

```markdown
## 4.0.0

- 8f21c0a refactor(query): normalize ordering in the planner
- 3ac9e14 Merge pull request #791 from meridian-labs/query-order
- b92ee05 fix sync
```

**After:** one entry per user-visible change, carrying impact and action:

```markdown
### Changed

- `meridian.query()` returns rows in ascending `timestamp` order instead of
  insertion order. If your code depended on insertion order, sort explicitly
  with `orderBy('_ingested')`. ([#791](https://github.com/meridian-labs/meridian-js/pull/791))
```

The filter: a change belongs in the changelog when a reader could notice it without reading your source. Internal refactors, test additions, and CI edits stay out.

Source: keepachangelog.com

## Keep a Changelog skeleton (N1, N2)

Keep one `CHANGELOG.md` at the repository root. Order versions newest first, keep an `[Unreleased]` section on top, date each released version in ISO format, and group entries under the six category sub-headings:

````markdown
# Changelog

All notable changes to Meridian SDK are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `meridian.events.replay()` reprocesses stored events from a saved cursor, so
  you can rebuild a downstream table without re-sending traffic. ([#812](...))

## [4.0.0] - 2026-08-14

### Added

- `meridian.events.record()` stores an event and returns the stored record,
  including the server-assigned `id`. ([#755](...))

### Changed

- **Breaking:** `meridian.query()` returns rows in ascending `timestamp` order
  instead of insertion order. Sort explicitly with `orderBy('_ingested')` to
  keep the old order. See [Migrate from 3.x to 4.0](docs/migrate-3-to-4.md).
  ([#791](...))

### Removed

- **Breaking:** `meridian.track()` is removed. Call
  `meridian.events.record()`, which accepts the same payload. Deprecated in
  3.4.0. See [Migrate from 3.x to 4.0](docs/migrate-3-to-4.md). ([#803](...))

### Fixed

- `meridian sync` no longer drops events when the connection times out
  mid-batch; an interrupted batch restarts from the last acknowledged offset.
  Affects 3.1.0 through 3.4.0. ([#799](...))

## [3.4.0] - 2026-06-30

### Added

- `meridian query` accepts `--output json` and prints one JSON object per row,
  so you can pipe results into `jq`. ([#780](...))

### Deprecated

- `meridian.track()` is deprecated in favor of `meridian.events.record()` and
  is removed in 4.0.0. Both accept the same payload; `record()` returns the
  stored event instead of `undefined`. ([#755](...))

### Security

- Upgraded `node-fetch` to 3.3.2, which fixes redirect handling that could
  forward the `Authorization` header to a third-party host (CVE-2026-31488).
  Upgrade if you set a custom `baseUrl`. ([#807](...))

[Unreleased]: https://github.com/meridian-labs/meridian-js/compare/v4.0.0...HEAD
[4.0.0]: https://github.com/meridian-labs/meridian-js/compare/v3.4.0...v4.0.0
[3.4.0]: https://github.com/meridian-labs/meridian-js/compare/v3.3.0...v3.4.0
````

The rules the skeleton encodes:

| Rule | Do | Avoid |
|---|---|---|
| Order | Newest version first, `[Unreleased]` above it | Oldest at the top |
| Dates | `## [4.0.0] - 2026-08-14` | `Aug 14, 2026`, `08/14/26`, no date |
| Categories | Added, Changed, Deprecated, Removed, Fixed, Security, in that order | Invented headings such as `### Misc` |
| Empty categories | Omit a category with no entries this release (convention) | Shipping `### Fixed` with nothing under it |
| Duplicates | One category sub-heading per version | Two `### Added` blocks in one version |
| Links | Bracketed headings resolved by compare links at the bottom | Bare version numbers, no diff link |

At release time, move the `[Unreleased]` entries under a dated heading, add the compare link, and repoint `[Unreleased]` at the new tag.

Source: keepachangelog.com

## Entry format (N3)

An entry is one sentence, or two, in this shape:

> **what changed** (named in code font) + **what it means for you** (the condition, the new behavior) + **what to do** (the action, or nothing) + **link** (issue or pull request, in parentheses at the end).

The impact clause is what commit messages never carry and what the reader came for. Drop it only when the change is self-evidently free.

Per category, commit-message-style line (`-`) and entry (`+`):

```markdown
Added
- feat(query): add json output
+ `meridian query` accepts `--output json` and prints one JSON object per row,
  so you can pipe results into `jq`. ([#780](...))

Changed
- refactor(query): normalize ordering in the planner
+ `meridian.query()` returns rows in ascending `timestamp` order instead of
  insertion order. If your code depended on insertion order, sort explicitly
  with `orderBy('_ingested')`. ([#791](...))

Deprecated
- deprecate track()
+ `meridian.track()` is deprecated in favor of `meridian.events.record()` and
  is removed in 4.0.0. Both accept the same payload. ([#755](...))

Removed
- remove legacy auth flag
+ The `--legacy-auth` flag is removed from `meridian login`. Sign in with
  `meridian login --token TOKEN`, or set `MERIDIAN_TOKEN`. Deprecated in
  3.2.0. ([#803](...))

Fixed
- fix sync
+ `meridian sync` no longer drops events when the connection times out
  mid-batch; an interrupted batch restarts from the last acknowledged offset.
  Affects 3.1.0 through 3.4.0. ([#799](...))

Security
- chore: bump node-fetch
+ Upgraded `node-fetch` to 3.3.2, which fixes redirect handling that could
  forward the `Authorization` header to a third-party host (CVE-2026-31488).
  Upgrade if you set a custom `baseUrl`. ([#807](...))
```

Four habits keep entries usable:

- **One change per entry.** A pull request that adds a flag and fixes a bug produces two entries in two categories.
- **Affected versions in a `Fixed` entry.** Name them when the bug shipped in several releases. That is how a reader on 3.2.0 learns the fix is for them.
- **Link last.** Write it as `([#799](url))`. Mid-sentence links break the scan.
- **Entry written with the change.** Do not write it at release time. Reconstructed impact statements are guesses.

Source: keepachangelog.com

## Breaking changes (N4)

Keep a Changelog does not prescribe a marker for breaking changes, so the placement and prefix below are a **(convention)**. Adopt one form and hold it across the file.

1. **First in the version.** Breaking entries lead their category, and the categories holding them lead the version. A reader who stops after five lines has still seen everything that can break their build.
2. **One consistent marker.** `**Breaking:**` at the start of the entry is a common form. It keeps the entry inside its Keep a Changelog category, so tools that parse the six headings still work. A separate `### Breaking changes` heading is outside the six and breaks those tools.
3. **Named migration steps.** Put them inline when they fit in a clause, otherwise link to the guide. "This is a breaking change" with no action is a warning, not documentation.
4. **Never buried in Changed.** A behavior change that silently alters results is breaking even when the signature is untouched.

**Before:** breaking and non-breaking entries interleaved, no marker, no action:

```markdown
### Changed

- Improved logging output for the sync command.
- Query results are now ordered differently.
- Renamed some internal helpers.
```

**After:** marked, first, with the action and the guide:

```markdown
### Changed

- **Breaking:** `meridian.query()` returns rows in ascending `timestamp` order
  instead of insertion order. Sort explicitly with `orderBy('_ingested')` to
  keep the old order. See [Migrate from 3.x to 4.0](docs/migrate-3-to-4.md).
  ([#791](...))
- `meridian sync` prints the batch offset with each progress line. ([#786](...))
```

For a release with several breaking changes, add a short **Upgrade notes** paragraph under the version heading, above the first category. List the changes in the order a reader should handle them, and link the guide once **(convention)**.

Source: convention

## Deprecations (N5)

A deprecation entry names three things. The first is the **replacement**: the exact API, flag, or option to call instead. The second is the **removal version or date** (`4.0.0`, or `2027-01-15` for a service). The third is the **difference**, when the replacement is not a drop-in.

**Before:**

```markdown
### Deprecated

- `meridian.track()` is deprecated.
```

**After:**

```markdown
### Deprecated

- `meridian.track()` is deprecated in favor of `meridian.events.record()` and
  is removed in 4.0.0. Both accept the same payload; `record()` returns the
  stored event instead of `undefined`. See
  [Migrate from track() to events.record()](docs/migrate-track-to-record.md).
  ([#755](...))
```

Keep the entry in place until removal. A reader jumping from 3.1.0 to 4.0.0 reads the 3.4.0 block on the day it stops being true. When the removal lands, write a `Removed` entry that points back to the deprecation ("Deprecated in 3.4.0").

The changelog entry, the deprecation note in the API reference (**A5**, [api-reference.md](api-reference.md)), and any runtime warning must name the same replacement and the same removal version. A mismatch is a factual defect, not a style one.

Source: keepachangelog.com, api-reference-comments

## Google language layer on entries

Entries are documentation, so the docs-set rules apply inside them. Tense needs one local decision. Category headings already carry a tense ("Added"), so entries read as fragments or as sentences about the API. Pick one form per file under **V3** ([voice-and-words.md](voice-and-words.md)): verb-first present ("Adds a `--dry-run` flag..."), subject-first present ("`meridian sync` accepts `--dry-run`..."), or simple past ("Added a `--dry-run` flag..."). Keep it for every entry in every version.

Four rewrites (`-` is the weak entry, `+` the fixed one):

```markdown
V1 second person for actions ([voice-and-words.md](voice-and-words.md))
- Users should update their config file, and the client will then reconnect.
+ Update `meridian.config.js` to set `retries`. The client reconnects on the
  next run.

V5 no unquantified "improved", "better", "enhanced" ([voice-and-words.md](voice-and-words.md))
- Greatly improved query performance and better error handling.
+ `meridian.query()` streams results instead of buffering them, which holds
  memory flat for result sets above 10,000 rows. Failed queries raise
  `QueryError` with the failing SQL in `error.query`.

V7 timeless: no "new", "currently" ([voice-and-words.md](voice-and-words.md))
- New: the SDK currently supports Deno, with more runtimes coming soon.
+ Adds Deno support. Import from `npm:meridian-js@4`.

P6 code font ([procedures-and-code.md](procedures-and-code.md)) + W7 word list [EN]
- Fixed the bug where users couldn't log in via the api using the --token
  flag, e.g. in CI.
+ `meridian login --token` no longer fails when `HOME` isn't set, for
  example in container builds. ([#788](...))
```

The last pair also applies the word list `[EN]`: sign in rather than log in, through rather than via, "for example" rather than "e.g." Entries are short. A single stray "simply" is the loudest word on the page.

Source: person, tense, excessive-claims, timeless-documentation, code-in-text, word-list

## Release notes and changelog compared

Two artifacts, two readers **(convention)**. A project can ship one, the other, or both:

| | Changelog | Release notes |
|---|---|---|
| Scope | Every user-visible change | The handful that matter this release |
| Shape | Categorized list, all versions in one file | Narrative page or post, one per release |
| Reader | Upgrading developer checking for impact | Anyone deciding whether to upgrade |
| Sections | Added / Changed / Deprecated / Removed / Fixed / Security | Highlights, upgrade notes, known issues |
| Cadence | Every release, including patches | Notable releases; patches often skipped |
| Home | `CHANGELOG.md` in the repository | Docs site, GitHub release, blog |

Ship both when a release carries more context than a list holds: a rewritten subsystem, a quota change, a migration with a deadline. Link them both ways. The notes end with "For the complete list of changes, see the [changelog](CHANGELOG.md)", and the changelog's version heading is the anchor the notes point back to.

The same release as a release-notes page:

```markdown
# Meridian SDK 4.0 release notes

Released 2026-08-14.

## Highlights

Events are stored through `meridian.events.record()`, which returns the stored
record instead of `undefined`, so you no longer need a second read to get the
server-assigned `id`.

## Upgrade notes

Two breaking changes need action before you upgrade: `meridian.track()` is
removed, and `meridian.query()` orders rows by `timestamp`. Follow
[Migrate from 3.x to 4.0](docs/migrate-3-to-4.md).

## Known issues

`meridian sync --parallel` reports the offset of the last completed batch
rather than the highest one ([#815](...)). Fix planned for 4.0.1.

For the complete list of changes, see the [changelog](CHANGELOG.md).
```

Source: convention

## Migration guides (N6)

A migration guide is a procedure, so the step mechanics belong to **P1 to P4** ([procedures-and-code.md](procedures-and-code.md)): numbered steps, one imperative action each, condition before instruction, expected result stated. The skeleton:

| Section | Contents |
|---|---|
| Title | "Migrate from X to Y" with versions or API names, not "Upgrade guide" |
| Intro | Who needs this, what changes, roughly how long it takes |
| Before you begin | Source and target versions, a backup or clean tree, feature flags to set |
| Numbered steps | One change per step, each with a before and after snippet |
| Verify the migration | A command to run and the output to expect |
| Roll back | How to return to the previous version, and what is not reversible |
| What's next | The reference pages for the new API |

A complete guide for a rename plus a signature change:

````markdown
# Migrate from meridian.track() to meridian.events.record()

Applies to projects on Meridian SDK 3.x that call `meridian.track()`, which is
removed in 4.0.0. The method is renamed and its return value changes from
`undefined` to the stored event. Expect about 15 minutes for a small codebase.

## Before you begin

- Confirm your current version: `npm ls meridian-js` reports 3.4.0 or later.
- Commit or stash your work, because the steps edit call sites in place.
- Set `MERIDIAN_STRICT_EVENTS=1` to make 3.4.0 warn at every remaining
  `track()` call site.

## Migrate the call sites

1. Upgrade the package:

   ```bash
   npm install meridian-js@4.0.0
   ```

2. Replace each `track()` call with `events.record()`. The payload is
   unchanged:

   ```javascript
   // Before
   meridian.track({ name: "checkout_started", userId });

   // After
   await meridian.events.record({ name: "checkout_started", userId });
   ```

3. Optional: if you read the event back to get its `id`, delete the follow-up
   read and use the returned record:

   ```javascript
   // Before
   meridian.track({ name: "checkout_started", userId });
   const stored = await meridian.events.latest({ userId });

   // After
   const stored = await meridian.events.record({
     name: "checkout_started",
     userId,
   });
   ```

## Verify the migration

Run the linter rule that ships with the package:

```bash
npx meridian lint --rule no-removed-apis
```

The output lists remaining call sites, or confirms there are none:

```text
meridian lint: 0 findings in 128 files
```

## Roll back

Reinstall the previous version with `npm install meridian-js@3.4.0` and revert
the call-site commit. Events recorded through 4.0.0 stay readable in 3.4.0.

## What's next

- [events.record() reference](../api/events-record.md)
- [Migrate from 3.x to 4.0](migrate-3-to-4.md) for the remaining breaking changes
````

Two defects to check before publishing. One is a step that says what changed without showing the edit (the snippets are the guide). The other is a guide with no verification step, which leaves the reader unable to tell a finished migration from a half-finished one.

Source: procedures

Adapted from wondelai/skills technical-documentation (MIT) and the Google developer documentation style guide (CC BY 4.0).
