# Pipeline-QC-sequencing-data

This repository contains a simple and reproducible bioinformatics pipeline for performing quality control (QC) of sequencing data using Python.

The goal of this project is to automate basic QC metrics for sequencing data and generate structured outputs suitable for downstream bioinformatics analysis.

---

## Features
- Reads DNA sequences from FASTA files
- Calculates sequence length
- Counts ambiguous bases (N)
- Computes the percentage of ambiguous bases per sequence
- Generates a QC summary report in CSV format

---

## Input
- FASTA file containing DNA sequences

Example:
data/example_sequences.fasta

---

## Output
- CSV file containing QC metrics per sequence, including:
  - Sequence ID
  - Sequence length
  - Number of ambiguous bases (N)
  - Percentage of ambiguous bases

Example output:
results/qc_summary.csv

---

## Requirements
- Python 3
- Biopython
- pandas

---

## Usage
Run the pipeline from the root directory:
python scripts/qc_sequences.py

## Installation
Install the required dependencies using:

```bash
pip install -r requirements.txt
}



