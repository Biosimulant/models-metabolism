# models-metabolism

Curated collection of **metabolism** simulation models for the **biosim** platform. This repository contains comprehensive computational models of metabolic pathways, genome-scale metabolic networks (GEMs), central carbon metabolism, energy production, biosynthesis, and organism-specific metabolic reconstructions across bacteria, fungi, plants, and mammals.

## What's Inside

### Models (707 packages)

This is the **largest model repository** with 707 metabolism models, including genome-scale reconstructions, pathway-specific models, and metabolic subsystems.

**Metabolism** — metabolic networks, pathways, and biochemical reactions:

#### Key Model Categories

**Genome-Scale Metabolic Models (GEMs):**
- Bacterial GEMs: E. coli, Salmonella, Streptococcus, Helicobacter, Neisseria, and 100+ other species
- Fungal GEMs: S. cerevisiae, C. albicans, A. niger, and other fungi
- Plant GEMs: Arabidopsis, rice, maize metabolic networks
- Mammalian GEMs: Human Recon models, mouse, rat tissue-specific metabolism
- AGORA collection: Strain-specific gut microbiome metabolic models

**Central Carbon Metabolism:**
- Glycolysis and gluconeogenesis
- TCA cycle (Krebs cycle)
- Pentose phosphate pathway
- Entner-Doudoroff pathway

**Energy Metabolism:**
- Oxidative phosphorylation and ATP synthesis
- Fermentation pathways
- Photosynthesis (plant and cyanobacterial)
- Chemolithotrophy and alternative energy sources

**Amino Acid & Protein Metabolism:**
- Amino acid biosynthesis and degradation
- Nitrogen metabolism and assimilation
- Shikimate pathway (aromatic amino acids)
- Branched-chain amino acid metabolism

**Lipid Metabolism:**
- Fatty acid synthesis and β-oxidation
- Phospholipid and sphingolipid metabolism
- Cholesterol biosynthesis and regulation
- Membrane lipid dynamics

**Nucleotide Metabolism:**
- Purine and pyrimidine biosynthesis
- Salvage pathways
- DNA/RNA precursor synthesis

**Specialized Metabolism:**
- Secondary metabolite production
- Polyketide and non-ribosomal peptide synthesis
- Vitamin and cofactor biosynthesis
- Xenobiotic degradation

**Brain & Neuronal Metabolism:**
- Neuron-astrocyte metabolic coupling
- Brain glucose and lactate metabolism
- Neurotransmitter biosynthesis and recycling

**Symbiotic & Community Metabolism:**
- Syntrophic metabolic interactions
- Cross-feeding networks
- Host-microbiome metabolic exchange
- Drosophila-Wolbachia symbiotic metabolism

**Metabolic Engineering & Biotechnology:**
- Heterologous pathway expression
- Flux optimization for bioproduction
- Ketogulonic acid, biofuel, and chemical production

**Constraint-Based Analysis:**
- Flux balance analysis (FBA) models
- Minimal media growth predictions
- Gene essentiality and knockout simulations
- Membrane economics and resource allocation

**Note:** This repository contains 707 models spanning all domains of life and metabolic processes. For a complete list, see the `models/` directory.

## Layout

```
models-metabolism/
├── models/<model-slug>/     # One model package per folder, each with model.yaml
├── libs/                    # Shared helper code for curated models
├── templates/model-pack/    # Starter template for new model packs
├── scripts/                 # Manifest and entrypoint validation scripts
├── docs/                    # Governance documentation
└── .github/workflows/       # CI/CD pipeline
```

## How It Works

### Model Interface

Every model implements the `biosim.BioModule` interface:

- **`inputs()`** — declares named input signals (e.g., nutrient availability, oxygen)
- **`outputs()`** — declares named output signals (e.g., metabolite concentrations, growth rate)
- **`advance_to(t)`** — advances the metabolic state to time `t`

Genome-scale models typically use constraint-based methods (FBA, FVA) while pathway models use ODE-based kinetics.

### Model Standards

Models in this repository include:
- **SBML format**: Systems Biology Markup Language for metabolic networks
- **Tellurium runtime**: For executing SBML models
- **Constraint-based models**: FBA-compatible GEMs with reactions, metabolites, and gene-protein-reaction (GPR) associations
- **Kinetic models**: ODE-based pathway dynamics with rate laws

## Getting Started

### Prerequisites

- Python 3.11+
- `biosim` framework
- Optional: COBRApy for advanced FBA analysis

### Install biosim

```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

### Using Metabolism Models

1. Reference models by `manifest_path` (e.g., `models/metabolism-sbml-achcar2012-glycolysis-in-bloodstream-form-t-bruc/model.yaml`)
2. Configure nutrient uptake rates and environmental conditions
3. Simulate metabolic flux distributions and growth phenotypes
4. Couple metabolism with gene regulation, signaling, or environmental models

## Validation & CI

Three scripts enforce repository integrity:

| Script | Purpose |
|--------|---------|
| `scripts/validate_manifests.py` | Schema validation for all model.yaml files |
| `scripts/check_entrypoints.py` | Verifies Python entrypoints are importable and callable |
| `scripts/check_public_boundary.sh` | Prevents business-sensitive content in this public repo |

The CI pipeline runs: **secret scan** → **manifest validation** → **smoke sandbox** (Docker).

## Contributing

- All dependencies must use exact version pinning (`==`)
- Model slugs use kebab-case with domain prefix (`metabolism-sbml-`)
- Models must follow the `biosim.BioModule` interface
- SBML models use tellurium or COBRApy runtime

## Domain-Specific Notes

**Metabolism Focus Areas:**
- **Genome-Scale Reconstruction**: Comprehensive metabolic network models with 1000+ reactions
- **Pathway-Level Modeling**: Focused subsystems (glycolysis, TCA, amino acid synthesis)
- **Flux Balance Analysis**: Constraint-based prediction of metabolic states
- **Kinetic Modeling**: Dynamic ODE models with enzyme kinetics and regulation
- **Multi-Organism Models**: Community metabolism and metabolic exchange
- **Clinical & Biotechnology Applications**: Disease metabolism, drug targets, bioproduction

**Organism Coverage:**
- **Bacteria**: 200+ species (gut microbiota, pathogens, model organisms)
- **Archaea**: Methanogenic and extremophile metabolism
- **Fungi**: Yeast, filamentous fungi, pathogens
- **Plants**: C3/C4 photosynthesis, specialized metabolism
- **Animals**: Human tissue-specific, mouse, Drosophila
- **Symbionts**: Endosymbionts, microbiome members

**Model Types:**
- Genome-scale metabolic models (GEMs)
- Core metabolic models (subset of pathways)
- Pathway-specific kinetic models
- Stoichiometric models for FBA
- Dynamic metabolic flux models

## License

This repository is dual-licensed:

- **Code** (scripts, templates, Python modules): Apache-2.0 (`LICENSE-CODE.txt`)
- **Model/content** (manifests, docs, wiring/config): CC BY 4.0 (`LICENSE-CONTENT.txt`)

Attribution guidance: `ATTRIBUTION.md`
