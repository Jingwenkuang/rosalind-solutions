def MortalFib(n, m):
    # n : alive for n month
    # m : dies after m month
    ages = [1] + [0] * (m - 1) # 1 pair of age 0, others 0
    for month in range(1, n):
        new_borns = sum(ages[1:]) # rabbis of age >= reproduce
        ages = [new_borns] + ages[:-1] # age everyone, remove the last one(oldest)
    return sum(ages)

n, m = 6, 3
print(MortalFib(n, m))