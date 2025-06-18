from Bio.Seq import Seq

# 1. Define the DNA sequence
seq_str = (
    "TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTAC"
    "AATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCAC"
    "CTACGGTAGAG"
)

shifted_seq = Seq(seq_str[0:]) # Start from first nucleotide, reading frame 1
# same as ---shifted_seq = Seq(seq_str)
protein = shifted_seq.translate(to_stop=False)
print(protein)

