"""
DNA Sequence Analyzer
----------------------
A simple beginner-level bioinformatics tool that analyzes a DNA sequence.
 
Features:
1. Counts occurrences of each base (A, T, G, C)
2. Calculates GC content (%)
3. Validates whether the sequence contains only valid DNA bases
 
Author: Anam
"""
 
def analyze_sequence(seq):
    seq = seq.upper()  # make sure input is uppercase for consistent checking
 
    a_count = 0
    t_count = 0
    g_count = 0
    c_count = 0
    is_valid = True
 
    for base in seq:
        if base == "A":
            a_count += 1
        elif base == "T":
            t_count += 1
        elif base == "G":
            g_count += 1
        elif base == "C":
            c_count += 1
        else:
            is_valid = False
            print(f"Invalid base found: {base}")
 
    print("\n--- Base Counts ---")
    print("A:", a_count)
    print("T:", t_count)
    print("G:", g_count)
    print("C:", c_count)
 
    total = len(seq)
    if total > 0:
        gc_content = ((g_count + c_count) / total) * 100
        print(f"\nGC Content: {gc_content:.2f}%")
 
    print("\n--- Validation ---")
    if is_valid:
        print("Sequence is valid! (Contains only A, T, G, C)")
    else:
        print("Sequence is invalid - contains incorrect letters.")
 
 
if __name__ == "__main__":
    # Example usage - you can change this sequence or use input() to enter your own
    seq = input("Enter a DNA sequence: ")
    analyze_sequence(seq)
 
