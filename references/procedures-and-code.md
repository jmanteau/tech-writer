# Procedures and code

This file owns **P1 to P11, I10, I11, and I18**: step-by-step instructions, forking procedures, UI verbs, code in prose, code samples, placeholders, command-line syntax, code citations, and symbol consistency. W1 (condition before instruction) belongs to [voice-and-words.md](voice-and-words.md). S12 (the bold, code-font, and italics summary) belongs to [structure-and-formatting.md](structure-and-formatting.md). A1 to A7 (API reference text, docstrings) belong to [api-reference.md](api-reference.md). They are mentioned here only where a procedure or sample touches them.

## Procedure anatomy (P1 to P4)

A procedure exists to get one reader from a starting state to a finished one. Every step names a single imperative action, states or implies where to act, and lets the reader confirm what happened before moving on.

**Rules:**
- **P1, numbered steps, one action each.** Split "click X and then configure Y" into two steps. If a step has two actions, the reader can't tell which one failed.
- **Condition before instruction (W1, owned by voice-and-words.md).** Write "If you want X, do Y", not "Do Y if you want X." The reader decides if the step applies before reading how to do it.
- **P4, where to act and what to expect.** Name the screen, menu, or file the action happens in. State the observable result: a new status, a redirect, a file on disk.
- **P3, "Optional:" prefix.** Not "(Optional)", not "You can also...". Start the step with the word "Optional:" so a scanning reader can skip it without reading the rest.
- **P2, single step is a bullet.** A procedure with exactly one action is a bullet (`*` or `-`), never "1." A numbered list of one implies that steps 2 and 3 are coming.
- **P2, sub-steps a/b/c, then i/ii/iii.** Use letters for a sub-sequence inside a numbered step. Drop to roman numerals only when a lettered sub-step itself has to branch, for example by operating system. Don't add a third level to document a style preference.
- **Document the shortest path.** When the UI and the CLI both accomplish the task, pick one and mention the other in a single sentence, not as a parallel procedure.

**Before:**

```markdown
To turn on automatic deployments, you should first go to the project
settings and look for the Deployments tab, then enable it, and after
that you can pick which branch you want it to watch. You should also
set a build command if you have one, and once you're done you can
save it, and it will deploy automatically from then on when you push
to that branch.
```

**After:**

```markdown
1. In the **shipit** console, open your project and click **Settings**.
2. Click **Deployments**.
3. Turn on **Automatic deployments**.
4. Select the branch to watch:
   a. Click the **Branch** menu.
   b. Choose the branch, for example `main`.
5. Optional: Enter a build command, for example `npm run build`.
6. Click **Save**. The **Status** column shows **Watching** next to
   the selected branch.
```

A step that must branch by platform drops to roman numerals inside the lettered sub-step:

```markdown
1. Open a terminal.
   a. On macOS or Linux, run `chmod +x shipit`.
      i. If `shipit` isn't on your `PATH`, move it to `/usr/local/bin`.
      ii. If it is, skip to step 2.
   b. On Windows, skip this step.
```

A single-action procedure stays a bullet:

```markdown
To restart the deployment watcher:

* Click **Restart** in the **Deployments** panel.
```

Source: procedures

## Forking procedures (I18)

When the reader's situation decides the next steps, the procedure forks. Use a decision table or a set of labelled conditions, not one numbered list that sends the reader jumping between steps. Each route starts with its condition (W1), and the reader follows only their own route. A short branch inside one step, such as a platform switch, stays a lettered sub-step (P2).

**Before:**

```markdown
1. Open the console.
2. If you use SSO, click **SSO** and go to step 5.
3. Enter your password.
4. Go to step 6.
5. Approve the SSO prompt.
6. Click **Deploy**.
```

**After:**

```markdown
Sign in to the console:

| If you sign in with | Do this |
|---|---|
| SSO | Click **SSO**, then approve the prompt. |
| A password | Enter your password, then click **Sign in**. |

Then click **Deploy**.
```

Source: ISO 24495-5 skill, rule 4 (I18, proxy, working draft)

## UI elements and device verbs (P5)

**Rules:**
- **Bold the element's name**, not its type: "Click **Save**", not "Click the **Save** button." Name the type only when the label alone is ambiguous. Example: "click the **Region** dropdown" when a section is also called Region.
- **Casing matches the UI**, with one exception: an ALL-CAPS label in the interface is written in sentence case in prose. A button rendered `SUBMIT ORDER` is still "click **Submit order**."
- **Menu paths** bold each segment and join with `>`: "**File > Save as**" (inferred). The guide doesn't give this exact notation, but it follows directly from bolding UI element names in sequence.
- **Device verbs** match how the reader is expected to interact with the target, not the writer's own device.

| Verb | Situation | Example |
|------|-----------|---------|
| Click | Mouse or trackpad: buttons, links, checkboxes | "Click **Deploy**." |
| Tap | Touchscreen: the same targets on mobile or tablet | "Tap **Deploy**." |
| Select | Device-agnostic: menu items, dropdown options, radio buttons | "Select **Production** from the **Environment** menu." |
| Enter | Typing a value into a field | "Enter your project ID." |
| Type | Free-text input where "enter" would also read correctly; the two are interchangeable (inferred) | "Type a description for the release." |
| Choose | Picking one option among several presented together; close in meaning to "select" (inferred) | "Choose a region for the new environment." |

**Before and after:**
- "Click on the SAVE CHANGES button to save your changes." becomes "Click **Save changes**."
- "Go to File, then Export, then click on PDF." becomes "Click **File > Export > PDF**."

Source: ui-elements

## Code in text (P6)

**Gets code font:** filenames, paths, commands, flags, parameters, values, method and function names, class names, HTTP status codes, environment variables.

**Doesn't:** product names, UI labels (those are bold, per P5), and general concepts ("the deploy step," not `the deploy step`).

Code isn't a part of speech. Don't inflect it as a verb, and don't pluralize it by adding a suffix outside the backticks. Add a plain-English noun instead: "call the `close` method," not "`close`ing the file"; "`Widget` objects," not "`Widget`s."

**Before and after:**
- "Open the config.yaml file and set the timeout value to 30 seconds." becomes "Open `config.yaml` and set `timeout` to `30`."
- "Run shipit deploy with the dash-dash-force flag to skip confirmation." becomes "Run `shipit deploy --force` to skip confirmation."
- "The API returns a 404 Not Found if SHIPIT_API_KEY isn't set." becomes "The API returns `404 Not Found` if `SHIPIT_API_KEY` isn't set."
- "After closing() the file, check for leftover Widgets. The Shipit CLI logs them." becomes "After you call the `close` method, check for leftover `Widget` objects. The shipit CLI logs them."
  - The method and class stay in code font. The product name doesn't.

Source: code-in-text

## Code samples (P7, P10)

**Rules:**
- **P7, introduce every sample with a sentence ending in a colon.** A bare code block gives the reader no reason to read it. It also hides what the code is for.
- **One concept per sample.** A sample that shows authentication and retry logic in one block forces a reader debugging retries to also parse auth.
- **Runnable and minimal.** Nothing in the sample should be unrelated to the concept it demonstrates, and nothing needed to run it should be missing.
- **Realistic names.** Use production-shaped data, not `foo` and `bar`. A reader pattern-matches against their own variables and data.
- **Wrap at 80 characters.** Long lines force horizontal scrolling in both the doc and the terminal the reader pastes into.
- **Show expected output** in a second fenced block, immediately after the sample.
- **Comments explain why**, not what the syntax already says.
- **Tag the language** on every fence (` ```python `, ` ```bash `). Untagged blocks can't be highlighted or reliably copied (convention).

**Before and after (function):**

```python
# before: no intro, mixed concepts, foo/bar, no output shown
def foo(bar):
    x = bar['data']
    result = []
    for i in x:
        if i['active'] == True and i['score'] > 50 and i['region'] in ['us', 'eu', 'apac']:
            result.append(i['name'])
    return result
```

The following function returns the names of active users in a supported region who scored above 50:

```python
SUPPORTED_REGIONS = ("us", "eu", "apac")


def high_scorers(users):
    # Scoring only applies in supported regions, so filter first.
    return [
        user["name"]
        for user in users
        if user["active"]
        and user["score"] > 50
        and user["region"] in SUPPORTED_REGIONS
    ]
```

```
>>> high_scorers(users)
['Priya Patel', 'Sam Nguyen']
```

**Before and after (CLI):**

```markdown
To see your deployments just run this: shipit list-deployments --all
--verbose --since=2026-01-01 --until=2026-08-29 --format=json --pretty
| jq '.[] | select(.status=="failed")'
```

The following command lists deployments that failed since the start of the year:

```bash
shipit list-deployments \
  --since=2026-01-01 \
  --status=failed
```

```
DEPLOYMENT   BRANCH   STATUS   FINISHED
d-8f2a1c     main     failed   2026-03-14T10:02:00Z
```

Source: code-samples, tech-writing/two "Sample code"

## Placeholders (P8)

A placeholder stands in for a value the reader supplies. Write it `ALL_CAPS_WITH_UNDERSCORES`. Never write `<your-api-key>`, because angle brackets read as literal characters to a reader who doesn't know the convention. Never write `MY_PROJECT_ID` or `YOUR_API_KEY`, because the prefix reads as part of the name. After the sample, list what each placeholder means in a "Replace the following:" block.

**Before:**

```bash
shipit deploy --key=<your-api-key> --project=YOUR_PROJECT_ID
```

**After:**

Deploy your project by running the following command:

```bash
shipit deploy --key=API_KEY --project=PROJECT_ID
```

Replace the following:

- `API_KEY`: the key from the project's **Settings > API keys** page.
- `PROJECT_ID`: the project ID shown at the top of the **Overview** page.

Source: placeholders

## Command-line syntax (P9)

| Notation | Meaning | Example |
|----------|---------|---------|
| `[optional]` | The argument may be omitted | `shipit deploy [--dry-run]` |
| `{a\|b}` | Choose exactly one | `shipit logs {--tail\|--since=DATE}` |
| `...` | The argument repeats | `shipit tag ITEM...` |
| `ALL_CAPS` | A placeholder, not a literal | `shipit init PROJECT_NAME` |

**One command per line** (convention). Don't chain unrelated commands with `&&` in a sample unless the sample's stated purpose is to show chaining.

**Long commands wrap with `\` continuation**, one flag per line, as in the CLI sample in the Code samples section.

**Prompt characters.** The guide doesn't say whether to show a leading `$` (convention). This skill's default is to omit it. The fenced ` ```bash ` tag already marks the block as a shell command, and readers who don't know to drop a bare `$` paste it verbatim. Follow a project's existing samples if they already include `$`: local convention wins (see SKILL.md, the precedence rule).

**Filenames** written inside docs, such as sample config files and script names, are lowercase, hyphenated, and ASCII:

- "See Getting_Started.MD for setup instructions." becomes "See `getting-started.md` for setup instructions."

Source: code-syntax, filenames

## Sample-code quality checklist (P10)

| Check | Why | Example fix |
|-------|-----|--------------|
| Language tag on every fence | Without it, editors and readers can't syntax-highlight or copy cleanly | ` ``` ` becomes ` ```python ` |
| Lines wrap at 80 characters | Long lines force horizontal scrolling in docs and terminals | Break a long flag list after the first flag with `\` |
| One concept per sample | A reader debugging one idea shouldn't have to parse three | Split an auth-and-retry sample into two samples |
| Realistic names, no foo/bar | `foo`/`bar` carries no information about real data | `def foo(bar)` becomes `def high_scorers(users)` |
| Comments explain why, not what | "# add 1" repeats the syntax; "why" earns the reader's attention | `# add 1` becomes `# Retry once before failing the request` |
| Placeholders in `ALL_CAPS`, explained after | `<your-key>` reads as a literal or gets pasted verbatim | `--key=<your-key>` becomes `--key=API_KEY` plus a "Replace the following" entry |
| Expected output shown in a second block | Without it, the reader can't tell if the sample worked | Add a fenced block with the actual return value or CLI output |
| Sample is runnable as shown | An undefined variable or missing import fails silently for the reader | Add the missing `import` or define the variable inline |
| Introduced by a sentence ending in a colon | A bare code block gives no reason to read it | "Here's code:" becomes "The following command lists failed deployments:" |
| Verified against code or `--help`, not invented | An unverified flag teaches a command that fails | Confirm `--status` exists via `shipit deploy --help` (see P11) |

Source: code-samples, tech-writing/two "Sample code"

## Fact verification before style (P11)

P11 is the one blocking rule in this file, and it comes before every other rule here. A beautifully formatted step for a flag that doesn't exist teaches the reader something false with total confidence. Style makes a doc readable. It does nothing to make a doc true.

Trace every command, flag, parameter, default, and described behavior to one of four sources before it goes in a doc:

1. **The parser or argument definitions.** Grep the CLI's flag-parsing code (`argparse`, `cobra`, `clap`, `yargs`, or the project's own dispatcher) for the exact flag name, type, and default value.
2. **`--help` output.** Run the actual command and read its usage text. Don't reconstruct it from memory of a similar tool or an older version.
3. **Tests.** A flag's real behavior, including edge cases, often matches its test fixtures more precisely than its comments or its `--help` string.
4. **The user.** When no code is reachable, ask. Don't infer a plausible-sounding default.

When none of the four resolves a fact, write `TODO(verify): confirm whether --status accepts a comma-separated list` inline and move on. Never fill the gap with a guess that reads as confident prose. A `TODO(verify)` marker is visible and fixable. A wrong sentence that reads well is neither.

The skill's rule (SKILL.md, the verification section): "Never include a command, flag, or parameter you didn't see in code or receive from the user." A wrong polished doc is worse than an ugly right one. Polish signals authority. A reader trusts a wrong flag name precisely because the sentence around it reads well. An ugly doc with a `TODO(verify)` marker at least tells the reader where the doc stops vouching for itself.

Source: skill rule

## Code citations (I10)

When you explain code (not when you guide a user's task), cite the exact file and line range as a link in the ISO 24495-3 format, for example `[state_manager.rs:45-52](file:///src/state_manager.rs#L45-L52)`. A reader can then open the code and check the claim. A chat reply may use plain `path:line`, such as `src/state_manager.rs:45-52`. Cite the range that holds the behavior, not the whole file. Re-read the lines before you cite them, because line numbers drift.

- Before: "The state manager saves the checkpoint before it exits."
- After: "The state manager saves the checkpoint before it exits ([state_manager.rs:45-52](file:///src/state_manager.rs#L45-L52))."

Do not use line citations in task guidance for end users, who do not have the source open.

Source: ISO 24495-3 skill, rule 2 (I10, proxy)

## Symbol consistency (I11)

Use the same symbol names across the text, the code samples, and the diagrams. If the code calls it `retry_table`, the prose and the diagram say `retry_table`, not "backoff schedule" or "RetryTable". This extends one term per concept (I4, voice-and-words.md) to code identifiers.

- Before: Prose says "the delay list"; the sample defines `RETRY_DELAYS`; the diagram box says "Backoff".
- After: Prose, sample, and diagram all say `retry_delays`.

Source: ISO 24495-3 skill, rule 3 (I11, proxy)

Adapted from wondelai/skills technical-documentation (MIT) and the Google developer documentation style guide (CC BY 4.0); I rules from iso-24495 skills (MIT, proxies, no ISO conformance claim).
