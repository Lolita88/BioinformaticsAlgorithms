
def motif_enumeration(dna, k, d):
    dna_patterns = []
    dna_length = len(dna[0])
    temp_patterns = []
    pattern_neighbors = []
    pattens = []
    #save all patterns from first dna row in pattern_neighbors
    for i in range(0, dna_length-k + 1):
        #print(dna[0][i:i+k])
        dna_patterns.append(dna[0][i:i+k])
    #print(dna_patterns)
    for each in dna_patterns:
        #print(neighbors(each, d))
        pattern_neighbors.append(neighbors(each, d))
    #print(pattern_neighbors)
    #print(len(dna))
    found = False
    #for each neighbor from first row in dna
    for row in pattern_neighbors:
        for each in row:
            #print(each)
            #loop through remaining dna strands over and over to see if neighbors are found
            for i in range(0, len(dna)):
                #print(dna[i])
                #for each k-mer in the strand
                for j in range(1, dna_length - k + 1):
                    each_dna_pattern = dna[i][j:j+k]
                    #print(dna[i][j:j+k])
                    if(hamming_distance(each_dna_pattern, each) <= d):
                        #add first time
                        print(str(each_dna_pattern) + " and " + str(each))
                        found = True
                        #temp_patterns.append(each)
                        #next time check to see if each is in temp_pattern if it isn't, delete
                    else:
                        found = False
                        break
                if found == True:
                    print(each_dna_pattern)
    #print(temp_patterns)    
    #remove duplicates from patterns
    #return patterns  

"""def motif_enumeration(dna, k, d):
    patterns = []
    for row in dna:
        dna_length = len(row)
        for i in range(0, dna_length - k + 1):
            pattern = row[i:i+k]
            dna_neighbors = neighbors(pattern, d)
            for  candidate in dna_neighbors:
                if pattern_is_motif(dna, candidate, d, k) == True:
                    patterns.append(candidate)
    #print(patterns)
    patterns = remove_duplicates(patterns)
    print(patterns)
    return patterns"""

def pattern_is_motif(dna, pattern, d, k):
    dna_length = len(dna[0])
    for row in dna:
        for i in range(0, dna_length - k + 1):
            if hamming_distance(pattern, row[i:i+k]) <= d:
                return True
        return False

def remove_duplicates(text):
    no_duplicates = []
    for item in text:
        if item not in no_duplicates:
            no_duplicates.append(item)
    return no_duplicates

"""def neighbors(pattern, d):
    alt_bases = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
    suffix = pattern[1:]
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {"A", "C", "G", "T"} 
    neighborhood = []
    suffix_neighbors = neighbors(suffix, d)
    for text in suffix_neighbors:
        if hamming_distance(suffix, text) < d:
            for nucleotide_x in alt_bases:
                neighborhood.append(nucleotide_x + text)
        else:
            neighborhood.append(pattern[0] + text)
    #neighborhood = neighborhood.sort()
    #print (neighborhood.sort())
    return neighborhood"""

def neighbors(pattern, d):
    if d == 0:
        return ([pattern])
    if len(pattern) == 1:
        return (['A', 'C', 'G', 'T'])
    neighborhood = []
    suffix_neighbors = neighbors(suffix(pattern), d)

    for text in (suffix_neighbors):
        if hamming_distance(suffix(pattern), text) <d:
            for base in "ACGT":
                neighborhood.append(base + text)
        else:
            neighborhood.append(first_symbol(pattern) + text)
    return (neighborhood)

def first_symbol(pattern):
    return pattern[0]

def suffix(pattern):
    suffix = pattern[1:len(pattern)]
    return (suffix)

def hamming_distance(pattern1, pattern2):
    distance = 0
    for x, y in zip(pattern1, pattern2):
        if x != y :
            distance += 1
    return distance

dna = ['ATTTGGC','TGCCTTA','CGGTATC','GAAAATT']
motif_enumeration(dna, 3, 1)
