#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    locations = []
    len1 = len(dna_string1)
    len2 = len(dna_string2)
    for i in range(len1 - len2 + 1):
        current_slice = dna_string1[i : i + len2]
        if current_slice == dna_string2:
            locations.append(i + 1)
    return tuple(locations)