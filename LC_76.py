# Minimum Windown Substring

s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"


def minWindow(str1: str, str2: str) -> str:
    if len(str1) < len(str2):
        return ""

    # using hashmaps
    countT, window = {}, {}

    for c in str2:
        countT[c] = 1 + countT.get(c, 0)
        # counting chars in str2 

    result = [-1,-1] # this is to save the result pointers
    resLen = float("infinity")
    have , need = 0 , len(countT)
    # these variable are used to check if met the result or not 

    l = 0 # left pointer, r is right pointer 
    for r in range(len(str1)):
        chr = str1[r] # character from str1 
        # add this in hashmap ie window
        window[chr] = 1 + window.get(chr, 0)

        if chr in countT and window[chr] == countT[chr]:
            have += 1
        
        # now if have == need means we got the result then we 
        # start decreasing the result to get min from left side of result

        while have == need:
            # update the result 
            if (r - l + 1) < resLen:
                result = [l, r]
                resLen = (r - l + 1)
            
            # decrease the length of the result, also we use while above 
            # if after decreasing the length of result from left side and have is same 
            # as need then we can update the result as we have to return min length

            window[str1[l]] -= 1

            # now checking if the character we removed is in need too
            # then we have decrease the count of have as well to maintain it

            if str1[l] in countT and window[str1[l]] < countT[str1[l]]:
                have -= 1
            l += 1
        
    l, r = result
    return str1[l:r+1] if resLen != float("infinity") else ""

print(minWindow(s, t))