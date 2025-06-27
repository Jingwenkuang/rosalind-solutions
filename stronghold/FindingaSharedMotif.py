def read_fasta_txt(file_path):
    """
    Reads a FASTA-format text file and returns a list of DNA sequences.
    """
    sequences = []
    current_sequence = ''
    
    with open('/Users/xx/Desktop/rosalind_lcsm.txt', 'r') as file:
        for line in file:
            line = line.strip()
            
            # If it's a header line (starts with '>'), save the current sequence
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ''
            else:
                current_sequence += line  # Keep adding DNA lines together
        
        # Add the last sequence after the loop ends
        if current_sequence:
            sequences.append(current_sequence)
    return sequences #['GATTACA', 'TAGACCA', 'ATACA']


def longest_common_substring_from_txt(file_path):
    """
    Finds the longest common substring among all DNA sequences
    in a FASTA-format text file.
    """
    sequences = read_fasta_txt(file_path) #['GATTACA', 'TAGACCA', 'ATACA']
    
    # Choose the shortest sequence to reduce the number of substrings to check
    shortest_seq = min(sequences, key=len) #'ATACA'
    shortest_len = len(shortest_seq)       #5

    # Start with the longest possible substrings and go down in size
    for substr_len in range(shortest_len, 0, -1):  #substr_len = 5, then 4, 3, down to 1
        # Slide a window of length 'substr_len' across the shortest sequence
        for start in range(shortest_len - substr_len + 1):  
            # Extract the current substring
            substring = shortest_seq[start:start + substr_len]

            # Check if this substring exists in every sequence
            found_in_all = True
            for seq in sequences:
                if substring not in seq:
                    found_in_all = False
                    break  # No need to check the rest
            
            if found_in_all:
                return substring  # Found the longest common substring

    return ""  # No common substring found


# Example usage:
# Save your FASTA-style text file as 'input.txt'
result = longest_common_substring_from_txt("input.txt")
print("Longest common substring:", result)
