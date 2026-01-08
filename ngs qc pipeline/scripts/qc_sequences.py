from Bio import SeqIO\
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
