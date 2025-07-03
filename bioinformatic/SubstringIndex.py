import bisect
import sys

class Index(object):
    def __init__(self, t, k):
        ''' Create index from all substrings of size 'length' '''
        self.k = k  # k-mer length (k)
        self.index = []
        for i in range(len(t) - k + 1):  # for each k-mer
            self.index.append((t[i:i+k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize by k-mer
# [('AATC', 12), ('ACGA', 3), ('AGAA', 10), ('ATCT', 6), ('ATCT', 13), ('CGAT', 4), 
# ('CGTA', 0), ('CTAG', 8), ('GAAT', 11), ('GATC', 5), ('GTAC', 1), ('TACG', 2), 
# ('TAGA', 9), ('TCTA', 7), ('TCTA', 14)]

    def query(self, p):
        ''' Return index hits for first k-mer of P '''

        kmer = p[:self.k]  # query with first k-mer
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary search  # i = 13
        # -1 means all the indices in the list are greater than negetive one
        # always get the first occurrence of that.
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

def queryIndex(p, t, index):
    k = index.k
    offsets = []
    for i in index.query(p):  #[7, 14] return all the possible hits
        if p[k:] == t[i+k:i+len(p)]:  # verify that rest of P matches
        # p[4:] == t[7+4:7+4]   
        # '' == '' , True
            offsets.append(i)
    return offsets

t = 'CGTACGATCTAGAATCTA'
p = 'TCTA'

index = Index(t, 4)
print(queryIndex(p, t, index))