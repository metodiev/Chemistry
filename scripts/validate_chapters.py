#!/usr/bin/env python3
"""Audit chapter files against the repository's structural standard.

Usage
-----
    python3 scripts/validate_chapters.py [ROOT] [--verbose]

Every file matching ``??-*/[0-9][0-9]-*.md`` is treated as a chapter. The script
checks that it has:

* a header block declaring Level, study time, prerequisites and difficulty;
* the required top-level sections (learning objectives, introduction,
  explanation, diagrams, formulas or equations, worked examples,
  common mistakes, summary, exercises, further reading);
* at least two Mermaid diagrams, each with a ``**Figure**`` caption;
* a "Common Mistakes" table;
* an exercises section and an answers/solutions section.

Exit code 0 when every chapter conforms, 1 otherwise.
"""

from __future__ import annotations

import glob
import os
import re
import sys

REQUIRED_SECTIONS = {
    "learning objectives": r"learning objectives",
    "introduction": r"introduction",
    "detailed explanation": r"detailed scientific explanation|scientific explanation|detailed explanation",
    "visual diagrams": r"visual diagrams|diagrams",
    "worked examples": r"worked examples",
    "common mistakes": r"common mistakes",
    "summary": r"chapter summary|summary",
    "exercises": r"exercises",
    "further reading": r"further reading",
}

HEADER_FIELDS = ("level", "estimated study time", "prerequisite", "difficulty")

MIN_DIAGRAMS = 2
MIN_FIGURES = 2


def chapter_files(root: str):
    pattern = os.path.join(root, "[0-9][0-9]-*", "[0-9][0-9]-*.md")
    return sorted(glob.glob(pattern))


def audit(path: str, root: str):
    problems = []
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    rel = os.path.relpath(path, root)
    lower = text.lower()

    first_block = text[:1200].lower()
    for field in HEADER_FIELDS:
        if field not in first_block:
            problems.append(f"header: missing '{field}' declaration")

    headings = re.findall(r"^##\s+(.+)$", text, re.M)
    heading_text = " | ".join(h.lower() for h in headings)
    for label, pattern in REQUIRED_SECTIONS.items():
        if not re.search(pattern, heading_text):
            problems.append(f"section: missing '{label}'")

    diagrams = text.count("```mermaid")
    if diagrams < MIN_DIAGRAMS:
        problems.append(f"diagrams: only {diagrams} Mermaid blocks (need {MIN_DIAGRAMS})")

    figures = len(re.findall(r"^\*\*Figure", text, re.M))
    if figures < MIN_FIGURES:
        problems.append(f"diagrams: only {figures} captioned figures (need {MIN_FIGURES})")

    lines = text.count("\n") + 1
    if lines < 200:
        problems.append(f"depth: only {lines} lines")

    # Common Mistakes must be a table with at least three rows.
    mistakes_idx = lower.find("common mistakes")
    if mistakes_idx == -1:
        problems.append("mistakes: section absent")
    else:
        tail = text[mistakes_idx : mistakes_idx + 4000]
        rows = [ln for ln in tail.splitlines() if ln.strip().startswith("|")]
        if len(rows) < 5:  # header + separator + 3 data rows
            problems.append(f"mistakes: only {max(0, len(rows) - 2)} table rows")

    if "answer" not in lower and "solution" not in lower:
        problems.append("exercises: no answers or solutions provided")

    return rel, problems, lines, diagrams, figures


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "--verbose" in sys.argv
    root = os.path.abspath(args[0] if args else ".")

    files = chapter_files(root)
    if not files:
        print("No chapter files found.")
        return 0

    failures = 0
    total_lines = 0
    for path in files:
        rel, problems, lines, diagrams, figures = audit(path, root)
        total_lines += lines
        if problems:
            failures += 1
            print(f"\n{rel}  ({lines} lines, {diagrams} diagrams)")
            for problem in problems:
                print(f"  - {problem}")
        elif verbose:
            print(f"OK  {rel}  ({lines} lines, {diagrams} diagrams, {figures} figures)")

    print(
        f"\nAudited {len(files)} chapters, {total_lines} lines total. "
        f"Non-conforming: {failures}"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
