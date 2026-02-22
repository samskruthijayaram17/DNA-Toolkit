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
txt_file = os.path.join(script_dir, "data", "example_sequences.txt")
sequences = []
with open(txt_file) as f:
    for line in f:
        dna = line.strip()
        if dna: 
            sequences.append(dna)

print("\n--- DNA TOOLKIT RESULTS ---")
for i, dna in enumerate(sequences, 1):
    print(f"\nSequence {i}: {dna}")
    print(f"GC Content: {gc_content(dna)}%")
    print(f"Reverse Complement: {reverse_complement(dna)}")
    print(f"RNA Transcription: {transcription(dna)}")
