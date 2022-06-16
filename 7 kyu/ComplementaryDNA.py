# Complementary DNA

def DNA_strand(dna):
    
    char_to_replace = {'A': 'T',
                       'T': 'A',
                       'G': 'C',
                       'C': 'G'}

    return ''.join([char_to_replace[i] for i in dna])
