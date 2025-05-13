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