# DNA Toolkit & Bioinformatics Analyzer
A comprehensive collection of Python scripts for bioinformatics analysis, ranging from basic DNA sequence manipulation to gene expression data visualization.

## Overview
This toolkit contains several scripts designed for different levels of analysis:

1.  **`bioinformatics_toolkit.py`** - The most advanced script, combining sequence analysis (mutations, motifs) with data science (gene expression stats, plotting).
2.  **`gene_expression_analyzer.py`** - Dedicated tool for analyzing and visualizing gene expression data using Pandas and Matplotlib.
3.  **`dna_toolkit_v2_fasta.py`** - Efficient tool for processing multiple DNA sequences from FASTA files.
4.  **`dna_toolkit_v1.py`** - Basic starter script for single sequence analysis.


### Sequence Analysis
-   **GC Content**: Calculate Guanine-Cytosine percentage.
-   **Reverse Complement**: Generate the reverse complement of DNA strands.
-   **Transcription**: Convert DNA to RNA.
-   **Mutation Detection**: Compare sample sequences against a reference to identify point mutations.
-   **Motif Search**: Locate specific subsequences within DNA data.

### Data Analysis & Visualization
-   **Gene Expression Statistics**: Calculate mean, max, min, and filter highly expressed genes.
-   **Visualizations**:
    -   Bar charts for expression levels.
    -   Heatmaps for sample comparison.
-   **File Support**: Handles `.txt`, `.fasta`, `.csv`, and `.xlsx` files.

## Requirements
The basic scripts (`v1`, `v2`) run with standard Python. The advanced analysis scripts require external libraries.


## File Structure
-   `data/` - Contains input files (`example_sequences.fasta`, `gene_expression.csv`, etc.).
-   `bioinformatics_toolkit.py` - Main integrated analysis script.
-   `gene_expression_analyzer.py` - Data analysis script.
-   `dna_toolkit_v2_fasta.py` - FASTA processor.

## Usage
### Running the Bioinformatics Toolkit
This script performs both sequence analysis and gene expression analysis.

### Analyzing Gene Expression
To generate plots and statistics for gene expression data:

### Basic FASTA Analysis
To process raw DNA sequences:
This will read all sequences from `example_sequences.fasta` and output analysis results for each sequence.

### Output Format

DNA TOOLKIT RESULTS

Sequence Name: seq1
Sequence: ATGCGTAA
GC Content: 37.5%
Reverse Complement: TTACGCAT
RNA Transcription: AUGCGUAA

Sequence Name: seq2
Sequence: GCGCGCTA
GC Content: 75.0%
Reverse Complement: TAGCGCGC
RNA Transcription: GCGCGCUA


## FASTA File Format
FASTA files contain sequences with headers. Each header starts with `>` followed by a sequence name:

```
>sequence_name_1
ATGCGTAA
>sequence_name_2
GCGCGCTA
>sequence_name_3
TTATGC
```

## How It Works
1. **Read FASTA File** - The script reads the `example_sequences.fasta` file
2. **Parse Sequences** - Identifies sequence headers (lines starting with `>`) and sequence data
3. **Store Sequences** - Saves each sequence name and its corresponding DNA sequence
4. **Analyze Each Sequence** - Applies all three analysis functions to every sequence
5. **Display Results** - Prints formatted output with all analysis results

## Getting Started
1. Place your DNA sequences in FASTA format in a file named `example_sequences.fasta` in the same directory
2. Run `python dna_toolkit_v2_fasta.py`
3. View the analysis results in the terminal output

## Supported DNA Bases
The toolkit recognizes the following DNA bases:
- **A** - Adenine
- **T** - Thymine
- **G** - Guanine
- **C** - Cytosine

## Notes

- The script is designed for beginner-level learning
- Sequences should contain only uppercase A, T, G, C bases
- Empty lines in FASTA files are automatically skipped
- The script can be run from any directory (uses relative file paths)

## Author
Created as a beginner bioinformatics learning tool.
