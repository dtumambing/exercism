def to_rna(dna):
    rna = ''

    for i,d in enumerate(dna):
        if d == 'G':
            rna += 'C'
        elif d == 'C':
            rna += 'G'
        elif d == 'T':
            rna += 'A'
        elif d == 'A':
            rna += 'U'
        else:
            return ''

    #test differ
    return rna

