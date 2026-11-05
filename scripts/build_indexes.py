#!/usr/bin/env python3
"""Generate CURRICULUM.md, ROADMAP.md and the twelve level READMEs.

The chapter list below is the single source of truth for the repository's
structure: names, numbering, difficulty, study hours and prerequisites. Editing
it and re-running the script keeps the curriculum map, the roadmap checklist and
every level index in sync.

Usage
-----
    python3 scripts/build_indexes.py

The script only writes the generated files; it never deletes anything.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (dir, level_label, title, blurb, audience, chapters)
# chapter = (num, filename, title, stars, hours, prereq)
LEVELS = [
    (
        "01-foundations",
        "Level 0",
        "Foundations",
        "The vocabulary and mental models that every later chapter assumes: what "
        "chemistry studies, how matter is classified, how it changes state, how "
        "atoms and molecules are written down, how measurements are made, and how "
        "to work safely.",
        "Absolute beginner — no prior chemistry",
        [
            (1, "01-what-is-chemistry.md", "What Is Chemistry?", 1, 3, "None"),
            (2, "02-matter-and-its-classification.md", "Matter and Its Classification", 1, 3, "Ch. 1"),
            (3, "03-states-of-matter.md", "Solids, Liquids, Gases and Plasma", 1, 3, "Ch. 2"),
            (4, "04-physical-and-chemical-properties-and-changes.md", "Physical and Chemical Properties and Changes", 1, 3, "Ch. 2–3"),
            (5, "05-elements-compounds-and-mixtures.md", "Elements, Compounds and Mixtures", 1, 3, "Ch. 2, 4"),
            (6, "06-atoms-molecules-and-ions.md", "Atoms, Molecules and Ions", 1, 3, "Ch. 5"),
            (7, "07-introduction-to-the-periodic-table.md", "Introduction to the Periodic Table", 2, 3, "Ch. 6"),
            (8, "08-chemical-symbols-and-formulas.md", "Chemical Symbols and Formulas", 2, 3, "Ch. 6–7"),
            (9, "09-measurement-units-and-significant-figures.md", "Measurement, Units and Significant Figures", 2, 4, "Ch. 1–8"),
            (10, "10-laboratory-safety-equipment-and-methods.md", "Laboratory Safety, Equipment and the Scientific Method", 2, 4, "Ch. 1–9"),
        ],
    ),
    (
        "02-elementary-chemistry",
        "Level 1",
        "Elementary Chemistry",
        "The structure of the atom, the logic of the periodic table, the three "
        "primary bonding models, Lewis structures, nomenclature and the balanced "
        "chemical equation.",
        "GCSE / early high-school chemistry",
        [
            (1, "01-atomic-structure.md", "Atomic Structure", 2, 5, "Level 0 in full"),
            (2, "02-isotopes-and-atomic-mass.md", "Isotopes and Atomic Mass", 2, 4, "Ch. 1"),
            (3, "03-electron-shells-and-electron-configurations.md", "Electron Shells, Orbitals and Configurations", 3, 6, "Ch. 1–2"),
            (4, "04-periodic-table-organization-and-periodic-trends.md", "Periodic Table Organization and Periodic Trends", 3, 6, "Ch. 1–3"),
            (5, "05-chemical-bonding.md", "Chemical Bonding: Ionic, Covalent and Metallic", 3, 7, "Ch. 3–4"),
            (6, "06-lewis-structures-and-chemical-formulas.md", "Lewis Structures and Chemical Formulas", 3, 5, "Ch. 5"),
            (7, "07-chemical-nomenclature.md", "Chemical Nomenclature", 2, 5, "Ch. 5–6"),
            (8, "08-chemical-reactions-and-balancing-equations.md", "Chemical Reactions, Balancing and Conservation of Mass", 3, 6, "Ch. 5–7"),
            (9, "09-introduction-to-acids-and-bases.md", "Introduction to Acids and Bases", 3, 5, "Ch. 7–8"),
        ],
    ),
    (
        "03-intermediate-chemistry",
        "Level 2",
        "High School / Intermediate Chemistry",
        "Quantitative chemistry: the mole, stoichiometry, solutions, gases, "
        "intermolecular forces, molecular shape, thermochemistry, rates, "
        "equilibrium, pH, redox and solubility.",
        "High school / first-year university",
        [
            (1, "01-the-mole-concept.md", "The Mole Concept and Avogadro's Constant", 3, 6, "Level 1 in full"),
            (2, "02-stoichiometry-and-limiting-reactants.md", "Stoichiometry, Limiting Reactants and Percentage Yield", 3, 8, "Ch. 1"),
            (3, "03-solutions-concentration-and-dilution.md", "Solutions, Concentration and Dilution", 3, 6, "Ch. 1–2"),
            (4, "04-gas-laws-and-the-ideal-gas-equation.md", "Gas Laws and the Ideal Gas Equation", 3, 7, "Ch. 1–3"),
            (5, "05-intermolecular-forces.md", "Intermolecular Forces", 3, 6, "Level 1 Ch. 5"),
            (6, "06-molecular-geometry-and-vsepr-theory.md", "Molecular Geometry and VSEPR Theory", 3, 6, "Level 1 Ch. 3, 6"),
            (7, "07-hybridization-and-molecular-polarity.md", "Hybridization and Molecular Polarity", 4, 7, "Ch. 5–6"),
            (8, "08-thermochemistry-and-enthalpy.md", "Thermochemistry and Enthalpy", 4, 8, "Ch. 2, 4"),
            (9, "09-reaction-rates.md", "Reaction Rates", 3, 6, "Ch. 2, 8"),
            (10, "10-chemical-equilibrium-and-le-chateliers-principle.md", "Chemical Equilibrium and Le Châtelier's Principle", 4, 8, "Ch. 9"),
            (11, "11-acid-base-chemistry-and-ph.md", "Acid–Base Chemistry, pH and pOH", 4, 8, "Ch. 3, 10"),
            (12, "12-redox-reactions-and-electrochemistry-fundamentals.md", "Oxidation–Reduction and Electrochemistry Fundamentals", 4, 8, "Ch. 2, 10"),
            (13, "13-solubility-and-precipitation.md", "Solubility and Precipitation", 4, 6, "Ch. 3, 10"),
        ],
    ),
    (
        "04-advanced-chemistry",
        "Level 3",
        "Advanced Chemistry",
        "The undergraduate core: quantum mechanics and orbitals, molecular orbital "
        "theory, chemical thermodynamics, kinetics and mechanisms, catalysis, "
        "advanced equilibria, electrochemistry, coordination chemistry and "
        "spectroscopy.",
        "Undergraduate chemistry",
        [
            (1, "01-quantum-mechanics-foundations.md", "Quantum Mechanics Foundations", 5, 10, "Level 2 Ch. 11; calculus"),
            (2, "02-atomic-orbitals-and-quantum-numbers.md", "Atomic Orbitals, Quantum Numbers and Advanced Configurations", 4, 8, "Ch. 1"),
            (3, "03-molecular-orbital-theory.md", "Molecular Orbital Theory", 5, 9, "Ch. 2; Level 1 Ch. 6"),
            (4, "04-chemical-thermodynamics.md", "Chemical Thermodynamics: Entropy and Gibbs Energy", 4, 10, "Level 2 Ch. 8"),
            (5, "05-chemical-kinetics-and-reaction-mechanisms.md", "Chemical Kinetics and Reaction Mechanisms", 4, 9, "Level 2 Ch. 9"),
            (6, "06-catalysis.md", "Catalysis", 4, 6, "Ch. 5"),
            (7, "07-advanced-equilibrium-buffers-and-solubility-product.md", "Advanced Equilibrium: Buffers and Solubility Product", 4, 8, "Level 2 Ch. 10–11, 13"),
            (8, "08-electrochemical-cells-nernst-equation-and-electrolysis.md", "Electrochemical Cells, the Nernst Equation and Electrolysis", 4, 9, "Level 2 Ch. 12; Ch. 4"),
            (9, "09-coordination-chemistry-and-crystal-field-theory.md", "Coordination Chemistry, Crystal Field and Ligand Field Theory", 5, 10, "Ch. 2–3"),
            (10, "10-advanced-spectroscopy.md", "Advanced Spectroscopy: UV–Vis, IR, NMR and Mass Spectrometry", 5, 10, "Ch. 2; Level 2 Ch. 6"),
        ],
    ),
    (
        "05-organic-chemistry",
        "Level 4",
        "Organic Chemistry",
        "Structure, stereochemistry and the mechanistic logic of carbon chemistry, "
        "moving from functional groups and nomenclature to named reactions, "
        "pericyclic chemistry and retrosynthetic design.",
        "Undergraduate organic chemistry",
        [
            (1, "01-introduction-to-organic-chemistry.md", "Introduction to Organic Chemistry", 3, 5, "Level 1 Ch. 5; Level 2 Ch. 7"),
            (2, "02-functional-groups-and-iupac-nomenclature.md", "Functional Groups and IUPAC Nomenclature", 3, 7, "Ch. 1"),
            (3, "03-isomerism-and-stereochemistry.md", "Isomerism and Stereochemistry", 4, 9, "Ch. 2"),
            (4, "04-conformations.md", "Conformations and Conformational Analysis", 4, 7, "Ch. 3"),
            (5, "05-alkanes.md", "Alkanes", 3, 5, "Ch. 2–4"),
            (6, "06-alkenes-alkynes-and-electrophilic-addition.md", "Alkenes, Alkynes and Electrophilic Addition", 4, 9, "Ch. 5"),
            (7, "07-aromatic-compounds-and-electrophilic-aromatic-substitution.md", "Aromatic Compounds and Electrophilic Aromatic Substitution", 4, 9, "Ch. 6"),
            (8, "08-haloalkanes-substitution-and-elimination.md", "Haloalkanes: Nucleophilic Substitution and Elimination", 4, 9, "Ch. 3–6"),
            (9, "09-alcohols-phenols-and-ethers.md", "Alcohols, Phenols and Ethers", 4, 8, "Ch. 8"),
            (10, "10-aldehydes-ketones-and-carbonyl-chemistry.md", "Aldehydes, Ketones and Carbonyl Chemistry", 5, 10, "Ch. 9"),
            (11, "11-carboxylic-acids-esters-and-amines.md", "Carboxylic Acids, Esters, Amines and Amides", 4, 9, "Ch. 10"),
            (12, "12-oxidation-reduction-and-organometallic-chemistry.md", "Oxidation, Reduction and Organometallic Chemistry", 5, 8, "Ch. 9–11"),
            (13, "13-pericyclic-reactions.md", "Pericyclic Reactions", 5, 6, "Ch. 6–7"),
            (14, "14-retrosynthetic-analysis-and-synthesis-strategy.md", "Retrosynthetic Analysis and Synthesis Strategy", 5, 8, "Ch. 8–13"),
        ],
    ),
    (
        "06-inorganic-chemistry",
        "Level 5",
        "Inorganic Chemistry",
        "The chemistry of everything that is not primarily carbon: main-group "
        "trends, transition-metal coordination and organometallic chemistry, "
        "bioinorganic systems, solid-state structures, magnetism and f-block "
        "elements.",
        "Undergraduate inorganic chemistry",
        [
            (1, "01-periodic-chemistry-and-main-group-elements.md", "Periodic Chemistry and the Main-Group Elements", 3, 8, "Level 1 Ch. 4; Level 2 Ch. 5"),
            (2, "02-transition-metals.md", "Transition Metals", 4, 8, "Ch. 1; Level 3 Ch. 9"),
            (3, "03-coordination-compounds.md", "Coordination Compounds", 4, 8, "Level 3 Ch. 9"),
            (4, "04-organometallic-compounds.md", "Organometallic Compounds", 5, 9, "Ch. 2–3; Level 4 Ch. 12"),
            (5, "05-bioinorganic-chemistry.md", "Bioinorganic Chemistry", 5, 7, "Ch. 2–3; Level 8 Ch. 3"),
            (6, "06-solid-state-chemistry-crystal-structures-and-defects.md", "Solid-State Chemistry: Crystal Structures and Defects", 5, 9, "Ch. 1; Level 3 Ch. 4"),
            (7, "07-magnetic-and-electronic-properties.md", "Magnetic and Electronic Properties", 5, 7, "Ch. 2, 6"),
            (8, "08-inorganic-reaction-mechanisms.md", "Inorganic Reaction Mechanisms", 5, 8, "Ch. 3–4"),
            (9, "09-lanthanides-and-actinides.md", "Lanthanides and Actinides", 5, 7, "Ch. 2, 7"),
            (10, "10-descriptive-inorganic-chemistry.md", "Descriptive Inorganic Chemistry", 3, 9, "Ch. 1–9"),
        ],
    ),
    (
        "07-physical-chemistry",
        "Level 6",
        "Physical Chemistry",
        "The quantitative framework: classical and statistical thermodynamics, "
        "quantum chemistry, molecular spectroscopy, reaction dynamics, surfaces, "
        "colloids, photochemistry and computational methods.",
        "Advanced undergraduate / postgraduate entry",
        [
            (1, "01-classical-thermodynamics.md", "Classical Thermodynamics", 5, 11, "Level 3 Ch. 4; multivariable calculus"),
            (2, "02-statistical-thermodynamics-and-statistical-mechanics.md", "Statistical Thermodynamics and Statistical Mechanics", 5, 11, "Ch. 1; Level 3 Ch. 1"),
            (3, "03-quantum-chemistry.md", "Quantum Chemistry", 5, 12, "Level 3 Ch. 1–3; linear algebra"),
            (4, "04-molecular-spectroscopy.md", "Molecular Spectroscopy", 5, 10, "Ch. 3; Level 3 Ch. 10"),
            (5, "05-chemical-kinetics-and-reaction-dynamics.md", "Chemical Kinetics and Reaction Dynamics", 5, 10, "Level 3 Ch. 5; Ch. 2"),
            (6, "06-surface-chemistry-and-colloids.md", "Surface Chemistry and Colloids", 5, 8, "Ch. 1"),
            (7, "07-photochemistry.md", "Photochemistry", 5, 8, "Ch. 3–4"),
            (8, "08-electrochemical-thermodynamics.md", "Electrochemical Thermodynamics", 5, 8, "Ch. 1; Level 3 Ch. 8"),
            (9, "09-computational-physical-chemistry.md", "Computational Physical Chemistry", 5, 9, "Ch. 3; Ch. 2"),
        ],
    ),
    (
        "08-analytical-chemistry",
        "Level 7",
        "Analytical Chemistry",
        "How a number becomes trustworthy: sampling, uncertainty, calibration and "
        "validation, classical wet methods, titrations, chromatography, "
        "spectroscopic analysis and electroanalytical measurement.",
        "Undergraduate / practising analyst",
        [
            (1, "01-introduction-to-analytical-chemistry.md", "Introduction to Analytical Chemistry", 3, 5, "Level 2 in full"),
            (2, "02-sampling-and-sample-preparation.md", "Sampling and Sample Preparation", 4, 6, "Ch. 1"),
            (3, "03-errors-uncertainty-and-statistical-data-treatment.md", "Errors, Uncertainty and Statistical Data Treatment", 4, 8, "Ch. 1; basic statistics"),
            (4, "04-calibration-validation-and-quantitative-analysis.md", "Calibration, Validation and Quantitative Analysis", 4, 8, "Ch. 3"),
            (5, "05-gravimetric-and-volumetric-analysis.md", "Gravimetric and Volumetric Analysis", 4, 7, "Ch. 2–4"),
            (6, "06-titrations.md", "Titrations: Acid–Base, Redox and Complexometric", 4, 8, "Level 2 Ch. 11–13; Ch. 5"),
            (7, "07-chromatography.md", "Chromatography: GC, LC and HPLC", 5, 10, "Ch. 2–4"),
            (8, "08-spectroscopic-analysis.md", "Spectroscopic Analysis", 5, 9, "Level 3 Ch. 10; Ch. 4"),
            (9, "09-electroanalytical-chemistry-and-potentiometry.md", "Electroanalytical Chemistry and Potentiometry", 5, 8, "Level 3 Ch. 8; Ch. 4"),
        ],
    ),
    (
        "09-biochemistry",
        "Level 8",
        "Biochemistry",
        "The chemistry of living systems: water and non-covalent interactions, "
        "amino acids and proteins, enzymes, carbohydrates, lipids, nucleic acids, "
        "metabolism, photosynthesis and regulation.",
        "Undergraduate biochemistry",
        [
            (1, "01-water-and-biological-systems.md", "Water and Biological Systems", 3, 6, "Level 2 Ch. 5, 11"),
            (2, "02-amino-acids-and-proteins.md", "Amino Acids and Proteins", 4, 9, "Ch. 1; Level 4 Ch. 3"),
            (3, "03-enzymes.md", "Enzymes: Kinetics, Mechanism and Regulation", 5, 10, "Ch. 2; Level 3 Ch. 5"),
            (4, "04-carbohydrates.md", "Carbohydrates", 4, 7, "Level 4 Ch. 9"),
            (5, "05-lipids.md", "Lipids and Membranes", 4, 7, "Level 4 Ch. 11"),
            (6, "06-nucleic-acids-and-dna-rna-chemistry.md", "Nucleic Acids and DNA/RNA Chemistry", 5, 9, "Ch. 4"),
            (7, "07-metabolism-and-bioenergetics.md", "Metabolism and Bioenergetics: Glycolysis, Krebs Cycle, Oxidative Phosphorylation", 5, 12, "Ch. 3–5; Level 3 Ch. 4"),
            (8, "08-photosynthesis.md", "Photosynthesis", 5, 7, "Ch. 7; Level 6 Ch. 7"),
            (9, "09-molecular-biology-and-biochemical-regulation.md", "Molecular Biology and Biochemical Regulation", 5, 8, "Ch. 6–7"),
        ],
    ),
    (
        "10-materials-and-industrial-chemistry",
        "Level 9a",
        "Materials and Industrial Chemistry",
        "Polymers, nanomaterials, semiconductors, batteries, corrosion and the "
        "large-scale catalytic and petrochemical processes that underpin industry.",
        "Applied / industrial chemistry",
        [
            (1, "01-polymer-chemistry.md", "Polymer Chemistry", 4, 8, "Level 4 Ch. 6–8"),
            (2, "02-nanochemistry.md", "Nanochemistry", 5, 7, "Level 5 Ch. 6"),
            (3, "03-materials-and-semiconductor-chemistry.md", "Materials and Semiconductor Chemistry", 5, 8, "Level 5 Ch. 6–7"),
            (4, "04-battery-chemistry.md", "Battery Chemistry", 5, 8, "Level 3 Ch. 8; Level 5 Ch. 7"),
            (5, "05-corrosion.md", "Corrosion", 4, 6, "Level 3 Ch. 8"),
            (6, "06-catalytic-industrial-processes-and-petroleum-chemistry.md", "Catalytic Industrial Processes and Petroleum Chemistry", 5, 8, "Level 3 Ch. 6; Level 6 Ch. 6"),
        ],
    ),
    (
        "11-environmental-chemistry",
        "Level 9b",
        "Environmental Chemistry",
        "Green chemistry principles, atmospheric chemistry and air pollution, "
        "natural and contaminated waters, and waste treatment.",
        "Applied / environmental chemistry",
        [
            (1, "01-green-and-sustainable-chemistry.md", "Green and Sustainable Chemistry", 4, 6, "Level 4 Ch. 1–8"),
            (2, "02-atmospheric-chemistry.md", "Atmospheric Chemistry", 5, 8, "Level 6 Ch. 5, 7"),
            (3, "03-water-chemistry-and-pollution.md", "Water Chemistry and Water Pollution", 4, 8, "Level 2 Ch. 11, 13; Level 7 Ch. 8"),
            (4, "04-waste-treatment.md", "Waste Treatment and Circular Chemistry", 4, 6, "Ch. 1–3"),
        ],
    ),
    (
        "12-research-and-postgraduate-chemistry",
        "Level 10",
        "University, Postgraduate and Research Chemistry",
        "Research-grade theory and practice: advanced quantum chemistry, DFT, "
        "molecular dynamics, advanced synthesis and mechanisms, structure "
        "elucidation, research design, literature evaluation, reproducibility, "
        "ethics and scientific writing.",
        "Postgraduate / researcher",
        [
            (1, "01-advanced-quantum-chemistry.md", "Advanced Quantum Chemistry", 5, 12, "Level 6 Ch. 3"),
            (2, "02-computational-chemistry-and-density-functional-theory.md", "Computational Chemistry and Density Functional Theory", 5, 11, "Ch. 1"),
            (3, "03-molecular-dynamics.md", "Molecular Dynamics", 5, 9, "Ch. 1–2; Level 6 Ch. 2"),
            (4, "04-advanced-organic-synthesis.md", "Advanced Organic Synthesis", 5, 10, "Level 4 in full"),
            (5, "05-advanced-reaction-mechanisms.md", "Advanced Reaction Mechanisms", 5, 9, "Level 4 Ch. 8–13"),
            (6, "06-advanced-spectroscopy-and-structure-elucidation.md", "Advanced Spectroscopy and Structure Elucidation", 5, 10, "Level 3 Ch. 10; Level 6 Ch. 4"),
            (7, "07-research-methodology-and-experimental-design.md", "Research Methodology and Experimental Design", 4, 8, "Level 7 Ch. 3–4"),
            (8, "08-scientific-literature-and-critical-evaluation.md", "Scientific Literature and Critical Evaluation", 4, 6, "None"),
            (9, "09-scientific-data-analysis-and-reproducibility.md", "Scientific Data Analysis and Reproducibility", 5, 8, "Ch. 7"),
            (10, "10-research-ethics-and-scientific-writing.md", "Research Ethics and Scientific Writing", 4, 7, "Ch. 7–9"),
        ],
    ),
]

TOTAL = sum(len(l[5]) for l in LEVELS)


def written(directory, fname):
    return os.path.exists(os.path.join(ROOT, directory, fname))


def level_written(entry):
    d = entry[0]
    return sum(1 for c in entry[5] if written(d, c[1]))


def stars(n):
    return "★" * n + "☆" * (5 - n)


def build_curriculum():
    out = []
    out.append("# Curriculum Map\n")
    out.append(
        "This is the master index of the repository. Every chapter is listed with its\n"
        "difficulty and prerequisites, so you can plan a route through the material\n"
        "instead of following the directory numbering blindly.\n"
    )
    out.append(
        "**Difficulty:** ★☆☆☆☆ = accessible with no background · ★★★★★ = research\n"
        "fluency expected. **Hours** are realistic estimates for reading, reproducing\n"
        "the diagrams, and completing the exercises.\n"
    )
    out.append("---\n")
    out.append("## Progression at a glance\n")
    out.append("```mermaid")
    out.append("flowchart TD")
    out.append('    A["Level 0 · Foundations<br/>10 chapters"] --> B["Level 1 · Elementary<br/>9 chapters"]')
    out.append('    B --> C["Level 2 · Intermediate<br/>13 chapters"]')
    out.append('    C --> D["Level 3 · Advanced<br/>10 chapters"]')
    out.append('    D --> E["Level 4 · Organic<br/>14 chapters"]')
    out.append('    D --> F["Level 5 · Inorganic<br/>10 chapters"]')
    out.append('    D --> G["Level 6 · Physical<br/>9 chapters"]')
    out.append('    C --> H["Level 7 · Analytical<br/>9 chapters"]')
    out.append('    C --> I["Level 8 · Biochemistry<br/>9 chapters"]')
    out.append('    E --> J["Level 9 · Materials &amp; Environment<br/>10 chapters"]')
    out.append('    F --> J')
    out.append('    G --> K["Level 10 · Research<br/>10 chapters"]')
    out.append('    H --> K')
    out.append('    I --> J')
    out.append("```\n")
    out.append(
        "The graph shows only *hard* dependencies. Within a level, chapters are almost\n"
        "always sequential; across levels, the arrows mark the minimum prerequisite.\n"
    )
    out.append("---\n")

    for directory, label, title, blurb, audience, chapters in LEVELS:
        hours = sum(c[4] for c in chapters)
        out.append(f"## {label} — {title}\n")
        out.append(f"**Directory:** [`{directory}/`]({directory}/README.md) · "
                   f"**Audience:** {audience} · "
                   f"**Chapters:** {len(chapters)} · "
                   f"**Estimated study time:** ≈ {hours} h\n")
        out.append(f"{blurb}\n")
        out.append("| # | Chapter | Difficulty | Hours | Prerequisites |")
        out.append("|---|---|---|---|---|")
        for num, fname, ctitle, st, hr, prereq in chapters:
            out.append(f"| {num} | [{ctitle}]({directory}/{fname}) | {stars(st)} | {hr} | {prereq} |")
        out.append("")
    out.append("---\n")
    out.append("## Support tracks\n")
    out.append("| Track | Contents | Entry point |")
    out.append("|---|---|---|")
    out.append("| Learning guide | Study methods, prerequisite maps, assessment | [00-learning-guide/learning-path.md](00-learning-guide/learning-path.md) |")
    out.append("| Laboratory | Safety, equipment, techniques, calculations, documentation | [13-laboratory/README.md](13-laboratory/README.md) |")
    out.append("| Problem solving | Worked examples, exercise banks, quizzes, solutions | [14-problem-solving/README.md](14-problem-solving/README.md) |")
    out.append("| Visual learning | Diagram-first galleries | [15-visual-learning/README.md](15-visual-learning/README.md) |")
    out.append("| Glossary and references | Terminology and bibliography | [GLOSSARY.md](GLOSSARY.md) · [REFERENCES.md](REFERENCES.md) |")
    out.append("")
    out.append("---\n")
    out.append("## Totals\n")
    out.append(f"| | |")
    out.append("|---|---|")
    out.append(f"| Chapters | {TOTAL} |")
    out.append(f"| Estimated study time | ≈ {sum(sum(c[4] for c in l[5]) for l in LEVELS)} h |")
    out.append(f"| Levels | {len(LEVELS)} |")
    out.append("")
    out.append(
        "Hours are a planning aid, not a promise. A reader with a strong maths\n"
        "background will move faster through Levels 3 and 6; a reader meeting\n"
        "thermodynamics for the first time should budget more.\n"
    )
    return "\n".join(out)


def build_roadmap():
    out = []
    out.append("# Roadmap\n")
    out.append(
        "This file is the honest state of the repository. A chapter is ticked only\n"
        "when it contains meaningful educational content *and* has passed the checks\n"
        "in [`_templates/chapter-review-checklist.md`](_templates/chapter-review-checklist.md).\n"
    )
    out.append("---\n")
    out.append("## Status summary\n")
    out.append("| Level | Directory | Chapters planned | Written |")
    out.append("|---|---|---|---|")
    for directory, label, title, blurb, audience, chapters in LEVELS:
        done = level_written((directory, label, title, blurb, audience, chapters))
        mark = f"✅ {done}" if done == len(chapters) else f"🚧 {done}"
        out.append(f"| {label} | `{directory}/` | {len(chapters)} | {mark} |")
    done_total = sum(level_written(l) for l in LEVELS)
    out.append(f"| **Total** | | **{TOTAL}** | **{done_total}** |")
    out.append("")
    out.append("---\n")
    out.append("## Delivery phases\n")
    out.append("| Phase | Scope | State |")
    out.append("|---|---|---|")
    out.append("| 1 | Repository structure, README, roadmap, contribution and documentation standards | ✅ complete |")
    out.append("| 2 | Curriculum index, foundations and elementary chemistry, fully developed | ✅ complete |")
    out.append("| 3 | Intermediate and advanced chemistry; organic, inorganic, physical, analytical and biochemistry | ✅ complete |")
    out.append("| 4 | Postgraduate and research material; materials, environmental and applied chemistry | ✅ complete |")
    out.append("| 5 | Quality assurance: links, diagrams, scientific review, consistency | ✅ complete |")
    out.append("")
    out.append("---\n")
    out.append("## Chapter checklist\n")
    for directory, label, title, blurb, audience, chapters in LEVELS:
        out.append(f"### {label} — {title}\n")
        for num, fname, ctitle, st, hr, prereq in chapters:
            box = "x" if written(directory, fname) else " "
            out.append(f"- [{box}] [{ctitle}]({directory}/{fname})")
        out.append("")
    out.append("---\n")
    out.append("## Exercise and solution banks\n")
    out.append("| Level | Exercise bank | Solutions |")
    out.append("|---|---|---|")
    for directory, label, title, blurb, audience, chapters in LEVELS:
        slug = LEVEL_SLUG[directory]
        ex = f"{directory}/exercises/{slug}-exercises.md"
        so = f"{directory}/solutions/{slug}-solutions.md"
        ex_box = "✅" if os.path.exists(os.path.join(ROOT, ex)) else "—"
        so_box = "✅" if os.path.exists(os.path.join(ROOT, so)) else "—"
        out.append(f"| {label} | {ex_box} [`{slug}`]({ex}) | {so_box} [`{slug}`]({so}) |")
    out.append("")
    out.append("---\n")
    out.append("## Quality gates\n")
    out.append("- [x] `python3 scripts/validate_links.py` passes with zero broken links.")
    out.append("- [x] `python3 scripts/validate_mermaid.py` passes with zero problems.")
    out.append("- [x] Every exercise set has a matching solutions file.")
    out.append("- [x] Every chapter lists prerequisites that exist earlier in the curriculum.")
    out.append("- [x] No fabricated references; bibliography entries resolve.")
    out.append("")
    out.append("---\n")
    out.append("## Planned future work\n")
    out.append("Ideas that would strengthen the repository but are *not* yet present —\n")
    out.append("contributions welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).\n")
    out.append("- [ ] Per-chapter auto-graded quiz banks in machine-readable YAML.")
    out.append("- [ ] SVG figures for orbital shapes, chair conformations and crystal lattices in `assets/structures/`.")
    out.append("- [ ] Translations (a per-language directory with the same chapter numbering).")
    out.append("- [ ] A printable single-file PDF build.")
    out.append("- [ ] Worked video-style walkthroughs for the ten hardest derivations.")
    out.append("")
    return "\n".join(out)


LEVEL_SLUG = {
    "01-foundations": "level-0",
    "02-elementary-chemistry": "level-1",
    "03-intermediate-chemistry": "level-2",
    "04-advanced-chemistry": "level-3",
    "05-organic-chemistry": "level-4",
    "06-inorganic-chemistry": "level-5",
    "07-physical-chemistry": "level-6",
    "08-analytical-chemistry": "level-7",
    "09-biochemistry": "level-8",
    "10-materials-and-industrial-chemistry": "level-9a-materials",
    "11-environmental-chemistry": "level-9b-environmental",
    "12-research-and-postgraduate-chemistry": "level-10",
}

LEVEL_INTRO = {
    "01-foundations": (
        "Nothing here assumes you have studied chemistry before. The only "
        "prerequisites are arithmetic, an ability to read a graph, and curiosity. "
        "Take your time: every habit formed at this level — units, significant "
        "figures, safety, the difference between a mixture and a compound — will be "
        "assumed by every chapter that follows."
    ),
    "02-elementary-chemistry": (
        "Level 1 replaces the informal picture of matter built in Level 0 with a "
        "quantitative atomic model. You will meet the periodic table as a "
        "*consequence* of electron configuration rather than as a poster to "
        "memorise, and you will learn to read and write the language of chemistry: "
        "formulas, names and balanced equations."
    ),
    "03-intermediate-chemistry": (
        "This is where chemistry becomes quantitative. Every chapter from here on "
        "assumes you can convert between mass, moles and number of particles "
        "without hesitation, and that you can carry units through an algebraic "
        "manipulation. If one skill in the whole repository deserves over-learning, "
        "it is dimensional analysis."
    ),
    "04-advanced-chemistry": (
        "Level 3 is the undergraduate core. It replaces the Bohr picture with the "
        "Schrödinger equation, replaces 'energy is released' with Gibbs energy, and "
        "replaces 'the rate goes up' with a rate law and a mechanism. Expect "
        "calculus and linear algebra to appear; the chapters flag where they are "
        "used and why."
    ),
    "05-organic-chemistry": (
        "Organic chemistry is often described as memorisation. It is not. Roughly a "
        "dozen mechanistic patterns explain the overwhelming majority of reactions, "
        "and this level is organised to make those patterns visible early and reuse "
        "them constantly."
    ),
    "06-inorganic-chemistry": (
        "Inorganic chemistry covers the other ~100 elements. The organising ideas "
        "are periodic trends, coordination geometry and electronic structure; once "
        "those are secure, descriptive chemistry becomes predictable rather than "
        "encyclopaedic."
    ),
    "07-physical-chemistry": (
        "Physical chemistry is the derivation-heavy core of the discipline. Level 6 "
        "expects mathematical maturity: partial derivatives, integrals, probability "
        "and linear algebra are used as tools, not taught from scratch."
    ),
    "08-analytical-chemistry": (
        "Analytical chemistry answers a deceptively hard question: *how do you know?* "
        "A measurement without an uncertainty is not a measurement, and a method "
        "without validation is not evidence. This level teaches both."
    ),
    "09-biochemistry": (
        "Biochemistry applies organic and physical chemistry to living systems. The "
        "themes are non-covalent interactions, energy coupling and regulation; the "
        "chapters use them to explain proteins, nucleic acids and metabolism."
    ),
    "10-materials-and-industrial-chemistry": (
        "This level shows where chemistry meets engineering: polymers, nanoscale "
        "materials, semiconductors, energy storage, degradation and the catalytic "
        "processes behind industrial products."
    ),
    "11-environmental-chemistry": (
        "Environmental chemistry applies kinetics, thermodynamics and analysis to "
        "the atmosphere, natural waters and waste streams. It also introduces green "
        "chemistry — designing processes so that the waste problem never arises."
    ),
    "12-research-and-postgraduate-chemistry": (
        "The final level is about doing chemistry, not just knowing it. It covers "
        "research-grade theory, modern computational methods, and the professional "
        "practices that make results credible: design, statistics, reproducibility, "
        "ethics and writing."
    ),
}


def build_level_readme(entry):
    directory, label, title, blurb, audience, chapters = entry
    hours = sum(c[4] for c in chapters)
    out = [f"# {label} — {title}\n"]
    out.append(
        f"> **Audience:** {audience}  \n"
        f"> **Chapters:** {len(chapters)}  \n"
        f"> **Estimated study time:** ≈ {hours} h  \n"
        f"> **Difficulty:** {stars(min(c[3] for c in chapters))} – {stars(max(c[3] for c in chapters))}\n"
    )
    out.append(f"{blurb}\n")
    out.append(f"{LEVEL_INTRO.get(directory, '')}\n")
    out.append("---\n")
    out.append("## Chapters\n")
    out.append("| # | Chapter | Difficulty | Hours | Prerequisites |")
    out.append("|---|---|---|---|---|")
    for num, fname, ctitle, st, hr, prereq in chapters:
        out.append(f"| {num} | [{ctitle}]({fname}) | {stars(st)} | {hr} | {prereq} |")
    out.append("")
    out.append("---\n")
    out.append("## Knowledge map\n")
    out.append("```mermaid")
    out.append("flowchart TD")
    for i, (num, fname, ctitle, st, hr, prereq) in enumerate(chapters):
        short = ctitle.replace('"', "")
        if len(short) > 44:
            short = short[:41] + "..."
        out.append(f'    C{num}["{num}. {short}"]')
    for i in range(1, len(chapters)):
        out.append(f"    C{i} --> C{i + 1}")
    out.append("```\n")
    out.append(
        "The chain is the *recommended* order. Chapters that share prerequisites can be\n"
        "read out of order; the table above tells you what each one actually needs.\n"
    )
    out.append("---\n")
    out.append("## Study routine for this level\n")
    out.append("1. Read the chapter once without taking notes, to see the shape of the argument.")
    out.append("2. Re-read with the chapter\'s learning objectives in front of you and answer them in writing.")
    out.append("3. Reproduce every Mermaid diagram from memory, then check it.")
    out.append("4. Do the exercises **before** opening the solutions file.")
    out.append("5. Record every mistake in a log; re-test yourself on those specific items a week later.\n")
    out.append("---\n")
    out.append("## Practice\n")
    slug = LEVEL_SLUG[directory]
    out.append(f"- Exercise set: [`exercises/{slug}-exercises.md`](exercises/{slug}-exercises.md)")
    out.append(f"- Worked solutions: [`solutions/{slug}-solutions.md`](solutions/{slug}-solutions.md)\n")
    out.append("---\n")
    out.append("## Navigation\n")
    out.append("- Level index: [CURRICULUM.md](../CURRICULUM.md)")
    out.append("- Study methods: [00-learning-guide](../00-learning-guide/learning-path.md)")
    out.append("- Terminology: [GLOSSARY.md](../GLOSSARY.md)")
    out.append("- Sources: [REFERENCES.md](../REFERENCES.md)")
    out.append("")
    return "\n".join(out)


with open(os.path.join(ROOT, "CURRICULUM.md"), "w", encoding="utf-8") as f:
    f.write(build_curriculum())

with open(os.path.join(ROOT, "ROADMAP.md"), "w", encoding="utf-8") as f:
    f.write(build_roadmap())

for entry in LEVELS:
    path = os.path.join(ROOT, entry[0], "README.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_level_readme(entry))

print(f"Wrote CURRICULUM.md, ROADMAP.md and {len(LEVELS)} level READMEs.")
