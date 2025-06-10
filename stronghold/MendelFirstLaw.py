def DominantPhenotypeProbability(k, m, n):
    total = k + m + n 
    subtotal = total - 1
    total_pairs = total * subtotal

    prob = 0
    prob += k * (k - 1)
    prob += 2 * k * m 
    prob += 2 * k * n
    prob += m * (m - 1) * 0.75
    prob += 2 * m * n * 0.5

    return round(prob / total_pairs, 5)

k = 15
m = 18
n = 29

    #           (kk, mm, nn)
    #         /       |      \
    #        2/6      2/6     2/6
    #     /  |  \   /  |  \    /  |  \
    #    k   m   n  k  m   n   k   m  n
    # 1/5  2/5 2/5 2/5 1/5 2/5 2/5 2/5 1/5 
AA x AA        k(k - 1)     100%
AA x Aa        2km          100%
AA x aa        2kn          100%
Aa x Aa        m(m - 1)      75%
Aa x aa        2mn           50%
aa x aa        n(n - 1)       0%
print(DominantPhenotypeProbability(k, m, n))