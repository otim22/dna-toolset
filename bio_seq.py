from bio_structs import *
from collections import Counter
import random

class bio_seq:
    """DNA Sequence class. Default value: ATCG, DNA, No label"""

    def __init__(self, seq="ATCG", seq_type="DNA", label="No label"):
        """Sequence initialization validation."""
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} sequence"
    
    # DNA Toolkit functions
    def __validate(self):
        """Check the sequence to make sure it is a DNA String"""
        return set(DNA_Nucleotides).issuperset(self.seq)
    
    def get_seq_biotype(self):
        """Returns sequence type"""
        return self.seq_type

    def get_seq_info(self):
        """Return 4 strings. Full sequence information"""
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"
    
    def generate_rnd_seq(self, length=10, seq_type="DNA"):
        """Generate a random DNA sequence, provided the length"""
        seq = ''.join([random.choice(DNA_Nucleotides) for x in range(length)])
        self.__init__(seq, seq_type, "Randomly generated sequence")

    def nucleotide_frequency(self):
        """Count nucleotides in a given sequence. Return a dictionary"""
        return dict(Counter(self.seq))
