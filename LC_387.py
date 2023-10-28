# Leet code - Ques 387 - First Unique Character

s = "loveleetcode"
# output - 2 : TC 2

""" Approach 1 """
def firstUniqChar(s: str) -> int:
    for i, c in enumerate(len(s)):
        if s.count(c) == 1:
            return i
        
    return -1

print(firstUniqChar(s))

""" Approach 2 """
# def firstUniChar(s:str) -> int:
#     set = Counter(s)
#         for i in range(len(s)):
#             if set[s[i]] == 1:
#                 return i

#         return -1
            
# s = "leetcode"
# output - 0 : TC 1

# s = "aabb"
# output - -1 : TC 3