# Chapter Review Checklist

Use this checklist before opening a pull request that adds or edits a chapter.
Copy it into the pull-request description and tick each item.

## Structure

- [ ] File name follows `NN-kebab-case-title.md` inside the correct level folder.
- [ ] Chapter header block contains level, study time, prerequisites and difficulty.
- [ ] Sections follow the order in [`chapter-template.md`](./chapter-template.md).
- [ ] The chapter is listed in the level `README.md` and in `CURRICULUM.md`.
- [ ] A solutions file exists in `solutions/` for every exercise set.

## Science

- [ ] Every chemical equation is balanced, with states where relevant.
- [ ] IUPAC nomenclature and terminology are used correctly.
- [ ] SI units are used; conversions are shown explicitly.
- [ ] Simplifications (Bohr model, VSEPR, ideal gas, steady state) are labelled
      as simplifications and their limits stated.
- [ ] Numerical values (constants, enthalpies, pKa, bond lengths) are traceable
      to a source listed in `REFERENCES.md`.
- [ ] No fabricated citations, DOIs, page numbers or experimental results.

## Diagrams

- [ ] Every Mermaid block is fenced with ` ```mermaid `.
- [ ] Each diagram has a caption **and** an explanatory paragraph.
- [ ] Diagram syntax validated with `python3 scripts/validate_mermaid.py`.
- [ ] Diagrams carry meaning; decorative diagrams removed.

## Mathematics

- [ ] Display math uses `$$ … $$`; inline math uses `$ … $`.
- [ ] Symbols are defined before use, with units.
- [ ] Worked examples show the algebraic rearrangement, not just the result.
- [ ] Answers are rounded to the significant figures justified by the data.

## Pedantry about pedagogy

- [ ] Learning objectives are measurable (use action verbs).
- [ ] Difficulty is consistent with the advertised level.
- [ ] Prerequisites exist earlier in the curriculum.
- [ ] At least one real-world application is included.
- [ ] Common misconceptions are addressed explicitly.

## Mechanics

- [ ] Relative internal links resolve (run `python3 scripts/validate_links.py`).
- [ ] Markdown table pipes are escaped where needed.
- [ ] No trailing whitespace or tabs.
