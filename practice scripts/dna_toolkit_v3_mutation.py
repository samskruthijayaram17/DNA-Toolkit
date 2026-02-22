from Bio import SeqIO
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
fasta_file = os.path.join(script_dir, "data", "example_sequences.fasta")
if not os.path.exists(fasta_file):
    raise FileNotFoundError(f"FASTA file not found: {fasta_file}")
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
def detect_mutations(ref, sample):
    """Compare reference sequence to sample and return list of mutations"""
    mutations = []
    length = min(len(ref), len(sample))
    for i in range(length):
        if ref[i] != sample[i]:
            mutations.append((i+1, ref[i], sample[i]))
    return mutations
print("Sequences loaded:")
for name, seq in sequences:
    print(f"  {name}: {seq}")
if len(sequences) < 2:
    print("\nError: Need at least 2 sequences (1 reference + 1 sample)")
else:
    # First sequence is reference
    reference_name, reference_seq = sequences[0]
    print(f"\n--- REFERENCE SEQUENCE (seq1: {reference_name}) ---")
    print(f"{reference_seq}")
    
    # All other sequences are samples
    print(f"\n--- MUTATION DETECTION RESULTS ---")
    for i in range(1, len(sequences)):
        sample_name, sample_seq = sequences[i]
        mutations = detect_mutations(reference_seq, sample_seq)
        
        print(f"\nSample {i} ({sample_name}):")
        print(f"Sequence: {sample_seq}")
        
        if mutations:
            print(f"Mutations found: {len(mutations)}")
            for pos, ref_base, sample_base in mutations:
                print(f"  Position {pos}: {ref_base} -> {sample_base}")
        else:
            print("No mutations detected")