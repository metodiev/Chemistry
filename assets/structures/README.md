# Structures

Chemically accurate molecular structures in SVG.

Mermaid cannot represent bond angles, stereochemistry, chair conformations or orbital
surfaces faithfully, and a misleading diagram is worse than no diagram. Where a
structure must be *seen*, it belongs here.

## Naming convention

```
<name>-<view>.svg
```

Examples: `cyclohexane-chair.svg`, `benzene-mo-homo.svg`,
`[fe(cn)6]3--crystal-field.svg`, `dna-base-pair.svg`.

## Drawing standards

| Feature | Convention |
|---|---|
| Bond length | Uniform within a structure |
| Line width | Uniform; bold wedges for bonds out of plane, hashed wedges for bonds into plane |
| Stereochemistry | Explicit wedges/dashes; never implied |
| Charges | Circled, positioned unambiguously |
| Lone pairs | Drawn where mechanistically relevant |
| Colour | Atoms may be colour-coded (O red, N blue, S yellow, P orange); colour must never be the only carrier of meaning |
| Text | Embedded as text elements, not outlines, so the file remains searchable and translatable |

## Index

| File | Structure | Chapter that uses it |
|---|---|---|
| *(none yet)* | | |

## Creating a structure

1. Draw in any chemistry-capable editor that exports SVG.
2. Strip editor metadata, embedded fonts and raster previews.
3. Run the SVG through a validator (for example W3C Nu HTML Checker) and confirm it
   renders without external references.
4. Add the row to the index above with the chapter link.

## Validation

An SVG is acceptable when: it renders standalone in a browser, contains no `<image>`
raster fallback, has a `viewBox`, and carries a `<title>` element for accessibility.
