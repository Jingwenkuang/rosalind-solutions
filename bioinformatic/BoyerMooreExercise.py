import sys
sys.path.append("/Users/wendy/Downloads/") 
from bm_preproc import BoyerMoore

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                genome += line.rstrip()
    return genome
#---------------------------------1-------------------------
#How many alignments does the naive exact matching algorithm try when matching the string 

def naive_with_counts(p, t):
    occurrences = []
    num_alignments = 0
    num_char_comparisions = 0
    for i in range(len(t) - len(p) + 1):
        num_alignments += 1
        match = True
        for j in range(len(p)):
            num_char_comparisions += 1
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    # return occurrences, num_alignments, num_char_comparisions
    return num_alignments

genome_path = '/Users/wendy/Downloads/chr1.GRCh38.excerpt.fasta'
genome = readGenome(genome_path)
t = genome
p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
print(naive_with_counts(p, t))       #799954

#-------------------------------2------------------------------
def naive_with_counts(p, t):
    occurrences = []
    num_alignments = 0
    num_char_comparisions = 0
    for i in range(len(t) - len(p) + 1):
        num_alignments += 1
        match = True
        for j in range(len(p)):
            num_char_comparisions += 1
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    # return occurrences, num_alignments, num_char_comparisions
    return num_char_comparisions
print(naive_with_counts(p, t))

#-------------------------------3------------------------------
def boyer_moore_with_counts(p, p_bm, t):
    occurrences = []
    num_alignments = 0
    num_char_comparisions = 0
    i = 0
    while i < len(t) - len(p) + 1:
        num_alignments += 1
        shift = 1
        mismatched = False 
        for j in range(len(p) -1, -1, -1):
            num_char_comparisions += 1
            if p[j] != t[i + j]:
                skip_bc = p_bm.bad_character_rule(j, t[i + j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True 
                break
        if not mismatched: 
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
#     return occurrences, num_alignments, num_char_comparisions
    return num_alignments
p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
p_bm = BoyerMoore(p)
t = genome
print(boyer_moore_with_counts(p, p_bm, t)) #127974

#----------------------------------------4--------------------------------------------
import bisect
from kmer_index import Index

def query_index_2mm(p, index):
    """Find approximate matches with up to 2 mismatches using the pigeonhole principle."""
    k = index.k
    segment_length = k
    total_length = len(p)
    assert total_length == 24, "Pattern length must be 24"
    
    # Split the pattern into three segments
    segments = [
        (0, p[0:k]),
        (8, p[8:8+k]),
        (16, p[16:16+k])
    ]
    
    hits = set()
    
    for offset, segment in segments:
        # Query the index for the current segment
        segment_hits = index.query(segment)
        for hit in segment_hits:
            # Calculate the start position of the entire pattern in the text
            start_pos = hit - offset
            if start_pos < 0 or start_pos + total_length > len(index.index_text):
                continue  # pattern would run off the ends of the text
            # Extract the candidate from the text
            candidate = index.index_text[start_pos:start_pos+total_length]
            # Count mismatches
            mismatches = 0
            for a, b in zip(p, candidate):
                if a != b:
                    mismatches += 1
                    if mismatches > 2:
                        break
            if mismatches <= 2:
                hits.add(start_pos)
    
    return sorted(hits)

# Example usage (assuming the text and pattern are defined):
# First, we need to modify the Index class to store the original text for later access.
class Index(object):
    def __init__(self, t, k):
        ''' Create index from all substrings of size 'length' '''
        self.k = k  # k-mer length (k)
        self.index = []
        self.index_text = t  # Store the original text
        for i in range(len(t) - k + 1):  # for each k-mer
            self.index.append((t[i:i+k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize by k-mer
    
    def query(self, p):
        ''' Return index hits for first k-mer of P '''
        kmer = p[:self.k]  # query with first k-mer
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

def read_genome(filename):
    with open(filename, 'r') as f:
        genome = ''
        for line in f:
            if not line.startswith('>'):
                genome += line.rstrip()
    return genome

# Load the genome
genome_file = '/Users/wendy/Downloads/chr1.GRCh38.excerpt.fasta'  # Assuming the file is in the current directory
t = read_genome(genome_file)
pattern = 'GGCGCGGTGGCTCACGCCTGTAAT'

# Build the 8-mer index
index = Index(t, 8)

# Find approximate matches
matches = query_index_2mm(pattern, index)
print(len(matches))   #19

#-----------------------------------5--------------------------------
import bisect
from kmer_index import Index

def count_index_hits(p, index):
    """Count the total number of index hits for the given pattern segments."""
    k = index.k
    total_length = len(p)
    assert total_length == 24, "Pattern length must be 24"
    
    # Split the pattern into three 8-base segments
    segments = [
        p[0:k],
        p[8:8+k],
        p[16:16+k]
    ]
    
    total_hits = 0
    
    for segment in segments:
        # Query the index for the current segment
        segment_hits = index.query(segment)
        total_hits += len(segment_hits)
    
    return total_hits

def read_genome(filename):
    with open(filename, 'r') as f:
        genome = ''
        for line in f:
            if not line.startswith('>'):
                genome += line.rstrip()
    return genome

# Load the genome
genome_file = '/Users/wendy/Downloads/chr1.GRCh38.excerpt.fasta'  # Assuming the file is in the current directory
t = read_genome(genome_file)
pattern = 'GGCGCGGTGGCTCACGCCTGTAAT'

# Build the 8-mer index
index = Index(t, 8)

# Count total index hits
total_hits = count_index_hits(pattern, index)
print(total_hits)         #90

#-------------------------------------6-------------------------------------------
import bisect
   
class SubseqIndex(object):
    """ Holds a subsequence index for a text T """
    
    def __init__(self, t, k, ival):
        """ Create index from all subsequences consisting of k characters
            spaced ival positions apart.  E.g., SubseqIndex("ATAT", 2, 2)
            extracts ("AA", 0) and ("TT", 1). """
        self.k = k  # num characters per subsequence extracted
        self.ival = ival  # space between them; 1=adjacent, 2=every other, etc
        self.index = []
        self.span = 1 + ival * (k - 1)
        for i in range(len(t) - self.span + 1):  # for each subseq
            self.index.append((t[i:i+self.span:ival], i))  # add (subseq, offset)
        self.index.sort()  # alphabetize by subseq
    
    def query(self, p):
        """ Return index hits for first subseq of p """
        subseq = p[:self.span:self.ival]  # query with first subseq
        i = bisect.bisect_left(self.index, (subseq, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != subseq:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits
    
genome_file = '/Users/wendy/Downloads/chr1.GRCh38.excerpt.fasta'  # Assuming the file is in the current directory
t = read_genome(genome_file)
p = 'GGCGCGGTGGCTCACGCCTGTAAT'

subseq_ind = SubseqIndex(t, 8, 3)
num_index_hits = query_subseq(p, t, subseq_ind)
print(num_index_hits)