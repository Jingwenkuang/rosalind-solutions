# Download and process
import requests
url = "https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ads1_week4_reads.fq"
response = requests.get(url)
with open("read_fastq", "wb") as f:
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

reads = read_fastq("read_fastq")

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

import itertools

def greedy_scs(reads, k):
    # Create a dictionary of all possible k-mers to reads that contain them
    kmer_to_reads = {}
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            if kmer not in kmer_to_reads:
                kmer_to_reads[kmer] = set()
            kmer_to_reads[kmer].add(read)
    
    # For each read, find all other reads that share a k-mer
    read_graph = {}
    for read in reads:
        read_graph[read] = set()
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            for other_read in kmer_to_reads[kmer]:
                if other_read != read:
                    olen = overlap(read, other_read, min_length=k)
                    if olen > 0:
                        read_graph[read].add((other_read, olen))
    
    # Now, greedily merge reads with maximum overlap
    while True:
        # Find the pair with maximum overlap
        max_overlap = 0
        best_pair = None
        for read in read_graph:
            for other_read, olen in read_graph[read]:
                if olen > max_overlap:
                    max_overlap = olen
                    best_pair = (read, other_read)
        if max_overlap == 0:
            break  # no more overlaps to merge
        a, b = best_pair
        # Merge a and b
        merged = a + b[max_overlap:]
        # Remove a and b from the graph
        del read_graph[a]
        del read_graph[b]
        # Remove any references to a or b in other reads' edges
        for read in list(read_graph.keys()):
            edges = read_graph[read]
            new_edges = set()
            for (other_read, olen) in edges:
                if other_read != a and other_read != b:
                    new_edges.add((other_read, olen))
            read_graph[read] = new_edges
        # Add the merged read to the graph
        read_graph[merged] = set()
        # Compute overlaps between merged and other reads
        for read in read_graph:
            if read != merged:
                olen = overlap(read, merged, min_length=k)
                if olen > 0:
                    read_graph[read].add((merged, olen))
                olen = overlap(merged, read, min_length=k)
                if olen > 0:
                    read_graph[merged].add((read, olen))
    # At this point, read_graph should have one read left
    if len(read_graph) != 1:
        print("Error: Assembly did not result in a single contig.")
        return None
    return list(read_graph.keys())[0]

genome = greedy_scs(reads, k=30)
a_count = genome.count('T')
print(a_count)