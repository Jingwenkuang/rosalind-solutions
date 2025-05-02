# method 1
def transcription(dna):
    rna = ''
    upperDNA = dna.upper()
    for nucleotide in upperDNA:
        if nucleotide == 'T':
            rna = rna + 'U'
        else:
            rna = rna + nucleotide
    return rna 

dna = 'GATGGAACTTGACTACGTAAATT'
print(transcription(dna))

# method 2
def transcription(dna):
    return dna.replace('T', 'U')
print(transcription(dna))