{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # NGS QC Pipeline\
\
This project implements a simple bioinformatics pipeline for quality control of sequencing data using Python.\
\
## Features\
- Reads FASTA files\
- Calculates sequence length\
- Counts ambiguous bases (N)\
- Generates a QC summary report in CSV format\
\
## Requirements\
- Python 3\
- Biopython\
- pandas\
\
## Usage\
```bash\
python scripts/qc_sequences.py\
}
## Run
pip install -r requirements.txt
python scripts/qc_sequences.py
