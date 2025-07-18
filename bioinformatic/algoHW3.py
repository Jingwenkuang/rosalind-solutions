# Download and process
import requests
url = "https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/chr1.GRCh38.excerpt.fasta"
response = requests.get(url)
with open("chr1_excerpt.fasta", "wb") as f:
    f.write(response.content)

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                genome += line.rstrip()
    return genome

# Run the analysis
genome = readGenome("chr1_excerpt.fasta")
pattern = "GATTTACCAGATTGAG"  # example pattern
# edit_dist = approximate_match(pattern, genome)


def approximate_match_edit_distance(p, t):
    # Create distance matrix
    D = []
    for i in range(len(p)+1):
        D.append([0]*(len(t)+1))
    # Initialize first column of matrix
    for i in range(len(p)+1):
        D[i][0] = i
    # Initialize first row to 0 (different from standard edit distance)
    for j in range(len(t)+1):
        D[0][j] = 0

    # Fill in the rest of the matrix
    for i in range(1, len(p)+1):
        for j in range(1, len(t)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if p[i-1] == t[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    # The edit distance is the minimum value in the bottom row
    return min(D[-1][j] for j in range(len(t)+1))

# p = 'GCGTATGC'
# t = 'TATTGGCTATACGGTT'
print(approximate_match_edit_distance(pattern, genome)) 