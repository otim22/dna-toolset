def countNucFrequency(seq):
    # Method 1
    tmptFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmptFreqDict[nuc] += 1
    return tmptFreqDict
    
    # Method 2
    # return dict(collections.Counter(seq))

DNAString = "ATCGTCTGTG"

result = countNucFrequency(DNAString)
print(' '.join([str(val) for key, val in result.items()]))