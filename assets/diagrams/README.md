# Diagrams

Reusable **Mermaid source** that appears in more than one chapter.

Most diagrams live inline in the chapter that introduces them, because a diagram is
part of the argument. A diagram belongs here only when two or more chapters need the
identical figure — for example the periodic-table block map, or the standard
thermodynamic square.

## Index

*No shared diagrams have been extracted yet. Every Mermaid diagram currently lives
inline in its chapter.*

## Convention for extracted diagrams

A shared diagram is stored as a Markdown file containing nothing but the fenced
Mermaid block and a one-line title, for example `periodic-blocks.md`:

````markdown
# Periodic table blocks

```mermaid
flowchart LR
    S["s-block"] --> P["p-block"] --> D["d-block"] --> F["f-block"]
```
````

Chapters then link to the file rather than duplicating the source, so that a
correction propagates everywhere at once.

## Validation

All Mermaid blocks — inline and extracted — are checked by
`python3 scripts/validate_mermaid.py`, which verifies the fence, the diagram type on
the first line, bracket balance and indentation.
