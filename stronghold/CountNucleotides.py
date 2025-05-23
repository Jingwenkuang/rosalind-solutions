# method 1
def count_nucleotides(dna):
    return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')

if __name__ == "__main__":
    dna = input("Enter DNA string: ").strip()
    a, c, g, t = count_nucleotides(dna)
    print(a, c, g, t)


dna = "CTAGCATATTCCAAGCATACCCTGTAGCAAACAGGTCGTCTCTCTACACCAACAAAGATTAGACTAGGTTGCAACACCGAGTCGACGGACTCCCGTAGTGCGCGGCAAGCCAAACGTGAGGTCAGATTACATGTCCAGGTAACCTTAAGCTACCGTCAGCGCACACCTTTCACTCGTACCCCAATACAGTCGCATATGAAGACCTCTGCCGTACCGTGTAGTCGTGGGAAAGCTGAAACCACGCGCATTCTTAGGACGTGAAACTTGCGTTCCAACGTTTTATACTTTTAGACGGGCCAGCGACACTCTATTACAGGGGGTTAGCCGTAGTTCGGCTCGCGGCCTGCGTGTTCATACATAAGAACGTAGTAAACGACCGTAATGGGTAGCTTATGGTTCTATTCGGGGCCGGGGAGTTTTCCTGACTAATATGGCTTCGGCGTAGCAGTCCACGCCGAACCCTTGTCAGATGCGGGCTGTGTTACCCAGGTGCGGGGTGTGGAGGACGCTGGATCTTTGCGTGAATTGGCCGACATACTTATTAACAGCGATGCTACACTATGGGTAGATCACACGAAGATACTGACTAGCCATAACTCCAGGCGGGAAACGAAACTACCATGATATACCGAATCCGCTATCCTAACACACTAGTTATGGGGATTGAGTTATAAGGTGATTAAACGTCAGGGGGCAAAACGCTATCTCTACTGATTCGTATACAACGCAAGCCACTATAAGCTGGGCGTAAGGTTACCCACACATGGTACAGGGC"

# method 2
def count_nucleotides(dna):
    counts = {'A': 0, 'T':0, 'C':0, 'G':0}
    for nucleotide in dna:
        counts[nucleotide] = counts[nucleotide] + 1
    return counts.values()

print(count_nucleotides(dna))