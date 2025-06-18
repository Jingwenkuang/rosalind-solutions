def RNAtoProtein(sequence):
    CODON = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'  
    }
    protein = ''
    for i in range(0, len(sequence), 3):
        codon = sequence[i: i + 3]
        # amino_acid = CODON.get(codon, '') 
        #the codon is invalid (but the code continues without adding anything to protein
        amino_acid = CODON[codon] # Raises KeyError if codon is invalid
        if amino_acid == '*':
            break
        protein += amino_acid
    return protein

sequence = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
# sequence = 'UGGGCCUCAUAUUUAUCCUAUAUACCAUGUUCGUAUGGUGGCGCGAUGUUCUACGUGAAUCCACGUUCGAAGGACAUCAUACCAAAGUCGUACAAUUAGGACCUCGAUAUGGUUUUAUUCUGUUUAUCGUAUCGGAGGUUAUGUUCUUUUUUGCUCUUUUUCGGGCUUCUUCUCAUUCUUCUUUGGCACCUACGGUAGAGUGGGCCUCAUAUUUAUCCUAUAUACCAUGUUCGUAUGGUGGCGCGAUGUUCUACGUGAAUCCACGUUCGAAGGACAUCAUACCAAAGUCGUACAAUUAGGACCUCGAUAUGGUUUUAUUCUGUUUAUCGUAUCGGAGGUUAUGUUCUUUUUUGCUCUUUUUCGGGCUUCUUCUCAUUCUUCUUUGGCACCUACGGUAGAG'
print(RNAtoProtein(sequence))