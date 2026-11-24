"""Vale rules of the tech-writer skill, run on fixtures in tests/fixtures."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
VALE_DIR = ROOT / "vale"
FIXTURES = ROOT / "tests" / "fixtures"
TELLS = FIXTURES / "tells.md"
CLEAN = FIXTURES / "clean.md"
CLAUDISMS = FIXTURES / "claudisms.md"
SKILL_DIR = ROOT
CHECKLIST = SKILL_DIR / "references" / "audit-checklist.md"
README = SKILL_DIR / "README.md"
ISO_AUDIT_GLOB = "iso-24495/*/*/skills/iso-24495-text-audit/scripts/audit-text-cli.ts"
# ISO text-audit rule -> Vale checks that port it. Left out: sentence-average reports line 1 for the whole document,
# and acronym-undefined maps to Google.Acronyms, which checks 3 to 5 capitals where the ISO audit checks 2 to 6.
ISO_UNPORTED = {"sentence-average", "acronym-undefined"}
ISO_TO_VALE = {
    "sentence-length": {"TechWriter.SentenceLength"},
    "paragraph-length": {"TechWriter.ParagraphLength"},
    "legalese": {"TechWriter.PlainWords"},
    "complex-word": {"TechWriter.PlainWords"},
    "wordy-phrase": {"TechWriter.WordyPhrases"},
    "doublet": {"TechWriter.WordyPhrases"},
    "double-negative": {"TechWriter.DoubleNegatives"},
    "filler-opening": {"TechWriter.FillerOpenings"},
    "prose-enumeration": {"TechWriter.ProseEnumeration"},
    "link-text": {"TechWriter.LinkText"},
    "image-alt": {"TechWriter.ImageAlt"},
    "table-header": {"TechWriter.TableHeader"},
    "heading-depth": {"TechWriter.HeadingDepth"},
    "heading-skip": {"TechWriter.HeadingSkip"},
    "heading-style": {"TechWriter.HeadingLength", "Google.HeadingPunctuation"},
}

pytestmark = pytest.mark.skipif(
    shutil.which("vale") is None or not (VALE_DIR / "styles" / "ai-tells").is_dir(),
    reason="vale or its packages are missing (run make vale-sync)",
)

CASES = [
    ("ai-tells.EmDashUsage", "The release is ready"),
    ("ai-tells.OverusedVocabulary", "We will delve"),
    ("ai-tells.ClosingPleasantries", "I hope this helps."),
    ("ai-tells.ServesAsDodge", "serves as the single source"),
    ("TechWriter.CurlyQuotes", "“true”"),
    ("TechWriter.ChatbotArtifacts", "[Your Name]"),
    ("TechWriter.SourceDisclaimers", "as of my last training update"),
    ("TechWriter.Significance", "highlights its significance"),
    ("TechWriter.NotabilityClaims", "active social media presence"),
    ("TechWriter.AIVocabulary", "Showcase the options"),
    ("TechWriter.NeedlessCount", "The board must act on"),
    ("TechWriter.NeedlessCount", "Chapter 21 lists"),
    ("TechWriter.AIVocabulary", "quietly broke"),
    ("TechWriter.AIVocabulary", "load-bearing for"),
    ("TechWriter.AIVocabulary", "And honestly"),
    ("TechWriter.ChatbotArtifacts", "you're not crazy"),
    ("TechWriter.ChatbotArtifacts", "You're just early."),
    ("TechWriter.Teasers", "the part that's really interesting"),
    ("TechWriter.Reversal", "The pattern isn't the problem."),
    ("TechWriter.DashSubstitutes", "Docs · Slides"),
    ("TechWriter.DashSubstitutes", "some hosts - like"),
    ("TechWriter.Staccato", "Tests pass. Builds fail."),
    ("Google.Semicolons", "The cache is fast; the disk"),
    ("TechWriter.SentenceLength", "The nightly job reads every export"),
    ("TechWriter.ParagraphLength", "The parser opens the input file now."),
    ("TechWriter.ParagraphLength", "- The loader opens each config file first."),
    ("TechWriter.PlainWords", "We utilize the cache"),
    ("TechWriter.PlainWords", "The service shall restart"),
    ("TechWriter.WordyPhrases", "Check each and every row."),
    ("TechWriter.WordyPhrases", "Restart in order to apply"),
    ("TechWriter.DoubleNegatives", "is not unlike the old one"),
    ("TechWriter.FillerOpenings", "Certainly, the file loads."),
    ("TechWriter.ProseEnumeration", "The first, second, and third runs"),
    ("TechWriter.LinkText", "[click here](https://example.com)"),
    ("TechWriter.ImageAlt", "![](img.png)"),
    ("TechWriter.TableHeader", "|   | Owner |"),
    ("TechWriter.HeadingSkip", "### Skipped level"),
    ("TechWriter.HeadingDepth", "##### Deep heading"),
    ("TechWriter.HeadingLength", "## A heading that keeps going"),
]
CHECKS = {check for check, _ in CASES}


def _mapped_checks() -> set[str]:
    """Vale checks named in the mapping table of audit-checklist.md (rows like `| a, b | H5 | exact |`)."""
    text = CHECKLIST.read_text(encoding="utf-8").split("| Vale check | ID | Kind |", 1)[1].split("\n\n", 1)[0]
    rows = [line.split("|")[1] for line in text.splitlines()[2:]]
    return {check.strip() for row in rows for check in row.split(",")}


def _iso_audit_script() -> Path | None:
    return next(iter(sorted((Path.home() / ".claude" / "plugins" / "cache").glob(ISO_AUDIT_GLOB))), None)


def _alerts(fixture: Path) -> list[dict[str, object]]:
    result = subprocess.run(
        ["vale", "--config", str(VALE_DIR / ".vale.ini"), "--output=JSON", str(fixture)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
        cwd=ROOT,
    )
    assert result.returncode in (0, 1), result.stderr
    return next(iter(json.loads(result.stdout).values()), [])


def _prose_line(sentence: str) -> int:
    """Line of the first occurrence of sentence, which is always outside the code block."""
    for number, line in enumerate(TELLS.read_text(encoding="utf-8").splitlines(), start=1):
        if sentence in line:
            return number
    raise AssertionError(f"{sentence!r} not in {TELLS}")


def _code_block_range() -> range:
    fences = [n for n, line in enumerate(TELLS.read_text(encoding="utf-8").splitlines(), start=1) if line.startswith("```")]
    assert len(fences) == 2
    return range(fences[0], fences[1] + 1)


@pytest.mark.parametrize(("check", "sentence"), CASES)
def test_tell_fires_on_its_line(check: str, sentence: str) -> None:
    lines = {a["Line"] for a in _alerts(TELLS) if a["Check"] == check}
    assert _prose_line(sentence) in lines


def test_no_tell_fires_inside_code_block() -> None:
    block = _code_block_range()
    hits = [a for a in _alerts(TELLS) if a["Check"] in CHECKS and a["Line"] in block]
    assert hits == []


def test_tells_do_not_fire_on_clean_prose() -> None:
    assert [a["Check"] for a in _alerts(CLEAN) if a["Check"] in CHECKS] == []


def test_mapping_table_names_known_checks() -> None:
    checks = _mapped_checks()
    assert {"Google.Semicolons", "TechWriter.Staccato", "ai-tells.ParallelStaccato"} <= checks
    assert {check for check in CHECKS if check.startswith("TechWriter.")} <= checks
    assert {"TechWriter.SentenceAverage", "Google.Acronyms", "Google.HeadingPunctuation"} <= checks
    assert set().union(*ISO_TO_VALE.values()) <= checks
    assert all("." in check and " " not in check for check in checks), checks


def test_every_claudism_line_gets_a_mapped_alert() -> None:
    mapped = _mapped_checks()
    hit = {a["Line"] for a in _alerts(CLAUDISMS) if a["Check"] in mapped}
    prose = [
        (number, line)
        for number, line in enumerate(CLAUDISMS.read_text(encoding="utf-8").splitlines(), start=1)
        if line.strip() and not line.startswith("#")
    ]
    assert [line for number, line in prose if number not in hit] == []


def test_readme_after_section_is_clean() -> None:
    lines = README.read_text(encoding="utf-8").splitlines()
    start = lines.index("## After") + 1
    end = lines.index("## Changes") + 1
    mapped = _mapped_checks()
    hits = [(a["Line"], a["Check"]) for a in _alerts(README) if a["Check"] in mapped and start < int(str(a["Line"])) < end]
    assert hits == []


@pytest.mark.parametrize(("sentences", "fires"), [(10, True), (9, False)])
def test_sentence_average_needs_ten_long_sentences(tmp_path: Path, sentences: int, fires: bool) -> None:
    doc = tmp_path / "average.md"
    doc.write_text(" ".join(["The job " + "reads " * 19 + "rows." for _ in range(sentences)]) + "\n", encoding="utf-8")
    assert any(a["Check"] == "TechWriter.SentenceAverage" for a in _alerts(doc)) is fires


def test_iso_text_audit_parity(tmp_path: Path) -> None:
    """Every line the ISO 24495 text audit flags in tells.md gets an alert from the Vale check that ports its rule."""
    script = _iso_audit_script()
    if shutil.which("bun") is None or script is None:
        pytest.skip("bun or the iso-24495 plugin is missing")
    out = tmp_path / "iso.json"
    result = subprocess.run(
        ["bun", str(script), str(TELLS), "--json", str(out)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
        cwd=ROOT,
    )
    assert result.returncode == 0, result.stderr
    violations = [v for f in json.loads(out.read_text(encoding="utf-8"))["files"].values() for v in f["violations"]]
    assert {v["rule"] for v in violations} - ISO_UNPORTED <= ISO_TO_VALE.keys()
    alerts = {(a["Line"], a["Check"]) for a in _alerts(TELLS)}
    missed = [
        (v["line"], v["rule"])
        for v in violations
        if v["rule"] in ISO_TO_VALE and not any((v["line"], check) in alerts for check in ISO_TO_VALE[v["rule"]])
    ]
    assert len(violations) > 10
    assert missed == []
