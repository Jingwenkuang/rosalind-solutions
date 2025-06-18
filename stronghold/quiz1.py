#-1-------------------------------------------
# Please run the following data set in the program(s) that you have written: 
# dna2.fasta
# If you created your program(s) correctly, you will be able to answer the questions below.
# How many records are in the multi-FASTA file?
print('--------1------------------------------18')
from Bio import SeqIO

fasta_file = "/Users/wendy/Desktop/dna2.fasta"  # Replace with your actual file name

count = 0
for record in SeqIO.parse(fasta_file, "fasta"):
    count += 1

print(f"Number of records in the FASTA file: {count}")

#-2-------------------------------------------
#What is the length of the longest sequence in the file?
print('--------2------------------------------4894')
from Bio import SeqIO

filename = "/Users/wendy/Desktop/dna2.fasta"  # Replace with your actual file path
max_length = 0
longest_seq_id = ""

for record in SeqIO.parse(filename, "fasta"):
    seq_length = len(record.seq)
    if seq_length > max_length:
        max_length = seq_length
        longest_seq_id = record.id

print(f"Longest sequence ID: {longest_seq_id}")
print(f"Length of longest sequence: {max_length} bp")
#-3-------------------------------------------
# Question 3
# What is the length of the shortest sequence in the file?
print('--------3------------------------------115')
from Bio import SeqIO

filename = "/Users/wendy/Desktop/dna2.fasta"  # Replace with your file path
min_length = float('inf')  # Initialize with a large number
shortest_seq_id = ""

for record in SeqIO.parse(filename, "fasta"):
    seq_length = len(record.seq)
    if seq_length < min_length:
        min_length = seq_length
        shortest_seq_id = record.id

print(f"Shortest sequence ID: {shortest_seq_id}")
print(f"Length of shortest sequence: {min_length} bp")
#-4-------------------------------------------
#What is the length of the longest ORF appearing in reading frame 2 of any of the sequences?
print('--------4------------------------------1458')
from Bio import SeqIO

def find_longest_orf(sequence, frame):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    max_orf_length = 0
    sequence = str(sequence.seq).upper()
    # Adjust for frame (frame 2 starts at index 1)
    subseq = sequence[frame-1:]
    for i in range(0, len(subseq) - 2, 3):
        codon = subseq[i:i+3]
        if codon == start_codon:
            for j in range(i+3, len(subseq) - 2, 3):
                stop_codon = subseq[j:j+3]
                if stop_codon in stop_codons:
                    orf_length = j + 3 - i  # +3 to include stop codon
                    if orf_length > max_orf_length:
                        max_orf_length = orf_length
                    break  # Stop at first in-frame stop codon
    return max_orf_length

filename = "/Users/wendy/Desktop/dna2.fasta"
max_orf_frame2 = 0
best_record = None

for record in SeqIO.parse(filename, "fasta"):
    orf_length = find_longest_orf(record, frame=2)
    if orf_length > max_orf_frame2:
        max_orf_frame2 = orf_length
        best_record = record.id

print(f"Longest ORF in frame 2: {max_orf_frame2} bp")
print(f"Sequence ID: {best_record}")
#-5-------------------------------------------
# What is the starting position of the longest ORF in reading frame 3 in any of the sequences? The position should indicate the character number where the ORF begins. For instance, the following ORF:
# > sequence1
# ATGCCCTAG
# starts at position 1.
print('--------5------------------------------636')
from Bio import SeqIO

def find_longest_orf_frame3(record):
    sequence = str(record.seq).upper()
    max_orf_length = 0
    start_pos = 0
    # Frame 3 starts at index 2 (0-based)
    for i in range(2, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon == "ATG":
            for j in range(i+3, len(sequence) - 2, 3):
                stop_codon = sequence[j:j+3]
                if stop_codon in ["TAA", "TAG", "TGA"]:
                    orf_length = j + 3 - i  # Include stop codon
                    if orf_length > max_orf_length:
                        max_orf_length = orf_length
                        start_pos = i + 1  # Convert to 1-based
                    break  # Stop at first in-frame stop
    return max_orf_length, start_pos

filename = "/Users/wendy/Desktop/dna2.fasta"
max_orf_len = 0
best_start = 0
best_record = None

for record in SeqIO.parse(filename, "fasta"):
    orf_len, start = find_longest_orf_frame3(record)
    if orf_len > max_orf_len:
        max_orf_len = orf_len
        best_start = start
        best_record = record.id

print(f"Longest ORF in frame 3: {max_orf_len} bp")
print(f"Starts at position: {best_start}")
print(f"Sequence ID: {best_record}")
#-6-------------------------------------------
# What is the length of the longest ORF appearing in any sequence and in any forward reading frame?
# from Bio import SeqIO
print('--------6------------------------------2394')
def find_longest_orf_any_frame(record):
    sequence = str(record.seq).upper()
    max_orf_length = 0
    for frame in [0, 1, 2]:  # Frames 1, 2, 3 (0-based)
        for i in range(frame, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if codon == "ATG":
                for j in range(i+3, len(sequence) - 2, 3):
                    stop_codon = sequence[j:j+3]
                    if stop_codon in ["TAA", "TAG", "TGA"]:
                        orf_length = j + 3 - i  # Include stop codon
                        if orf_length > max_orf_length:
                            max_orf_length = orf_length
                        break  # Stop at first in-frame stop
    return max_orf_length

filename = "/Users/wendy/Desktop/dna2.fasta"
global_max_orf = 0
best_record = None

for record in SeqIO.parse(filename, "fasta"):
    current_max = find_longest_orf_any_frame(record)
    if current_max > global_max_orf:
        global_max_orf = current_max
        best_record = record.id

print(f"Longest ORF (any frame): {global_max_orf} bp")
print(f"Sequence ID: {best_record}")
#-7-------------------------------------------
# Question 7
# What is the length of the longest forward ORF that appears in the sequence with the identifier  gi|142022655|gb|EQ086233.1|16?
print('--------7------------------------------1644')
from Bio import SeqIO

def find_longest_orf_in_sequence(sequence_id, filename):
    for record in SeqIO.parse(filename, "fasta"):
        if sequence_id in record.id:
            sequence = str(record.seq).upper()
            max_orf_length = 0
            for frame in [0, 1, 2]:  # Frames 1, 2, 3 (0-based)
                for i in range(frame, len(sequence) - 2, 3):
                    if sequence[i:i+3] == "ATG":
                        for j in range(i+3, len(sequence) - 2, 3):
                            stop_codon = sequence[j:j+3]
                            if stop_codon in ["TAA", "TAG", "TGA"]:
                                orf_length = j + 3 - i  # Include stop codon
                                if orf_length > max_orf_length:
                                    max_orf_length = orf_length
                                break  # Stop at first in-frame stop
            return max_orf_length
    return None

filename = "/Users/wendy/Desktop/dna2.fasta"
sequence_id = "gi|142022655|gb|EQ086233.1|16"
longest_orf = find_longest_orf_in_sequence(sequence_id, filename)

print(f"Longest ORF in {sequence_id}: {longest_orf} bp")
#-8-------------------------------------------
#Find the most frequently occurring repeat of length 6 in all sequences. How many times does it occur in all?
print('--------8------------------------------153')
from Bio import SeqIO
from collections import defaultdict

def find_most_frequent_6mer(filename):
    kmer_counts = defaultdict(int)
    for record in SeqIO.parse(filename, "fasta"):
        sequence = str(record.seq).upper()
        for i in range(len(sequence) - 5):
            kmer = sequence[i:i+6]
            kmer_counts[kmer] += 1
    most_frequent = max(kmer_counts.items(), key=lambda x: x[1])
    return most_frequent

filename = "/Users/wendy/Desktop/dna2.fasta"
repeat_6mer, count = find_most_frequent_6mer(filename)
print(f"Most frequent 6-mer: {repeat_6mer} (occurs {count} times)")
#-9-------------------------------------------
# Question 9
# Find all repeats of length 12 in the input file. 
# Let's use Max to specify the number of copies
# of the most frequent repeat of length 12.  How many different 12-base sequences 
# occur Max times?
print('--------9------------------------------4')
from Bio import SeqIO
from collections import defaultdict

def find_top_12mers(filename):
    kmer_counts = defaultdict(int)
    for record in SeqIO.parse(filename, "fasta"):
        sequence = str(record.seq).upper()
        for i in range(len(sequence) - 11):
            kmer = sequence[i:i+12]
            kmer_counts[kmer] += 1
    
    max_count = max(kmer_counts.values())
    top_12mers = [kmer for kmer, count in kmer_counts.items() if count == max_count]
    return max_count, top_12mers

filename = "/Users/wendy/Desktop/dna2.fasta"
max_occurrences, top_12mers = find_top_12mers(filename)

print(f"Max occurrences of any 12-mer: {max_occurrences}")
print(f"Number of 12-mers with Max count: {len(top_12mers)}")
print(f"These 12-mers: {', '.join(top_12mers)}")
#-10-------------------------------------------
# Question 10
# Which one of the following repeats of length 7 has a maximum number of occurrences?
print('--------10------------------------------CGCGCCG')
from Bio import SeqIO
from collections import defaultdict

def find_top_7mer(filename):
    kmer_counts = defaultdict(int)
    for record in SeqIO.parse(filename, "fasta"):
        sequence = str(record.seq).upper()
        for i in range(len(sequence) - 6):
            kmer = sequence[i:i+7]
            kmer_counts[kmer] += 1
    max_count = max(kmer_counts.values())
    top_7mer = [kmer for kmer, count in kmer_counts.items() if count == max_count]
    return top_7mer[0], max_count

filename = "/Users/wendy/Desktop/dna2.fasta"
top_7mer, count = find_top_7mer(filename)
print(f"Most frequent 7-mer: {top_7mer} (occurs {count} times)")