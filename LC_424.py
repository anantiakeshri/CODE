# Longest repeating character replacement - LC 424
# TC - O(26.n)

s = "AABABBA"
k = 1
# Output: 4

def characterReplacement(s, k):
    count = {}
    res = 0
    l = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
    return res

print(characterReplacement(s, k))