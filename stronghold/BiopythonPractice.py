from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

sequence = (
    "TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTAC"
    "AATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCAC"
    "CTACGGTAGAG"
)
# Run BLAST (nucleotide blast - blastn)
result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
# blastn searches nucletides against nucleotides (program to use)
# nt is the nucletides database (which database to search against)

# Parse the BLAST output
# default output format is xml(web type format)

# if e value is very, very small, the search was not accidental
blast_record = NCBIXML.read(result_handle)
E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('sequence:', alignment.title)
            print('e value:', hsp.expect)
            print(hsp.match)
# best_hit = blast_record.alignments[0]
# print("Best match title:", best_hit.title)
# print("E-value:", blast_record.descriptions[0].e)