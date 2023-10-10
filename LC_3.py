# Leet Code - Ques 3

s = "pwwkew"
# output - 3

""" Approach 1 """
# def lengthOfLongestSubstring(s: str) -> int:
#     n = len(s)
#     maxLength = 0
#     charSet = set()
#     left = 0
    
#     for right in range(n):
#         if s[right] not in charSet:
#             charSet.add(s[right])
#             maxLength = max(maxLength, right - left + 1)
#         else:
#             while s[right] in charSet:
#                 charSet.remove(s[left])
#                 left += 1
#             charSet.add(s[right])
    
#     return maxLength

# print(lengthOfLongestSubstring(s))

""" Approach 2 - O(n) - Sliding Window Technique"""
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring(s))