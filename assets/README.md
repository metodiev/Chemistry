# Assets

Static files that cannot be expressed as Markdown or Mermaid.

| Folder | Contents | Format |
|---|---|---|
| [diagrams/](diagrams/README.md) | Reusable Mermaid source files quoted by more than one chapter | `.mmd` / `.md` |
| [images/](images/README.md) | Photographs, micrographs, spectra and plots | `.svg`, `.png` |
| [structures/](structures/README.md) | Chemically accurate molecular structures | `.svg` |

## Rules

1. **Prefer Mermaid.** If a relationship can be expressed as a flowchart, state
   machine or mindmap, it belongs in the chapter, not here.
2. **Prefer vector.** SVG scales and stays legible when printed; PNG is acceptable only
   for photographic content.
3. **Name files semantically:** `orbital-2p-node.svg`, not `figure3-final-v2.svg`.
4. **Record provenance.** Every binary asset needs an entry in the folder's `README.md`
   stating its author, licence and source. Assets with unclear licensing will be
   removed.
5. **Do not commit** large instrument data files, raw spectra, or anything over about
   1 MB without discussion in an issue.

## What does *not* belong here

- Screenshots of textbooks or journal figures — these are almost always
  copyright-restricted.
- Decorative images. Every asset in this repository must carry an explanation in the
  chapter that uses it.
- Anything that encodes a safety-relevant procedure for unsupervised use.
