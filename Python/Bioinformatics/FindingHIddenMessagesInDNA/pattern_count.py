import sys
lines = sys.stdin.read().splitlines() # read in the input from STDIN
#text = lines[0]
#pattern = lines[1]

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if(text[i:i + len(pattern)] == pattern):
            count +=1
    return count

print (pattern_count(lines[0], lines[1]))

