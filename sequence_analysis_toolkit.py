from Bio import SeqIO
import os

def gc_content(DNA):
    """Calculate GC content percentage of sample DNA sequence."""
    if not DNA:
        return 0.0
    gc = 0
    for base in DNA:
        if base == 'G' or base == 'C':
            gc += 1
    percentage = (gc / len(DNA)) * 100
    return percentage

def detect_mutations(ref, sample):
    """Compare sample sequence to reference and return list of mutations."""
    mutations = []
    length = min(len(ref), len(sample))
    for i in range(length):
        if ref[i] != sample[i]:
            mutations.append((i+1, ref[i], sample[i]))
    return mutations

def find_motif(sequence, query):
    """Find all positions of a query motif in a sequence."""
    if not query:
        return []
    positions = []
    qlen = len(query)
    for i in range(len(sequence) - qlen + 1):
        if sequence[i:i+qlen] == query:
            positions.append(i+1)
    return positions

script_dir = os.path.dirname(os.path.abspath(__file__))
fasta_file = os.path.join(script_dir, "data", "example_framewise.fasta")
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

print("Samples loaded:")
for name, seq in sequences[1:]:
    print(f"  {name}: {len(seq)} bp")

if len(sequences) < 2:
    print("\nError: Need at least 2 sequences (1 reference + 1 sample)")
else:
    # First sequence is reference
    reference_name, reference_seq = sequences[0]
    reference_seq = reference_seq.upper()
    
    # === PART 1: GC CONTENT ANALYSIS (SAMPLES ONLY) ===
    print("--- GC CONTENT ANALYSIS (SAMPLES) ---")
    for i in range(1, len(sequences)):
        sample_name, sample_seq = sequences[i]
        sample_seq = sample_seq.upper()
        gc = gc_content(sample_seq)
        print(f"Sample {i} ({sample_name}): {gc:.2f}%\n")
    
    # === PART 2: MUTATION DETECTION ===
    print("--- MUTATION DETECTION RESULTS ---")
    for i in range(1, len(sequences)):
        sample_name, sample_seq = sequences[i]
        sample_seq = sample_seq.upper()
        mutations = detect_mutations(reference_seq, sample_seq)
        
        print(f"\nSample {i} ({sample_name}):")
        
        if mutations:
            print(f"Mutations found: {len(mutations)}")
            for pos, ref_base, sample_base in mutations:
                print(f"  Position {pos}: {ref_base} -> {sample_base}")
        else:
            print("No mutations detected")
    
    # === PART 3: MOTIF FINDING ===
    print("\n--- MOTIF SEARCH ---")
    # Hardcode the motif here (only in-code). Example: query = "ATG"
    query = "GC"  # set motif here
    query = (query or "").strip().upper()

    if not query:
        print("No motif provided in code. Skipping motif search.")
    else:
        print(f"\nSearching for motif: {query}\n")

        # Search only in samples (exclude reference)
        for i in range(1, len(sequences)):
            sample_name, sample_seq = sequences[i]
            sample_seq = sample_seq.upper()
            matches = find_motif(sample_seq, query)
            print(f"\nSample {i} ({sample_name}):")
            if matches:
                print(f"  Positions found: {matches}")
            else:
                print(f"  No matches found")