# 🧬 BioComputing Portfolio: Computational Genomics & Data Pipelines

Welcome to my independent research repository. This space documents my transition from wet-lab biotechnology into **data-driven bioinformatics, structural biological simulations, and algorithmic scripting workflows**. 

---

## 🔬 Core Publications & Preprints

*   **Review Article:** *AI/ML Applications in Blood Cancer (Leukemia) Diagnosis*  
    *   **Abstract Summary:** A comprehensive evaluation synthesizing recent literature on deep learning frameworks applied to blood malignancies. Addressed critical bottleneck barriers including single-hospital dataset generalizability shifts, microscopic imaging constraints, and geographic sample classification biases.
    *   **Repository Registry:** Published as a formal preprint via Zenodo.
    *   **Permanent Identifier:** [DOI: 10.5281/zenodo.22299904](https://doi.org)
## 1. NCBI-Based Sequence Retrieval & Analysis
- **Source Folder:** `/ncbi-sequence-retrieval`
- **Technical Stack:** Python, Biopython (Entrez, SeqIO, SeqUtils), Google Colab
- **Description:** Used Biopython's Entrez module to programmatically fetch gene records from the NCBI nucleotide database (e.g., human TP53), then computed sequence-level statistics such as GC content and sequence length.
- ## 2. Multiple Sequence Alignment & Phylogenetic Analysis of BCR-ABL1 Fusion Variants
- **Technical Stack:** Clustal Omega, phylogenetic tree construction
- **Description:** Aligned four BCR-ABL1 fusion transcript variants (associated with leukemia) using Clustal Omega, identifying a conserved ABL1-derived region and clustering patterns among the variants.
- ## 3. DNA Sequence Quality Control Analyzer
- **Source Folder:** `/dna-sequence-analyzer`
- **Technical Stack:** Python (core logic, no external libraries)
- **Description:** Built a Python tool from scratch to validate DNA sequences, count nucleotide base composition (A, T, G, C), calculate GC content, and compute reverse complements — core operations used in sequence quality control.
- ## 4. Physicochemical & 3D Structural Analysis of Human Insulin
- **Tools Used:** ExPASy ProtParam, RCSB Protein Data Bank, Mol* Viewer
- **Description:** Computed physicochemical properties (molecular weight, instability index, GRAVY/hydropathicity) of human insulin using ExPASy ProtParam, and visualized its hexameric 3D structure (PDB ID: 4EYD) using the RCSB PDB Mol* viewer.
  
- *Developed independently by Anam Abid, as preparation for graduate-level research in bioinformatics and computational biology.*
