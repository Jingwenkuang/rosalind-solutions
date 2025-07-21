def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

import itertools

#------------------Bruth force-------------
def scs(ss):
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
# ('ACGGTACGAGC', 'GAGCTTCGGA', 'GACACGG')
# ('ACGGTACGAGC', 'GACACGG', 'GAGCTTCGGA')
# ('GAGCTTCGGA', 'ACGGTACGAGC', 'GACACGG')
# ('GAGCTTCGGA', 'GACACGG', 'ACGGTACGAGC')
# ('GACACGG', 'ACGGTACGAGC', 'GAGCTTCGGA')
# ('GACACGG', 'GAGCTTCGGA', 'ACGGTACGAGC')
# 6 permutations
        sup = ssperm[0] #ssperm[0] = 'ACGGTACGAGC', get the first string in the permutation tuple.
        for i in range(len(ss) - 1):
            olen = overlap(ssperm[i], ssperm[i + 1], min_length = 1)
            print(i, sup)
            sup += ssperm[i + 1][olen:] #Add 'GAGCTTCGGA'[4:] → 'TTCGGA'
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

# print(scs(['ACGGTACGAGC', 'GAGCTTCGGA', 'GACACGG']))

#---------------Greedy---------------------
def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a, b in itertools.permutations(reads, 2):
        print('a', a, 'b', b)
        olen = overlap(a, b, min_length = k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen 
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

reads = ['ABC', 'BCA', 'CAB'] #'CABCA'
# reads = ['ABCD', 'CDBC', 'BCDA'] #CDBCABCDA
print(greedy_scs(reads, 2))

