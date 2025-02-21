# DNA Toolset/Code testing file
from dna_toolkit import *
from utilities import colored
import random

# Creating a random DNA sequence for testing
randomDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])

DNAStr = validate_seq(randomDNAStr)

# print(f'\nSequence: {colored(DNAStr)}\n')
# print(f'[1] + Sequence length: {len(DNAStr)}\n')
# print(colored(f'[2] + Nucleotide Frequency: {nucleotide_frequency(DNAStr)}\n'))
# print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')
# print(f"[4] + DNA String + Reverse Complement: \n5' {colored(DNAStr)} 3'")
# print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
# print(f"3' {colored(reverse_complement(DNAStr)[::-1])} 5' [Complement]\n")
# print(f"5' {colored(reverse_complement(DNAStr))} 3' [Rev. Complement]\n")
# print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
# print(f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')
# print(f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr)}\n')
# print(f'[8] + Codon frequency (L): {condon_usage(DNAStr, "L")}\n')

print(f'[9] + Reading frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)

# test_rf_frame = ['R', 'M', 'Y', 'V', 'R', 'G', '_', 'Q', 'P', 'G', 'S', 'E', 'D', 'V', 'S', 'C']
# print(proteins_from_rf(test_rf_frame))

print('\n[10] + All proteins in 6 open reading frames:')
for protein in all_proteins_from_orfs(DNAStr, 0, 0, True):
    print(f'{protein}')