#!/usr/bin/env python3
"""Validate relative Markdown links across the repository.

Usage
-----
    python3 scripts/validate_links.py [ROOT]

Checks every Markdown file under ROOT (default: repository root) for links of
the form ``[text](target)`` and verifies that relative targets exist on disk.
External URLs, ``mailto:`` links and pure anchors are skipped.

Exit code is 0 when no problems are found, 1 otherwise.
"""

from __future__ import annotations

import os
import re
import sys
from typing import Iterator, List, Tuple

SKIP_DIRS = {".git", "node_modules", ".github", "assets"}

LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE_FENCE_RE = re.compile(r"^(```|~~~)")


def iter_markdown_files(root: str) -> Iterator[str]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                yield os.path.join(dirpath, name)


def strip_code_blocks(text: str) -> str:
    """Replace fenced code blocks and inline code with blanks (line-preserving)."""
    out: List[str] = []
    in_fence = False
    for line in text.splitlines():
        if CODE_FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    joined = "\n".join(out)
    return re.sub(r"`[^`\n]*`", "", joined)


def is_external(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith(("http://", "https://", "mailto:", "ftp://", "tel:"))
        or lowered.startswith("#")
        or lowered.startswith("data:")
    )


def check_file(path: str, root: str) -> List[Tuple[int, str, str]]:
    problems: List[Tuple[int, str, str]] = []
    with open(path, "r", encoding="utf-8") as handle:
        raw = handle.read()
    text = strip_code_blocks(raw)

    for line_no, line in enumerate(text.splitlines(), start=1):
        for regex in (LINK_RE, IMAGE_RE):
            for match in regex.finditer(line):
                target = match.group(1)
                if is_external(target):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                if target.startswith("/"):
                    # Repository-absolute link: resolve against the repo root.
                    resolved = os.path.join(root, target.lstrip("/"))
                else:
                    resolved = os.path.normpath(
                        os.path.join(os.path.dirname(path), target)
                    )
                resolved = resolved.split("#", 1)[0]
                if not os.path.exists(resolved):
                    rel = os.path.relpath(path, root)
                    problems.append((line_no, rel, target))
    return problems


def main() -> int:
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    total_files = 0
    total_links = 0
    all_problems: List[Tuple[int, str, str]] = []

    for md_path in iter_markdown_files(root):
        total_files += 1
        all_problems.extend(check_file(md_path, root))

    for line_no, rel, target in all_problems:
        print(f"{rel}:{line_no}: broken link -> {target}")

    print(
        f"\nChecked {total_files} Markdown files. "
        f"Broken links: {len(all_problems)}"
    )
    return 1 if all_problems else 0


if __name__ == "__main__":
    sys.exit(main())
