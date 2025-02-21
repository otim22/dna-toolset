# DNA Toolset/Code testing file

from bio_seq import bio_seq

# test_dna = bio_seq("ATCG", "DNA", "Test Label")
test_dna = bio_seq()
test_dna.generate_rnd_seq(40, "DNA")

print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
print(test_dna.transcription())
print(test_dna.seq)
print(test_dna.reverse_complement())
print(test_dna.gc_content())
print(test_dna.gc_content_subsec())
print(test_dna.translate_seq())
print(test_dna.condon_usage("L"))

# print(test_dna.gen_reading_frames())
for rf in test_dna.gen_reading_frames():
    print(rf)

# print(test_dna.proteins_from_rf(
#     ['L', 'M', 'A', 'C', 'Y', 'S', 'I', 'H', 'G', 'T', 'S', '_', 'W']
# ))

print(test_dna.all_proteins_from_orfs())