def ExpectedDominantOffspring(couples):
# Couple	Probability that child has dominant phenotype
# AA-AA	100% → 1.0
# AA-Aa	100% → 1.0
# AA-aa	100% → 1.0
# Aa-Aa	75% → 0.75
# Aa-aa	50% → 0.5
# aa-aa	0% → 0.0

# couples = [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa]
    probs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    total = 0
    for c, p in zip(couples, probs):
        total += (2 * c * p)
    return total

couples = [17874, 16207, 18621, 17571, 17513, 17988]
print(ExpectedDominantOffspring(couples))
