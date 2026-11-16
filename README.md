# Genomic Sequence Analyzer

#### Description:

Genomic Sequence Analyzer is a command-line bioinformatics tool designed to parse, analyze, and extract biological metrics from DNA sequences provided in FASTA format. Built entirely in Python, this tool bridges computational logic with molecular biology, allowing users to rapidly calculate GC content, count nucleotides, and generate sequence reports directly in the terminal or exported as a CSV file.

This project was developed as the final project for CS50's Introduction to Programming with Python (CS50P).

## Project Structure and Files

The project is modularly designed, separating the core biological logic from the command-line interface and file input/output operations.

- `dna.py`: The biological engine of the project. It contains the `DNA` object-oriented class. When instantiated with a DNA string, this class normalizes the sequence, validates its length (minimum of 3 nucleotides), and provides methods for various biological processes:
  - `nucleotides`: Returns a dictionary counting the occurrences of Adenine (A), Thymine (T), Cytosine (C), and Guanine (G).
  - `gc_content()`: Calculates the percentage of G and C nucleotides in the sequence, a crucial metric for determining DNA stability.
  - `transcript()`: Simulates transcription by replacing Thymine (T) with Uracil (U) to form mRNA.
  - `translate()`: Converts the mRNA sequence into a peptide chain (amino acids) using a comprehensive codon dictionary, stopping appropriately if a stop codon (`*`) is reached.
  - `orfs()`: Scans the sequence to identify and count Open Reading Frames by locating "ATG" start codons.
- `project.py`: The main executable script. It handles command-line arguments using `argparse`, validates file paths and extensions using `pathlib`, and parses FASTA files utilizing the `Bio.SeqIO` module from Biopython. It manages the flow of data from reading the input to formatting the output (via `tabulate`) or exporting it (`csv`).
- `test_project.py`: The testing suite. It utilizes `pytest` to ensure the reliability of both the `DNA` class methods and the standalone functions in `project.py`. It leverages fixtures like `tmp_path` to test file generation without cluttering the user's directory, and `capsys` to verify standard terminal output.
- `requirements.txt`: Contains the external dependencies required to run the project (`biopython`, `tabulate`, `pytest`).

## Design Choices

During development, several deliberate design choices were made to ensure the program is robust, scalable, and user-friendly:

1.  **Object-Oriented Biological Logic:** Instead of writing standalone functions for transcription and translation, I encapsulated all biological properties within a `DNA` class. This mimics the real-world nature of a DNA molecule—each sequence has its own inherent properties (GC content, nucleotide counts) and behaviors (translation).
2.  **Terminal Output Pagination:** FASTA files can contain thousands of sequences. To prevent flooding the user's terminal window, the `table_data` function includes an `eliminate=True` parameter by default. If the terminal display (`-s` flag) is triggered, it slices the data to show only the first 10 sequences, adding a visual indicator (`There are other DNA sequences......`) if the file contains more.
3.  **Strict File Validation:** I utilized `pathlib.Path` directly inside the `argparse` configuration. Before any heavy processing or Biopython parsing begins, the script strictly verifies that the input file exists and ends with a valid FASTA extension (`.fasta`, `.fa`, `.fna`). It similarly restricts output files to the `.csv` extension, preventing corrupted file generations.
4.  **Range Boundaries for Translation:** When iterating through the mRNA sequence for translation, I implemented `range(0, len(m_rna)-2, 3)`. This mathematical boundary ensures the loop safely slices codons in chunks of three without raising index errors if the sequence length is not a perfect multiple of three.

## Installation & Usage

### Prerequisites

Ensure you have Python installed. Install the required external libraries by running:

```bash
pip install -r requirements.txt
```

### Usage Examples

Here are some practical command-line examples you can run in your bash terminal to interact with the program:

**1. Quick Terminal Preview**
Analyze a local sequence file and print the results grid directly to the terminal (defaults to showing the first 10 sequences if no output file is specified):

```bash
python project.py sample_data/brca1_gene.fasta
```

**2. Generate a Complete CSV Report**
Process a large FASTA file and silently export the full analysis to a CSV file to be opened in Excel or parsed with Pandas:

```bash
python project.py sample_data/viral_genomes.fa -o reports/viral_analysis.csv
```

**3. Export and Preview Simultaneously**
Save the complete dataset to a CSV file while still printing a quick 10-sequence summary to the terminal to ensure the program ran correctly:

```bash
python project.py sample_data/unknown_sequences.fna --output reports/results.csv --show
```
