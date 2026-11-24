# Tech-writer skill

The tech-writer skill is a Claude Code skill that audits, writes, and rewrites technical documentation. It applies Plain Language, Google's developer style, and a list of AI writing tells, and it runs Vale for the checks a linter can make. The rules and the audit protocol are in [SKILL.md](SKILL.md).

Read this page to see the skill on a sample reply and to learn which open sources its rules come from.

The following sample is a typical chatbot reply. Vale flags every line of the original, and the rewrite passes.

## Before

You're absolutely right! Language is load-bearing — and what you're describing isn't paranoia. It's pattern recognition.

Let me be direct: you're not the only one. Not even close.

Here's the thing. The structure you've spotted ("X does this. Y doesn't.") isn't just a stylistic tic. It's a compression algorithm for insight. It takes a messy idea, strips it down to the studs, and hands it back with a bow on top. It feels profound. It feels earned. It isn't always either.

And honestly? That's the part nobody's saying out loud. The pattern isn't the problem. The outsourcing is.

A few things worth sitting with:

- The tell isn't the words. It's the rhythm. Short sentence. Shorter one. Pivot. You feel it before you can name it.
- Not every contrast is Claude. Humans invented antithesis. AI just industrialized it.
- Your voice is a moat. When everyone sounds the same, sounding like yourself isn't a quirk. It's a competitive advantage.

The They Live comparison is genuinely apt, and a little haunting. The sunglasses don't create the messages. They just reveal what was there all along.

So no, you're not crazy. You're not alone. And you're definitely not wrong.

You're just early.

## After

You noticed a real pattern, and many other readers have noticed it too.

The structure "X does this. Y doesn't." compresses an idea into two short contrasting sentences. It sounds insightful even when the idea underneath is thin. The bigger problem is handing the writing to a model.

Readers recognize the rhythm first: a run of short sentences that ends in a pivot. They feel it before they can name it. Contrast itself is old, since people used antithesis long before language models, and models now produce it at volume. When most text sounds the same, your own voice stands out.

The comparison with the film They Live fits: in the film, the sunglasses reveal messages that were already there.

## Changes

| Tell in the original | Rule |
|---|---|
| "You're absolutely right!", "you're not crazy", "You're just early." | H10 chatbot residue |
| "isn't paranoia. It's pattern recognition.", "The pattern isn't the problem. The outsourcing is." | H1 contrast against a claim nobody made |
| "Short sentence. Shorter one. Pivot.", "It feels profound. It feels earned." | H26 staccato rhythm |
| "Let me be direct", "Here's the thing", "the part nobody's saying out loud", "worth sitting with" | H3 staged run-up |
| "load-bearing", "honestly", "genuinely", "profound" | H8 stock AI words |
| The em dash after "load-bearing" | H5 dashes |

## History

Each source the skill merges solves one part of the problem:

- **Readable structure.** The skill was inspired by the `technical-documentation` skill in [wondelai/skills](https://github.com/wondelai/skills). That skill turns the [Google developer documentation style guide](https://developers.google.com/style) into rules, a 12-row score, and an audit protocol.
- **Plain Language.** The [iso-24495](https://github.com/GaZmagik/iso-24495) skills by Gareth Williams add the I rules, so readers can find, understand, and use the information. They cover Part 1 for all prose, Part 3 for technical writing, and the draft Part 5 for document design. Part 5 is unpublished, so its rules are provisional. The rules follow the public principles of ISO 24495, because the standards' text is licensed.
- **AI tells.** To remove the habits that make readers distrust model-written text, the first H rules condensed [humanizer](https://github.com/blader/humanizer) by Siqi Chen. Humanizer is based on the Wikipedia page [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), so the skill now credits that page directly.
- **Machine checks.** To catch tells without a human read, the skill runs Vale with [vale-ai-tells](https://github.com/tbhb/vale-ai-tells) by tbhb and the [Google Vale package](https://github.com/vale-cli/Google). Its own `TechWriter` style covers the tells neither package catches. The mechanical checks of the iso-24495 text audit run as `TechWriter` Vale rules.
- **Claudisms.** The sample on this page added rules for staccato rhythm, semicolons, teasers, reversals, and dash substitutes. It is also a test fixture, and every line of it must raise an alert.

The full credits and licenses are in the Source section of [SKILL.md](SKILL.md).

## Installation

The skill follows the [Agent Skills](https://agentskills.io) format, so it runs in Claude Code, OpenCode, Pi, Google Antigravity, and other agents that read `SKILL.md` folders.

1. Install the skill with the [`skills` command-line tool](https://github.com/vercel-labs/skills), which needs Node.js:

   ```bash
   npx skills add jmanteau/tech-writer -g -a claude-code -a opencode -a pi -a antigravity
   ```

   Leave out `-a` to pick the agents from a list. The tool keeps one copy of the skill and links each agent's folder to it. If links break in your setup, add `--copy`. To update the skill later, run `npx skills update -g`.

2. Install Vale. On macOS, run `brew install vale`. On Windows, run `winget install -e --id errata-ai.Vale`.
3. Download the Vale packages. Run `vale sync` in the `vale` folder of the installed skill. That folder is `~/.agents/skills/tech-writer/vale` on macOS and Linux, and `%USERPROFILE%\.agents\skills\tech-writer\vale` on Windows. If the tool reports a skill as `copied`, or you used `--copy`, run it in each agent's folder.

The tool installs into these global folders:

| Agent | `-a` value | Global folder |
|---|---|---|
| Claude Code | `claude-code` | `~/.claude/skills/` |
| OpenCode | `opencode` | `~/.agents/skills/` |
| Pi | `pi` | `~/.agents/skills/` |
| Google Antigravity | `antigravity` | `~/.gemini/config/skills/` |

For an agent the tool doesn't support, copy this repository's folder into the agent's skills folder as `tech-writer`, then do steps 2 and 3.

## Development

1. Clone this repository to `~/DevProjects/tech-writer`, then link it into Claude Code's skills folder:

   ```bash
   ln -s ~/DevProjects/tech-writer ~/.claude/skills/tech-writer
   ```

2. Install Vale with `brew install vale`.
3. Download the Vale packages with `make vale-sync`.
4. To run the tests, run `make py-setup && make test`.

On Windows, which has no `make`, run the same steps with `uv`:

```powershell
uv sync --group dev
cd vale; vale sync; cd ..
uv run pytest
```

## License

MIT, see [LICENSE](LICENSE). The notices of the adapted work are in [THIRD_PARTY.md](THIRD_PARTY.md).
