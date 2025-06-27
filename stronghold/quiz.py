import sys
from collections import defaultdict

def read_fasta(filename):
    """Read a FASTA file and return a dictionary of sequences."""
    sequences = {}
    filename = "/Users/xx/Desktop/dna2.fasta"
    with open(filename, 'r') as f:
        current_id = None
        current_seq = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_id is not None:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id is not None:
            sequences[current_id] = ''.join(current_seq)
    return sequences

def count_records(sequences):
    """Return the number of records in the FASTA file."""
    return len(sequences)

def sequence_lengths(sequences):
    """Return information about sequence lengths."""
    lengths = {seq_id: len(seq) for seq_id, seq in sequences.items()}
    max_len = max(lengths.values())
    min_len = min(lengths.values())
    max_seqs = [seq_id for seq_id, length in lengths.items() if length == max_len]
    min_seqs = [seq_id for seq_id, length in lengths.items() if length == min_len]
    return {
        'lengths': lengths,
        'max_length': max_len,
        'min_length': min_len,
        'max_sequences': max_seqs,
        'min_sequences': min_seqs
    }

def find_orfs(sequence, frame):
    """Find all ORFs in a sequence for a given reading frame (1, 2, or 3)."""
    orfs = []
    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']
    
    # Adjust for frame (1 becomes 0, 2 becomes 1, 3 becomes 2)
    start_pos = frame - 1
    sequence = sequence[start_pos:]
    
    i = 0
    while i < len(sequence) - 2:
        codon = sequence[i:i+3]
        if codon == start_codon:
            # Found start codon, look for stop codon
            for j in range(i+3, len(sequence)-2, 3):
                stop_codon = sequence[j:j+3]
                if stop_codon in stop_codons:
                    # Found ORF from i to j+3
                    orfs.append({
                        'start': i + 1 + start_pos,  # convert to 1-based
                        'end': j + 3 + start_pos,
                        'length': (j + 3) - i
                    })
                    i = j + 3  # skip ahead to after stop codon
                    break
            else:
                # No stop codon found, skip this start codon
                i += 3
        else:
            i += 3
    
    return orfs

def find_all_orfs(sequences, frame):
    """Find all ORFs in all sequences for a given frame."""
    all_orfs = {}
    for seq_id, seq in sequences.items():
        orfs = find_orfs(seq, frame)
        all_orfs[seq_id] = orfs
    return all_orfs

def longest_orf_info(all_orfs):
    """Find the longest ORF across all sequences."""
    longest_length = 0
    longest_orf_info = None
    per_sequence_longest = {}
    
    for seq_id, orfs in all_orfs.items():
        if orfs:
            seq_longest = max(orfs, key=lambda x: x['length'])
            per_sequence_longest[seq_id] = seq_longest
            if seq_longest['length'] > longest_length:
                longest_length = seq_longest['length']
                longest_orf_info = {
                    'sequence_id': seq_id,
                    'start': seq_longest['start'],
                    'length': seq_longest['length']
                }
    
    return {
        'overall_longest': longest_orf_info,
        'per_sequence': per_sequence_longest
    }

def find_repeats(sequences, n):
    """Find all repeats of length n in all sequences."""
    repeat_counts = defaultdict(int)
    
    for seq in sequences.values():
        # Find all possible substrings of length n
        for i in range(len(seq) - n + 1):
            substring = seq[i:i+n]
            repeat_counts[substring] += 1
    
    # Filter to only repeats (count > 1)
    repeats = {k: v for k, v in repeat_counts.items() if v > 1}
    
    if not repeats:
        return None
    
    most_frequent = max(repeats.items(), key=lambda x: x[1])
    
    return {
        'all_repeats': repeats,
        'most_frequent': {
            'repeat': most_frequent[0],
            'count': most_frequent[1]
        }
    }

def main(filename):
    # Read the FASTA file
    sequences = read_fasta(filename)
    
    # Question 1: Number of records
    num_records = count_records(sequences)
    print(f"1. Number of records: {num_records}")
    
    # Question 2: Sequence lengths
    length_info = sequence_lengths(sequences)
    print("\n2. Sequence length information:")
    print(f"   - Longest sequence: {length_info['max_length']} bp")
    print(f"     Sequences with this length: {', '.join(length_info['max_sequences'])}")
    print(f"   - Shortest sequence: {length_info['min_length']} bp")
    print(f"     Sequences with this length: {', '.join(length_info['min_sequences'])}")
    
    # Question 3: ORFs (using frame 1 as example)
    frame = 1
    all_orfs = find_all_orfs(sequences, frame)
    orf_info = longest_orf_info(all_orfs)
    
    print("\n3. ORF information (reading frame 1):")
    if orf_info['overall_longest']:
        print(f"   - Longest ORF in file: {orf_info['overall_longest']['length']} bp")
        print(f"     Sequence ID: {orf_info['overall_longest']['sequence_id']}")
        print(f"     Starting position: {orf_info['overall_longest']['start']}")
    else:
        print("   - No ORFs found in reading frame 1")
    
    # Example of per-sequence ORF info (just show first few)
    print("\n   - Longest ORF per sequence (first few examples):")
    for i, (seq_id, orf) in enumerate(orf_info['per_sequence'].items()):
        if i >= 3:  # Limit output
            break
        print(f"     {seq_id}: length {orf['length']}, starts at {orf['start']}")
    
    # Question 4: Repeats (using n=7 as example)
    n = 7
    repeat_info = find_repeats(sequences, n)
    
    print(f"\n4. Repeat information (length {n}):")
    if repeat_info:
        print(f"   - Most frequent repeat: {repeat_info['most_frequent']['repeat']}")
        print(f"     Count: {repeat_info['most_frequent']['count']}")
        print(f"   - Total distinct repeats of length {n}: {len(repeat_info['all_repeats'])}")
    else:
        print(f"   - No repeats of length {n} found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dna_analysis.py <fasta_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    main(input_file)