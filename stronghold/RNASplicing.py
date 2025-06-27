# Import necessary modules from Biopython
from Bio import SeqIO
from Bio.Seq import Seq

# Step 1: Read sequences from the FASTA file
# Replace "your_input_file.fasta" with your actual file path
fasta_file = '/Users/xx/Downloads/rosalind_splc.txt'

# Use SeqIO to read all the sequences in the FASTA file
records = list(SeqIO.parse(fasta_file, "fasta"))

# Step 2: Extract the main DNA string (first sequence in the FASTA)
main_record = records[0]               # First FASTA entry is the full DNA string
main_dna_seq = str(main_record.seq)    # Convert Seq object to string

# Step 3: Extract the introns (all the remaining sequences)
introns = []                           # Initialize an empty list for introns

# Loop through the rest of the records to get intron sequences
for i in range(1, len(records)):
    intron_record = records[i]         # Get the i-th record
    intron_seq = str(intron_record.seq)  # Convert to string
    introns.append(intron_seq)         # Add to the list of introns

# Step 4: Remove all introns from the main DNA string
for intron in introns:
    if intron in main_dna_seq:
        main_dna_seq = main_dna_seq.replace(intron, "")  # Remove the intron

# Step 5: Transcribe the cleaned exon DNA to RNA
# DNA transcription: replace T with U
exon_seq = Seq(main_dna_seq)           # Convert string back to Seq object
mRNA_seq = exon_seq.transcribe()       # Transcribe to RNA (T -> U)

# Step 6: Translate the mRNA to a protein string
# Translation: convert RNA to amino acids using codon table
# to_stop=True tells it to stop at the first stop codon
protein_seq = mRNA_seq.translate(to_stop=True)

# Step 7: Print the final protein string
print(protein_seq)
