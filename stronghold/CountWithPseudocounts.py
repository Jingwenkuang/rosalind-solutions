def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    for symbol in 'ACGT':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# {'A': [2, 3, 2, 1, 1, 3], 'C': [3, 2, 5, 3, 1, 1], 'G': [2, 2, 1, 3, 2, 2], 'T': [2, 2, 1, 2, 5, 3]}
Motifs = ['AACGTA', 'CCCGTT','CACCTT','GGATTA','TTCCGG']
print(CountWithPseudocounts(Motifs))

#######################################
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = CountWithPseudocounts(Motifs)
        
    for symbol in "ACGT":
        profile[symbol] = []
        for i in range(k):
            fre = count[symbol][i] / (t + 4)
            profile[symbol].append(fre)
    return profile
print(ProfileWithPseudocounts(Motifs))