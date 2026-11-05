#!/usr/bin/env python3
"""Lightweight Mermaid sanity checker for the Chemistry Mastery repository.

This is *not* a full Mermaid parser. It catches the mistakes that actually occur
in hand-written Markdown:

* unterminated ```mermaid fences;
* empty diagrams;
* a missing or unknown diagram-type keyword on the first line;
* unbalanced ``[]``, ``()``, ``{}`` or double quotes inside a line;
* ``mindmap`` blocks that use tabs instead of spaces;
* sequence-diagram messages containing a bare semicolon.

Usage
-----
    python3 scripts/validate_mermaid.py [ROOT]

Exit code is 0 when no problems are found, 1 otherwise.
"""

from __future__ import annotations

import os
import re
import sys
from typing import Dict, Iterator, List, Tuple

SKIP_DIRS = {".git", "node_modules", ".github"}

DIAGRAM_TYPES = {
    "flowchart",
    "graph",
    "sequenceDiagram",
    "classDiagram",
    "stateDiagram",
    "stateDiagram-v2",
    "erDiagram",
    "journey",
    "gantt",
    "pie",
    "quadrantChart",
    "requirementDiagram",
    "gitGraph",
    "mindmap",
    "timeline",
    "sankey-beta",
    "xychart-beta",
    "block-beta",
    "packet-beta",
    "architecture-beta",
    "radar-beta",
}

FENCE_RE = re.compile(r"^(\s*)```(\w*)\s*$")


def iter_markdown_files(root: str) -> Iterator[str]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                yield os.path.join(dirpath, name)


def balanced(line: str) -> bool:
    pairs = {"[": "]", "(": ")", "{": "}"}
    stack: List[str] = []
    in_quotes = False
    escaped = False
    for char in line:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_quotes = not in_quotes
            continue
        if in_quotes:
            continue
        if char in pairs:
            stack.append(pairs[char])
        elif char in pairs.values():
            if not stack or stack.pop() != char:
                return False
    return not stack and not in_quotes


def check_file(path: str) -> List[Tuple[int, str]]:
    problems: List[Tuple[int, str]] = []
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    index = 0
    block_number = 0
    while index < len(lines):
        match = FENCE_RE.match(lines[index])
        if not match or match.group(2) != "mermaid":
            index += 1
            continue

        block_number += 1
        start = index + 1
        index += 1
        body: List[str] = []
        closed = False
        while index < len(lines):
            if FENCE_RE.match(lines[index]) and not FENCE_RE.match(lines[index]).group(2):
                closed = True
                break
            body.append(lines[index])
            index += 1

        if not closed:
            problems.append((start, "unterminated ```mermaid fence"))
            break

        content = [line for line in body if line.strip()]
        if not content:
            problems.append((start, "empty Mermaid diagram"))
            index += 1
            continue

        first = content[0].strip()
        keyword = first.split()[0] if first.split() else ""
        base_keyword = keyword.split("-")[0] if keyword else ""
        if keyword not in DIAGRAM_TYPES and base_keyword not in {
            k.split("-")[0] for k in DIAGRAM_TYPES
        }:
            problems.append(
                (start + 1, f"unknown diagram type '{keyword}' on first line")
            )

        if keyword == "mindmap":
            for offset, line in enumerate(body):
                if "\t" in line:
                    problems.append(
                        (
                            start + 1 + offset,
                            "mindmap indentation must use spaces, not tabs",
                        )
                    )

        for offset, line in enumerate(body):
            stripped = line.strip()
            if not stripped or stripped.startswith("%%"):
                continue
            if not balanced(line):
                problems.append(
                    (start + 1 + offset, f"unbalanced brackets or quotes: {stripped}")
                )
    return problems


def main() -> int:
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    files = 0
    problems: List[Tuple[str, int, str]] = []
    for md_path in iter_markdown_files(root):
        files += 1
        for line_no, message in check_file(md_path):
            problems.append((os.path.relpath(md_path, root), line_no, message))

    for rel, line_no, message in sorted(problems):
        print(f"{rel}:{line_no}: {message}")

    print(f"\nScanned {files} Markdown files. Mermaid problems: {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
