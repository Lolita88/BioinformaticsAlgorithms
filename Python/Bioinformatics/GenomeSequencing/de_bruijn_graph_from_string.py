def de_bruijn_graph_from_string(dna, k):
    kmers = []
    adjacency_list = {}
    
    # split out all kmers, length of the k passed in
    for i in range(len(dna) - k + 1):
        kmers.append(dna[i:i+k])
    kmers.sort()
    
    for i in range(len(kmers)):
        pre = kmers[i][0:-1]
        suf = kmers[i][1:]
        if(pre[1:] == suf[:-1]):
            #add to dict for output
            if pre in adjacency_list.keys(): # if already there, append
                adjacency_list[pre] += ("," + suf)
            else: # write anew
                adjacency_list[pre] = pre + " -> " + suf
    return adjacency_list.values()

k = 12
dna = "CTAATTTCCCGCAGCATTGCCAAGAAGTACTGCACGAACAAATATAAAGTCCCTATATACTCTAACTACCCTTCTGTTGTGGTAGATCGGGCAACTAAGTGGCCAGCAGGAGACACCCTCACCCGATGGGCTATGAACGCAGGCGGTGCAACCGCTAAGCTCTGTTGTGGGGAGAGGTGCCACTCTCTATGTGTTTGGACAACGTTAAAATCCCTAGCTATTGTTGAACTCATAGGGGTTGTCTTCGGCGTGGCTAGTATCGGACTCAGCTCAGATCTTTCTGTCGTATCTTGGAGGCATGCATAGACCCGGCCAGGCCAGCACTTGCACGCGGTCCGGCTCCCTTGCTAGCGCGCATTGGAATCTAACAACATCAGGGCAGCGCCGGCTACAGTCCCTCAATTGTGTGTCGGTTGAACGTGAGCCGAGATATTTGAAACCCTTTCGTGTCGTCATTGTGTTTGTCGGTCCTTTCTGAGTGTCCACACTGTAGGCGTATTTAGCCGTGCGGATCCCTGGTGGTTAACGATTTTAATGCGCCGAATAAAGGTACAGTTCTGGTTGTTATAGTGTTCTTGCGGATGTGGCAATACACGGCCATACGCAGACTGTTGTGGGGCTGGTGAGAATCGGTAGCTTACGTTGCCACACACCGGCGCCTCCCAAACGACCTCCCCAGAGTCGTCCCCTCTGTACACCCCCGCTTCAGTTAGAGAACGAGACACCGCCTTAGCGCAAATGGAAATAGCCATCGCCTCTGACCCTTTCTGTCAGCAAGGCGAAACAGTACATTAGAGTTGTCAGATGTTGTGCAGAGTGAGCGTAACAAGCGTAATTACGCGGCGGATTCTTAGAGCGCAAACTATCCGTCGTCATCGCGTCAGGCCTCCTTATAGCTATGTATCCACGGTTTCCCAAGTGGCTATAGATACCGAATCAGAAACCCTTTTAGACAAGGGCGAATGCCATTTTGGTGAGGAACTTCCTTGGTATGGGAGAAGGTGCTCATATAGCGGACAGGACTTTCAGAGGCCCTCCCTCACAAGAGTAACATCCGTGCACAGTGTTCTGTACCAGGTCCATGGACGCCTGAGGATTACGCGTAAGAGCTGTTCTTCGCTCGAATACTAGCCTCGTCTTAAACAAATTCTAACAATTTCGCGCGCTTGGGTCAAAATGGTCGCCAAGTCCTTGAATGGTCTTCGACACCGGTCTTCGTAGGGGCCTGAGCGTGATTAGGCACCCCACTTTACTATTGCATACGACCGTATAATGGAAGGAGTGACAATCCTTCGACGTATATCTTCGAATGCATGATTCCTCATCGGGCTCGGAAGGCCCAAGAGACAGCCAACATTCGCGGCAGAAGCGACTAACGTCAATATAAATTTTCGGTTAGGAGCTTCCAATCACGGTTGCATTCGCTTCCATTTCTGAACCGGACTCTTTGAATAAGCCAAGGCCAATCCGTGCGGATTGGGTGGAACTGAGACGATAAAGGGCATGCGTTCACTCCAGGCACTCAAGGGTTATAACAAGAAGGTTGAACATGTCAGTTGCCACCTGATGTACGTAGCAGGATCAAACCGCACGGCACGGAACAAATGCTGACTCCCTACTGACACTGGGAAAATCATGGGCACTCCCTCAATGTCTTCTCGGTGTTGCTGCTAGAACGGGGCCTCGCTGTTGGTGGAATTGGACCGCATTATCAGGACTTGTGAATTAGAAGTCAGAGGGTAAAGCGCAAATATCTGGGAAGGACCAAATATACGTATGTAGCCACCTACCTCGATAATGCACAATTCGGTCCCTGTAAAGGTTACTGCGTGTGCTTATTAATGGCGGGAAAGTGTGGTCGATGGTCACTACCAATACCTTGCTCATAAGACGGTCCCAACTCGTAGAATATAAGTAGGACCGTCGTCCTTGGTAAGCCAGGAAGTGGATTAAATAATCGCGTGCCTAGGAAGCTCGACTCGGTGGCGTCATGATGACGG"
print('\n'.join(de_bruijn_graph_from_string(dna, k)))