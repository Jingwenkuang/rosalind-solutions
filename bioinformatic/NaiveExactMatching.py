# implementation of the naive exact matching algorithm:
def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

# # function that takes a DNA string and returns its reverse complement:
def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

# # function that parses a DNA reference genome from a file in the FASTA format.
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


# # function that parses the read and quality strings from a FASTQ file containing sequencing reads.
# def readFastq(filename):
#     sequences = []
#     qualities = []
#     with open(filename) as fh:
#         while True:
#             fh.readline()  # skip name line
#             seq = fh.readline().rstrip()  # read base sequence
#             fh.readline()  # skip placeholder line
#             qual = fh.readline().rstrip() # base quality line
#             if len(seq) == 0:
#                 break
#             sequences.append(seq)
#             qualities.append(qual)
#     return sequences, qualities
# filename = '/Users/xx/Desktop/lambda_virus.fa'
# print(readGenome(filename))

print('--------1-----------------')
from Bio import SeqIO

# Load the genome file
filename = '/Users/xx/Desktop/lambda_virus.fa'
record = SeqIO.read(filename, "fasta")
sequence = str(record.seq)

# Count both 'AGGT' and its reverse complement 'ACCT'
count_aggt = sequence.count("AGGT")
count_acct = sequence.count("ACCT")

# Total count
total = count_aggt + count_acct

print("AGGT count:", count_aggt)
print("ACCT count:", count_acct)
print("Total count:", total)

print('--------2-----------------')

rec = SeqIO.read(filename, "fasta")
seq = str(rec.seq)

count_ttaa = seq.count("TTAA")
print("TTAA count:", count_ttaa)

print('--------4-----------------')
#Question 4
# What is the offset of the leftmost occurrence of AGTCGA or its reverse complement in the Lambda virus genome?

print('--------5-----------------')
def naive_2mm(P, T): #2 mismatch
    occurrences = []
    len_P = len(P)
    len_T = len(T)
    for i in range(len_T - len_P + 1):
        mismatch = 0
        for j in range(len_P):
            if T[i + j] != P[j]:
                mismatch += 1
                if mismatch > 2:
                    break
        if mismatch <= 2:
            occurrences.append(i)
    return occurrences
lambda_virus_genome = readGenome('/Users/xx/Desktop/lambda_virus.fa')
occurrences = naive_2mm('TTCAAGCC', lambda_virus_genome)
print(len(occurrences))