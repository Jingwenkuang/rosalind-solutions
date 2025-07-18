# Download and process
import requests
url = "https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ERR266411_1.for_asm.fastq"
response = requests.get(url)
with open("reads.fastq", "wb") as f:
    f.write(response.content)
import urllib.request


def read_fastq(filename):
    sequences = []
    with open(filename, 'r') as f:
        while True:
            f.readline()  # skip name line
            seq = f.readline().rstrip()  # read sequence line
            f.readline()  # skip placeholder line
            f.readline()  # skip quality line
            if not seq:
                break
            sequences.append(seq)
    return sequences

reads = read_fastq("reads.fastq")

def overlap(a, b, min_length=3):
    start = 0 
    while True:
        start = a.find(b[:min_length], start)  
        if start == -1: 
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1  # move just past previous match

def build_kmer_dict(reads, k):
    kmer_dict = {}
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i: i + k]
            if kmer not in kmer_dict:
                kmer_dict[kmer] = set()
            kmer_dict[kmer].add(read)
    return kmer_dict

#--------------------------3----------------------------
# def find_overlaps(reads, k):
#     kmer_dict = build_kmer_dict(reads, k)
#     overlaps = []
#     for a in reads:
#         suffix = a[-k:]
#         reads_with_kmer = kmer_dict.get(suffix, set())
#         for b in reads_with_kmer:
#             if a != b:
#                 olen = overlap(a, b, min_length=k)
#                 if olen >= k:
#                     overlaps.append((a, b, olen))
#     return overlaps

#--------------------------4-----------------------------
def find_overlaps(reads, k):
    kmer_dict = build_kmer_dict(reads, k)
    overlaps = []
    outgoing_nodes = set()
    for a in reads:
        suffix = a[-k:]
        reads_with_kmer = kmer_dict.get(suffix, set())
        for b in reads_with_kmer:
            if a != b:
                olen = overlap(a, b, min_length=k)
                if olen >= k:
                    overlaps.append((a, b, olen))
                    outgoing_nodes.add(a)
    return len(overlaps), len(outgoing_nodes)

# reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']

print(find_overlaps(reads, 30))

