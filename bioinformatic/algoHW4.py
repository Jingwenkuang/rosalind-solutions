#-----------------------------1-----------------------------------------
def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

import itertools

def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup  # found shorter superstring
    return shortest_sup  # return shortest

# print(scs(['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']))
# strings = ['ABC', 'BCA', 'CAB']
strings = ['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']
#--------------------------------2---------------------------
def scs_list(ss):
    """ Returns all shortest common superstrings of given
        strings, which must be the same length """
    shortest_len = None
    scs_list = []
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss) - 1):
            olen = overlap(ssperm[i], ssperm[i + 1], min_length=1)
            sup += ssperm[i + 1][olen:]
        if shortest_len is None or len(sup) < shortest_len:
            shortest_len = len(sup)
            scs_list = [sup]
        elif len(sup) == shortest_len:
            scs_list.append(sup)
    # Remove duplicates
    unique_scs = list(set(scs_list))
    return unique_scs


print(scs(strings))
print(scs_list(strings))