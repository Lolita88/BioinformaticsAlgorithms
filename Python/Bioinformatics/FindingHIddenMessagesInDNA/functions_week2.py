def skew(genome):
    skew_array = {}
    skew_array[0] = 0
    minimun_skew = 0
    minimum_skew_array = []
    for i in range(1, len(genome) + 1):
        if genome[i-1] == 'G':
            skew_array[i] = skew_array[i-1] + 1
        elif genome[i-1] == 'C':
            skew_array[i] = skew_array[i-1] - 1
        else:
            skew_array[i] = skew_array[i-1]
    return skew_array
    #return ' '.join([str(skew_array[i]) for i in sorted(skew_array.keys())])

def minimum_skew(genome):
    temp_skew = skew(genome)
    min_value = min(temp_skew.values())
    min_keys = [k for k in temp_skew if temp_skew[k] == min_value]
    #return min_keys
    return ' '.join(str(x) for x in min_keys)

def hamming_distance(pattern1, pattern2):
    distance = 0
    for x, y in zip(pattern1, pattern2):
        if x != y :
            distance += 1
    return distance

def approximate_pattern_matching(pattern, genome, d):
    positions = []
    for i in range(0, len(genome) - len(pattern) + 1):
        if(hamming_distance(pattern, genome[i:i + len(pattern)]) <= d):
            positions.append(i)
    #return positions
    return ' '.join(str(x) for x in positions)

def approximate_pattern_count(pattern, genome, d):
    count = 0
    for i in range(0, len(genome) - len(pattern) + 1):
        if(hamming_distance(pattern, genome[i:i + len(pattern)]) <= d):
            count += 1
    return count

def pattern_to_number(pattern):
    k = len(pattern)
    if k == 0:
        return 0
    symbol = pattern[k-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)

def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = math.floor(index/4)
    r = index%4
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol

def frequent_words_with_mismtaches(genome, k, d):
    frequent_patterns = []
    frequency_array = []
    close = []
    for i in range(0, 4 ** k - 1):
        close[i] = 0
        #frequecy_array[i] = 0
    for i in range(0, len(genome) - k - 1):
        neighborhood = neighbors(genome(i, k), d)
        for pattern in neighborhood:
            index = pattern_to_number(pattern)
            close[index] = 1
    for i in range(0, 4 ** k -1):
        if close[i] == 1:
            pattern = number_to_pattern(i, k)
            frequency_array[i] = approximate_pattern_count(genome, pattern, d)
    max_count = max(frequency_array)
    for i in range(0, 4 ** k -1):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    return frequent_patterns

    

print (frequent_words_with_mismtaches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))
#print (approximate_pattern_count("GGATCGC", "AGGGCCCCATATGCTCGTGCCCACAATTGGGGATCGCATCAGCGGCATCGTTTTCGGTTACCGGACTCCGGTATGCGTCCGTCCTTTATGCTGAGAAGAAGTAGGTAAGTACACCATTTAGGAGAGCTCGAGAGTCCCCGACGCATAAATCCATTTGAGACGTCTCACGCGCAAGTCCCTTTCCACTCTCCTTGATGGTCCCCCTCTTTGGACTGGACCTTGAGCTGTCAATAGGGGACGCCCCGCCAGTTAGTGGGATTGAAGTCTCCACTGTGGTGACTAATATCGAAGCTCCGACGGGCGA", 3))
#print(approximate_pattern_matching("ATTCTGGA", "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", 3))