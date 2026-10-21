# SPDX-License-Identifier: MIT
# Copyright (c) 2026 陳柏威 (https://drpwchen.com) — see LICENSE-MIT
"""Static checks for the skill repo. Run: python scripts/check_skill.py  (exit 0 = all green)

Checks:
  1. SKILL.md frontmatter follows the Agent Skills spec (name format, name == folder, description length).
  2. Every relative Markdown link in the repo points to an existing file.
  3. Skill files carry no personal location / price data (they must stay evergreen and private-data free).
  4. Each test scenario contains the required output sections.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "ha-first-home-planner"

# Places tied to the author's household; must never appear in published skill / research text.
PII_TERMS = ["花蓮", "台南", "臺南", "Hualien", "Tainan", "慈濟"]
# Skill files must not hard-code prices (they go stale); research/ may quote dated prices with sources.
PRICE_RE = re.compile(r"(NT\$|US\$|\$\s?\d|\d+\s?美元|\d[\d,]*\s?元(?!件))")
SCENARIO_SECTIONS = ["## 你的需求", "## 第一期購物清單", "| 必買", "| 可等", "| 別買",
                     "## 買之前要查的事", "## 第一週要做的事", "## 評語"]

errors = []


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def check_skill_md():
    p = SKILL_DIR / "SKILL.md"
    fm = frontmatter(p.read_text(encoding="utf-8"))
    if fm is None:
        errors.append("SKILL.md: missing frontmatter")
        return
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    if not name:
        errors.append("SKILL.md: missing name")
    else:
        n = name.group(1)
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n) or len(n) > 64:
            errors.append(f"SKILL.md: invalid name {n!r}")
        if n != SKILL_DIR.name:
            errors.append(f"SKILL.md: name {n!r} != folder {SKILL_DIR.name!r}")
    desc = re.search(r"^description:\s*>?\s*\n((?:[ \t]+.*\n?|\s*\n)+)", fm, re.M)
    if not desc:
        errors.append("SKILL.md: missing block description")
    else:
        text = " ".join(line.strip() for line in desc.group(1).splitlines() if line.strip())
        if not (1 <= len(text) <= 1024):
            errors.append(f"SKILL.md: description length {len(text)} not in 1..1024")
    lines = p.read_text(encoding="utf-8").count("\n")
    if lines > 500:
        errors.append(f"SKILL.md: {lines} lines > 500 (spec recommendation)")


def check_links():
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", md.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target):
                continue
            if not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link {target}")


def check_private_and_prices():
    scan = list(SKILL_DIR.rglob("*.md")) + list((ROOT / "research").rglob("*.md")) + \
        list((ROOT / "tests").rglob("*.md")) + [ROOT / "README.md"]
    for f in scan:
        text = f.read_text(encoding="utf-8")
        for term in PII_TERMS:
            if term in text:
                errors.append(f"{f.relative_to(ROOT)}: private location term {term!r}")
        if SKILL_DIR in f.parents:
            for m in PRICE_RE.finditer(text):
                errors.append(f"{f.relative_to(ROOT)}: hard-coded price {m.group(0)!r}")


def check_scenarios():
    files = sorted((ROOT / "tests" / "scenarios").glob("[0-9]*.md"))
    if len(files) < 3:
        errors.append(f"tests/scenarios: expected >= 3 scenarios, found {len(files)}")
    for f in files:
        text = f.read_text(encoding="utf-8")
        for s in SCENARIO_SECTIONS:
            if s not in text:
                errors.append(f"{f.relative_to(ROOT)}: missing section {s!r}")


for check in (check_skill_md, check_links, check_private_and_prices, check_scenarios):
    check()

if errors:
    print("FAIL")
    print("\n".join(f"  - {e}" for e in errors))
    sys.exit(1)
print("OK: skill frontmatter, links, private-data/price scan, scenarios")
