# def SkewArray(Genome):
#     # your code here
#     skew = [0] 
#     n = len(Genome)
#     for i in range(n):
#         if Genome[i] == "C":
#             skew.append(skew[i] - 1)
#         elif Genome[i] == "G":
#             skew.append(skew[i] + 1)
#         else:
#             skew.append(skew[i])
#     return skew

# Genome = "GATACACTTCCCGAGTAGGTACTG"
# print(SkewArray(Genome))

def HammingDistance(p, q):
    dist = 0
    for i in range(len(p)):
        if not p[i] == q[i]:
            dist += 1
    return dist

p = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
q = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"
print(HammingDistance(p, q))
