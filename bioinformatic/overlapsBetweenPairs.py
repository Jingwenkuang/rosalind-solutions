#The overlap function finds the maximum overlap between the suffix of string a and the prefix of string b, requiring at least min_length characters of overlap.
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

a = 'TTACGT'
b = 'CGTACCGT'
print(overlap(a, b, min_length=3))