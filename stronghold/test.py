def GreedyMotifSearch(Dna, k, t):
    BestMotifs = [] #['GGC', 'AAG', 'CAA', 'CAC', 'CAA']
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        best_score = Score(BestMotifs)
    n = len(Dna[0])
    for i in range(n - k + 1):
        # Start with current k-mer from first sequence
        Motifs = [Dna[0][i:i+k]]
        
        # Build profile and find motifs in remaining sequences
        for j in range(1, t):
            P = Profile(Motifs[:j])  # Profile from first j motifs
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        
        # Check if current motifs are better
        current_score = Score(Motifs)
        if current_score < best_score:
            best_score = current_score
            BestMotifs = Motifs
    
    return BestMotifs

def Profile(motifs):
    """Build profile matrix from given motifs"""
    profile = {'A': [], 'C':[], 'G':[], 'T':[]}
    k = len(motifs[0]) #3
    t = len(motifs)    #5
    for i in range(k):
        counts = {'A':0, 'C':0, 'G':0, 'T':0}
        for motif in motifs:
            counts[motif[i]] += 1
        for nucleotide in ['A', 'C', 'G', 'T']:
            profile[nucleotide].append(counts[nucleotide]/t)
    return profile

def ProfileMostProbablePattern(Text, k, Profile):
    """Find most probable k-mer in Text based on Profile"""
    max_prob = -1
    most_probable = Text[:k]
    
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]
        prob = 1.0
        for j in range(k):
            nucleotide = kmer[j]
            prob *= Profile[nucleotide][j]
        
        if prob > max_prob:
            max_prob = prob
            most_probable = kmer
    
    return most_probable

def Score(motifs):
    """Calculate score as total mismatches from consensus"""
    consensus = GetConsensus(motifs)
    score = 0
    for motif in motifs:
        for i in range(len(motif)):
            if motif[i] != consensus[i]:
                score += 1
    return score

def GetConsensus(motifs):
    """Determine consensus string from motifs"""
    consensus = []
    k = len(motifs[0])
    for i in range(k):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            counts[motif[i]] += 1
        consensus.append(max(counts, key=counts.get))
    return ''.join(consensus)  
k = 3
t = 5
Dna = [
    "GGTGCTCAGGCA",
    "AAGAATCAGTCA",
    "CAAGGAGTTCGC",
    "CACGTCAATCAC",
    "CAATAATATTCG"
]
print(GreedyMotifSearch(Dna, k, t))

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def CountWithPseudocounts(Motifs):
    count = {symbol: [1] * len(Motifs[0]) for symbol in "ACGT"}
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4
    count = CountWithPseudocounts(Motifs)
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    for i in range(len(Motifs[0])):
        for nucleotide in ['A', 'C', 'G', 'T']:
            profile[nucleotide].append(count[nucleotide][i] / t)
    return profile

def ScoreWithPseudocounts(Motifs):
    consensus = ConsensusWithPseudocounts(Motifs)
    k = len(consensus)
    t = len(Motifs)
    score = 0
    for j in range(k):
        for i in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score

def ConsensusWithPseudocounts(Motifs):
    profile = ProfileWithPseudocounts(Motifs)
    consensus = ""
    k = len(Motifs[0])
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if profile[symbol][j] > m:
                m = profile[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def ProfileMostProbablePattern(Text, k, profile):
    max_prob = -1
    most_probable = ""
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        prob = 1
        for j in range(k):
            prob *= profile[pattern[j]][j]
        if prob > max_prob:
            max_prob = prob
            most_probable = pattern
    return most_probable

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [string[:k] for string in Dna]
    
    for i in range(len(Dna[0]) - k + 1):
        Motifs = [Dna[0][i:i+k]]
        
        for j in range(1, t):
            profile = ProfileWithPseudocounts(Motifs)
            motif = ProfileMostProbablePattern(Dna[j], k, profile)
            Motifs.append(motif)
        
        if ScoreWithPseudocounts(Motifs) < ScoreWithPseudocounts(BestMotifs):
            BestMotifs = Motifs
    
    return BestMotifs
# Sample Input:
# 3 5
# GGCGTTCAGGCA
# AAGAATCAGTCA
# CAAGGAGTTCGC
# CACGTCAATCAC
# CAATAATATTCG
# Sample Output:
# TTC
# ATC
# TTC
# ATC
# TTC
#######################################################