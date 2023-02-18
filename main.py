def dna(txt):
    trans_table = str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'})
    replaced = txt.translate(trans_table)
    return replaced

print(dna('AATTAG'))