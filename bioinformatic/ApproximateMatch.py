def naiveHamming(p, t, maxDistance):
    occurrences = []
    for i in xrange(len(t) - len(p) + 1):
        nmm = 0
        match = True
        for j in xrange(len(p)):
            if t[i + j] != p[j]:
                nmm += 1
                if nmm > maxDistance:
                    break
        if nmm <= maxDistance:
            occurrences.append(i)
    return occurrences