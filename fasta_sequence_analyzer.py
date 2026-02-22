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
codon_table={'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
             'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L', 'TAA':'*', 'TAG':'*', 'TGA':'*',
             'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'AGT':'S', 'AGC':'S',
             'TGG':'W', 'CAA':'Q', 'CAG':'Q', 'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
             'GAA':'E', 'GAG':'E', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'CAT':'H', 'CAC':'H', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
             'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L'}
def translate_dna(sequence):
    amino_acids = ""
    valid_bases = set('ATGC')
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if len(codon) == 3 and all(base in valid_bases for base in codon):
            if codon in codon_table:
                amino_acids += codon_table[codon]
            else:
                amino_acids += 'X'
        else:
            amino_acids += 'X'
    return amino_acids
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
print("\n--- FASTA FILE CONTENTS WITH TRANSLATION ---\n")
print(f"Total number of sequences: {len(sequences)}")
for name, seq in sequences:
    seq = seq.upper()
    valid_bases = set('ATGC')
    invalid_bases = set(seq) - valid_bases
    if invalid_bases:
        print(f"Sequence Name:{name}")
        print(f"WARNING: Found invalid DNA bases:{','.join(sorted(invalid_bases))}")
        print(f"These will be treated as 'X' during translation")
    amino_acid_seq = translate_dna(seq)
    print(f"Sequence Name:{name}")
    print(f"DNA Sequence:{seq}")
    print(f"GC Content: {gc_content(seq)}%")
    print(f"Reverse Complement: {reverse_complement(seq)}")
    print(f"RNA Transcription: {transcription(seq)}")
    print(f"Amino Acid Sequence:{amino_acid_seq}")
    print(f"Sequence Length:{len(seq)} bp,{len(amino_acid_seq)} aa")
    print("Amino Acid Frequencies:")
    unique_amino_acids=sorted(set(amino_acid_seq))
    for aa in unique_amino_acids:
        count=amino_acid_seq.count(aa)
        print(f"{aa}:{count}")
    print()