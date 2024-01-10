# 567. Permutation in String

from collections import Counter
 
s1 = "ab" 
s2 = "eidbaooo"

def checkInclusion(s1, s2):
    s1_map = Counter(s1)
    s2_map = Counter()

    if len(s1) > len(s2):
        return False

    for i in range(len(s2)):
        s2_map[s2[i]] += 1
        if i >= len(s1):
            if s2_map[s2[i - len(s1)]] > 1:
                s2_map[s2[i - len(s1)]] -= 1                    
            else:
                del s2_map[s2[i - len(s1)]]
        if s1_map == s2_map:
            return True 

    return False
    
print(checkInclusion(s1, s2))