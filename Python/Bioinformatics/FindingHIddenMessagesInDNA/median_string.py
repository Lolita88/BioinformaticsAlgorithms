import math

def median_string(k, dna):
    distance = 10000000000 #math.inf
    median = ""
    for i in range(0, int(math.pow(4,k))):
        pattern = number_to_pattern(i,k)
        #prints all possible patterns of AA-TT
        #print(pattern)
        #if(d(pattern, dna) <= distance):
        if distance_between_pattern_and_strings(pattern, dna) <= distance:
            distance = distance_between_pattern_and_strings(pattern, dna)
            median = pattern
    return median
    
def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for i in range(len(dna)):
        ham_distance = 100000000000 #math.inf
        #print(type(hamming_distance))
        dna_length = len(dna[0])
        for j in range(0, dna_length-k+1):
            sliding_pattern = dna[i][j:j+k]
            #print(sliding_pattern)
            #print(pattern)
            if ham_distance > hamming_distance(pattern, sliding_pattern):
                print("oh hello")
                ham_distance = hamming_distance(pattern, sliding_pattern)
        distance = distance + ham_distance
    return distance

def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = math.floor(index/4)
    r = index%4
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol

def number_to_symbol(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'

def hamming_distance(pattern1, pattern2):
    distance = 0
    for x, y in zip(pattern1, pattern2):
        if x != y :
            distance += 1
    return distance

print(median_string(3, ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTTCGGGACAG"]))
