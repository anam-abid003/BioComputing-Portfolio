DNA Sequence Analyzer

A simple Python tool that analyzes a DNA sequence and reports its base composition, GC content, and validity. Built as a beginner-friendly introduction to combining basic Python programming with core bioinformatics concepts.

What it does

Given a DNA sequence (a string of A, T, G, C), the script:

Counts each base — how many A's, T's, G's, and C's are in the sequence
Calculates GC content — the percentage of the sequence made up of Guanine (G) and Cytosine (C), a value commonly used in genome analysis and organism identification
Validates the sequence — checks whether the sequence contains only valid DNA bases (A, T, G, C), flagging any unexpected characters (useful for catching errors in raw sequencing data)
Why GC content matters

GC content is a simple but widely used metric in molecular biology:

Higher GC content is associated with greater thermal/structural stability of DNA
It's used to help identify and classify organisms (e.g., in microbiology)
It's a standard first step in analyzing any new sequence
How to run it
bash
python dna_analyzer.py

You'll be prompted to enter a DNA sequence, for example:

Enter a DNA sequence: ATGCGCTA
Example output
--- Base Counts ---
A: 2
T: 2
G: 2
C: 2

GC Content: 50.00%

--- Validation ---
Sequence is valid! (Contains only A, T, G, C)
Example with an invalid sequence
Enter a DNA sequence: ATGCXGCTA
Invalid base found: X

--- Base Counts ---
A: 2
T: 2
G: 2
C: 2

GC Content: 44.44%

--- Validation ---
Sequence is invalid - contains incorrect letters.
Concepts used
Loops and conditionals (for, if/elif/else)
String iteration and indexing
Flag variables for validation logic
Basic arithmetic for percentage calculations
Functions for reusable, organized code
Future improvements
Add reverse complement calculation (a key operation in primer design and PCR)
Fetch real sequences directly from NCBI using Biopython (Bio.Entrez)
Support FASTA file input instead of manual entry
Add unit tests

Author
Anam — BS Biotechnology student, building a bioinformatics/computational biology portfolio.
