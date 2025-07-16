from itertools import permutations
#list(permutations([1, 2, 3], 3))
#[(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        # b = 'CGT', finds the starting at index 3
        # start = 3
        print('start', start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            # a[start:] = a[3:] = 'CGT'
            return len(a) - start
        start += 1

def naive_overlap_map(reads, k):
    olaps = {}
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > 0:
            olaps[(a, b)] = olen
    return olaps

reads = ['ACGGATGATC', 'GATCAAGT', 'TTCACGGA']
print(naive_overlap_map(reads, 3))
#{('ACGGATGATC', 'GATCAAGT'): 4, ('TTCACGGA', 'ACGGATGATC'): 5}

#All permutaions of (a, b)
# (ACGGATGATC, GATCAAGT) → overlap = 5  (GATC)
# (GATCAAGT, ACGGATGATC) → 0
# (ACGGATGATC, TTCACGGA) → 0
# (TTCACGGA, ACGGATGATC) → overlap = 4  (ACGG)
# (GATCAAGT, TTCACGGA) → 0
# (TTCACGGA, GATCAAGT) → 0