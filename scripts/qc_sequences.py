{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from Bio import SeqIO\
import pandas as pd\
\
input_fasta = "data/example_sequences.fasta"\
output_csv = "results/qc_summary.csv"\
\
results = []\
\
for record in SeqIO.parse(input_fasta, "fasta"):\
    sequence = str(record.seq)\
    length = len(sequence)\
    n_count = sequence.upper().count("N")\
    n_percentage = (n_count / length) * 100 if length > 0 else 0\
\
    results.append(\{\
        "sequence_id": record.id,\
        "length": length,\
        "N_count": n_count,\
        "N_percentage": round(n_percentage, 2)\
    \})\
\
df = pd.DataFrame(results)\
df.to_csv(output_csv, index=False)\
\
print("QC analysis completed. Results saved to", output_csv)\
}