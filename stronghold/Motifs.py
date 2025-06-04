# Input:  A set of kmers Motifs
# Output: Count(Motifs)
#method 1
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0]) if Motifs else 0
    for symbol in "ACGT":
        count[symbol] = [0] * k      # {A: [0,0,0,0,0,0]}
    for motif in Motifs:             # loop thr each sequence
        for i in range(len(Motifs[0])): # loop thr each position in the seq
            symbol = motif[i]        # get nucleotide at current position
            count[symbol][i] += 1    # increment count for this nucleotide at this position
    return count
# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# {'A': [1, 2, 1, 0, 0, 2], 'C': [2, 1, 4, 2, 0, 0], 'G': [1, 1, 0, 2, 1, 1], 'T': [1, 1, 0, 1, 4, 2]}
#method 2
def Count(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

Motifs = [
    "AACGTA",
    "CCCGTT",
    "CACCTT",
    "GGATTA",
    "TTCCGG"
]
print(Count(Motifs))

###########################################
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = Count(Motifs)
    for symbol in "ACGT":
        profile[symbol] = []
        for i in range(k):
            fre = count[symbol][i] / t
            profile[symbol].append(fre)

    # insert your code here
    return profile

def Count(Motifs):
    count = {}
    for symbol in "ACGT":
        count[symbol] = [0] * len(Motifs[0])
    for motif in Motifs:
        for i in range(len(Motifs[0])):
            symbol = motif[i]
            count[symbol][i] += 1
    return count
# Sample Input:

# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:

# {'A': [0.2, 0.4, 0.2, 0.0, 0.0, 0.4], 
# 'C': [0.4, 0.2, 0.8, 0.4, 0.0, 0.0], 
# 'G': [0.2, 0.2, 0.0, 0.4, 0.2, 0.2], 
# 'T': [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]}
###########################################
# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Count(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    count ={}
    for symbol in "ACGT":
        count[symbol] = [0] * k
    for motif in Motifs: 
        for i in range(t):
            symbol = motif[i]
            count[symbol][i] += 1
    return count
# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# CACCTA
###########################################
def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
# Copy your Count(Motifs) function here.
def Count(Motifs):
    count = {}
    for symbol in "ACGT":
        count[symbol] = [0] * len(Motifs[0])
    for motif in Motifs:
        for i in range(len(Motifs[0])):
            symbol = motif[i]
            count[symbol][i] += 1
    return count
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    if not Motifs:
        return 0
    consensus = Consensus(Motifs)
    score = 0
    for motif in Motifs:
        for i in range(len(Motifs[0])):
            if motif[i] != consensus[i]:
                score += 1
    return score
# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
#14
###########################################
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        symbol = Text[i]
        p *= Profile[symbol][i]
    return p

Profile = {
    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}

Text = "ACGGGGATTACC"
print(Pr(Text, Profile))  # Output: 0.000839808
# Sample Input:

# ACGGGGATTACC
# 0.2 0.2 0.0 0.0 0.0 0.0 0.9 0.1 0.1 0.1 0.3 0.0
# 0.1 0.6 0.0 0.0 0.0 0.0 0.0 0.4 0.1 0.2 0.4 0.6
# 0.0 0.0 1.0 1.0 0.9 0.9 0.1 0.0 0.0 0.0 0.0 0.0
# 0.7 0.2 0.0 0.0 0.1 0.1 0.0 0.5 0.8 0.7 0.3 0.4
# Sample Output:

# 0.0008398080000000002
###########################################
# Insert your Pr(text, profile) function here from Motifs.py.

# Write your ProfileMostProbableKmer() function here.
# The profile matrix assumes that the first row corresponds to A, the second corresponds to C,
# the third corresponds to G, and the fourth corresponds to T.
# You should represent the profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats
def ProfileMostProbableKmer(text, k, profile):
    max_prob = -1 # ensure any computed probability will be higher initially
    most_probable_kmer = ""
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = Pr(kmer, profile)
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    return most_probable_kmer
def Pr(text, profile):
    p = 1
    for i in range(len(text)):
        symbol = text[i]
        p *= profile[symbol][i]
    return p
# Sample Input:
# ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
# 5
# 0.2 0.2 0.3 0.2 0.3
# 0.4 0.3 0.1 0.5 0.1
# 0.3 0.3 0.5 0.2 0.4
# 0.1 0.2 0.1 0.1 0.2
# Sample Output:

# CCGAG
###########################################
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    # Initialize BestMotifs with first k-mer from each sequence
    BestMotifs = [Dna[i][0:k] for i in range(t)] #['GGC', 'AAG', 'CAA', 'CAC', 'CAA']
    best_score = Score(BestMotifs)
    
    n = len(Dna[0])
    for i in range(n - k + 1):
        # Start with current k-mer from first sequence
        Motifs = [Dna[0][i:i+k]] #[GGC
        # GCG, CGT, GTT, TTA, TCA, CAG, AGG, GGC, GCA]
        print('BestMotifs', BestMotifs)
        # Build profile and find motifs in remaining sequences
        for j in range(1, t):
            P = Profile(Motifs[:j])  #Motifs = ['GGC']
            print(Motitf[:j])
            print(j)                 #1
            print(P)                 #{'A':[0.0, 0.0, 0.0], 'C':[0.0, 0.0, 1.0],'G':[1.0, 1.0, 0.0],'C':[0.0, 0.0, 0.0]}
            print('---------')
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            print('second', Motifs)
       
        # Check if current motifs are better
        current_score = Score(Motifs)
        print('best_score', best_score)
        if current_score < best_score:
            best_score = current_score
            BestMotifs = Motifs
    
    return BestMotifs

def Profile(motifs):
    """Build profile matrix from given motifs"""
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    k = len(motifs[0])
    t = len(motifs)
    
    for i in range(k):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            counts[motif[i]] += 1
        for nucleotide in ['A', 'C', 'G', 'T']:
            profile[nucleotide].append(counts[nucleotide] / t)
    
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

# Dna = [
#     "GGCGTTCAGGCA",
#     "AAGAATCAGTCA",
#     "CAAGGAGTTCGC",
#     "CACGTCAATCAC",
#     "CAATAATATTCG"
# ]
#method 2
def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    n = len(Dna[0])
    best_motifs = [Dna[i][0:k] for i in range(t)]

    for i in range(n - k + 1):
        motifs = [Dna[0][i:i+k]]
        for j in range(1, t):
            profile = Profile(motifs[0:j])
            motifs.append(ProfileMostProbableKmer(Dna[j], k, profile))

        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
    return best_motifs

def Score(Motifs):
    consensus = Consensus(Motifs)
    k = len(consensus)
    t = len(Motifs)
    score = 0
    for j in range(k):
        for i in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    count = Count(Motifs)
    profile = {}
    k = len(Motifs[0])
    t = len(Motifs)    
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(count[symbol][j] / t)
    return profile

def Consensus(Motifs):
    profile = Profile(Motifs)
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

def ProfileMostProbableKmer(Text, k, Profile):
    max_prob = -1
    most_probable = ""

    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        prob = Pr(pattern, Profile)
        if prob > max_prob:
            max_prob = prob
            most_probable = pattern
    return most_probable

def Pr(Text, Profile):
    p = 1.0

    for i in range(len(Text)):
        symbol = Text[i]
        column = i
        p *= Profile[symbol][column]
    return p
#########################################
#method 1
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
#method 2
# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    counts = {'A': [1] * k, 'C': [1] * k, 'G': [1] * k, 'T': [1] * k}
    
    # Iterate through each position in the motifs
    for i in range(k):
        for motif in Motifs:
            counts[motif[i]][i] += 1
    return counts
##########################################################################
    # Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
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

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
# HINT:   You need to use CountWithPseudocounts as a subroutine of ProfileWithPseudocounts
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
#Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# {'A': [0.2222222222222222, 0.3333333333333333, 
# 0.2222222222222222, 0.1111111111111111, 0.1111111111111111, 
# 0.3333333333333333], 'C': [0.3333333333333333, 0.2222222222222222,
#  0.5555555555555556, 0.3333333333333333, 0.1111111111111111, 
#  0.1111111111111111], 'G': [0.2222222222222222, 0.2222222222222222, 
#  0.1111111111111111, 0.3333333333333333, 0.2222222222222222, 
#  0.2222222222222222], 'T': [0.2222222222222222, 0.2222222222222222, 
#  0.1111111111111111, 0.2222222222222222, 0.5555555555555556, 
#  0.3333333333333333]}

##################################################################################
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

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    k = len(Profile["A"])
    most_probable_kmers = []
    for text in Dna:
        most_probable = ProfileMostProbablePattern(text, k, Profile)
        most_probable_kmers.append(most_probable)
    return most_probable_kmers

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
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
# Sample Input:
# 0.8 0.0 0.0 0.2
# 0.0 0.6 0.2 0.0
# 0.2 0.2 0.8 0.0
# 0.0 0.2 0.0 0.8
# TTACCTTAAC
# GATGTCTGTC
# ACGGCGTTAG
# CCCTAACGAG
# CGTCAGAGGT
# Sample Output:
# ACCT
# ATGT
# GCGT
# ACGA
# AGGT
#######################################################
import random
# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    random_motifs = []
    t = len(Dna)
    l = len(Dna[0])
    for i in range(t):
        ran_num = random.randint(0,l-k)
        random_motifs.append(Dna[i][ran_num:ran_num+k])
    return random_motifs
# Sample Input:
# 3 5
# TTACCTTAAC
# GATGTCTGTC
# ACGGCGTTAG
# CCCTAACGAG
# CGTCAGAGGT
# Sample Output:
# ACC
# GAT
# TAG
# TAA
# AGA

#######################################################
import random
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    
    while True:
        #create profile from current motifs
        profile = ProfileWithPseudocounts(M)
        #generate new motifs based on profile
        M = Motifs(profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 
        
# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
def RandomMotifs(Dna, k, t):
    random_motifs = []
    t = len(Dna)
    l = len(Dna[0])
    for i in range(t):
        ran_num = random.randint(0,l-k)
        random_motifs.append(Dna[i][ran_num:ran_num+k])
    return random_motifs

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    count = CountWithPseudocounts(Motifs)
    profile = {'A':[], 'C':[], 'G':[], 'T':[]}
    for i in range(len(Motifs[0])):
        for nucleotide in ['A', 'C', 'G', 'T']:
            profile[nucleotide].append(count[nucleotide][i]/(t + 4))
    return profile

def CountWithPseudocounts(Motifs):
    count = {symbol: [1]*len(Motifs[0]) for symbol in 'ACGT'}
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Motifs(Profile, Dna):
    k = len(Profile["A"])
    most_probable_kmers = []
    for text in Dna:
        most_probable = ProfileMostProbablePattern(text, k, Profile)
        most_probable_kmers.append(most_probable)
    return most_probable_kmers

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

def Score(Motifs):
    consensus = Consensus(Motifs)
    k = len(consensus)
    t = len(Motifs)
    score = 0
    for j in range(k):
        for i in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score

def Consensus(Motifs):
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
#     sample input
#     Dna = [
#     "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
#     "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
#     "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
#     "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
#     "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
# ]
# k = 8
# t = 5
# Sample Output:
# TCTCGGGG
# CCAAGGTG
# TACAGGCG
# TTCAGGTG
# TCCACGTG
#######################################################
def Normalize(Probabilities):
    sum_of_values=sum(Probabilities.values())
    normal={}
    for symbol in Probabilities:
        normal[symbol]=Probabilities[symbol]/sum_of_values
    return normal
# Sample Input:
# {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
# Sample Output:
# {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}

#######################################################
import random
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    p = random.uniform(0, 1)
    for kmer, probability in Probabilities.items():
        p -= probability
        if p <= 0:
            return kmer
# Sample Input:
# 0.25 A
# 0.25 C
# 0.25 G
# 0.25 T
# Sample Output:
# A
#######################################################
import random
# then, copy Pr, Normalize, and WeightedDie below this line
def Pr(kmer, profile):
    prob = 1.0
    for i, nucleotide in enumerate(kmer):
        prob *= profile[nucleotide][i]
    return prob

def Normalize(Probabilities):
    sum_of_values=sum(Probabilities.values())
    normal={}
    for symbol in Probabilities:
        normal[symbol]=Probabilities[symbol]/sum_of_values
    return normal

def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    p = random.uniform(0, 1)
    for kmer, probability in Probabilities.items():
        p -= probability
        if p <= 0:
            return kmer
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0, n - k + 1):
        kmer = Text[i:i+k]
        probabilities[kmer] = Pr(kmer, profile)
    probabilities = Normalize(probabilities)  # Normalize the probabilities
    return WeightedDie(probabilities)
# Sample Input:
# AAACCCAAACCC
# {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
# 2
# Sample Output:
# AA
#######################################################
import random
# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    Motifs=RandomMotifs(Dna, k, t)
    BestMotifs=Motifs
    for j in range(N):
        i=random.randint(1,t)
        text=Motifs.pop(i-1)
        profile=ProfileWithPseudocounts(Motifs)
        kmer=ProfileMostProbableKmer(text, k, profile)
        Motifs.insert(i-1,kmer)
        if Score(Motifs)<Score(BestMotifs):
            BestMotifs=Motifs
    return BestMotifs

def RandomMotifs(Dna, k, t):
    Motifs=[]
    n=len(Dna[0])
    for i in range(t):
        start_index=random.randint(0,n-k)
        random_kmer=Dna[i][start_index:start_index+k]
        Motifs.append(random_kmer)
    return Motifs

def CountWithPseudocounts(Motifs):
    count = {}
    k=len(Motifs[0])
    for i in "ACGT":
        count[i]=[]
        for j in range(k):
            count[i].append(0)
    for i in range(len(Motifs)):
        for j in range(k) :
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    for i in 'ACGT':
        for j in range(k):
            count[i][j]+=1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile=CountWithPseudocounts(Motifs)
    n=0
    for i in "ACGT":
        n=n+profile[i][0]
    for i in "ACGT":
        for j in range(k):           
            profile[i][j]=profile[i][j]/n   
    return profile

def Consensus(Motifs):
    consensus = ""
    k=len(Motifs[0])
    dic=CountWithPseudocounts(Motifs)
    for j in range(k):
        m=-1
        for i in 'ACGT':                    
            if dic[i][j]>m:
                m=dic[i][j]
                most_frequent_symbol=i
        consensus=consensus+most_frequent_symbol
    return consensus

def Score(Motifs):
    k=len(Motifs[0])
    t=len(Motifs)
    benchmark=Consensus(Motifs)
    score=0
    for j in range(k):  
        for i in range(t):
            if Motifs[i][j]!=benchmark[j]:
                score+=1
    return score

def Pr(String, Profile):
    product=1
    j=0
    for i in String:
        product=product*(Profile[i][j])
        j+=1
    return product

def ProfileMostProbableKmer(text, k, profile):
    n=len(text)
    m=-1
    target=''
    for i in range(n-k+1):
        string=text[i:i+k]
        pr=Pr(string,profile)        
        if pr>m:
            target=string
            m=pr
    return target
# Sample Input:
# 8 5 100
# CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
# GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
# TAGTACCGAGACCGAAAGAAGTATACAGGCGT
# TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
# AATCCACCAGCTCCACGTGCAATGTTGGCCTA
# Sample Output:
# TCTCGGGG
# CCAAGGTG
# TACAGGCG
# TTCAGGTG
# TCCACGTG
