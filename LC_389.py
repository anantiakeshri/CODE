# Leet Code - Ques 389

# TC 1
s = "abcd"
t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.

# TC 2
# s = ""
# t = "y"
# Output: "y"


def findTheDifference(s, t):
        if len(t) > len(s):
            for i in t:
                if t.count(i) > s.count(i):
                    return(i)
                
print(findTheDifference(s, t))