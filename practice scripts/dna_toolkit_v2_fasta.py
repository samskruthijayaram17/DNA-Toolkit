def gc_content(DNA):
    gc=0
    for base in DNA:
        if base == 'G' or base == 'C':
            gc+=1
    percentage=(gc/len(DNA))*100
    return percentage

def reverse_complement(DNA):
    complement={'A':'T','T':'A','G':'C','C':'G'}
    complement_str=""
    for base in DNA:
        complement_str+=complement[base]
    return complement_str[::-1]

def transcription(DNA):
    return DNA.replace('T','U')

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
fasta_file = os.path.join(script_dir, "data", "example_sequences.fasta")
sequences = []  
with open(fasta_file) as f:
    sequence_name = None
    sequence = ""
    for line in f:
        line = line.strip()  
        if not line:  
            continue
        if line.startswith(">"): 
            if sequence_name is not None:
                sequences.append((sequence_name, sequence))
            sequence_name = line[1:]
            sequence = ""
        else:  
            sequence += line
    if sequence_name is not None:
        sequences.append((sequence_name, sequence))

print("\nDNA TOOLKIT RESULTS")
for name, dna in sequences:
    print(f"\nSequence Name: {name}")
    print(f"Sequence: {dna}")
    print(f"GC Content: {gc_content(dna)}%")
    print(f"Reverse Complement: {reverse_complement(dna)}")
    print(f"RNA Transcription: {transcription(dna)}")
