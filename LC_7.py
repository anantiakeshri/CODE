# Leet Code - Ques 7 - Reverse a Integer

# x = -123
# Output: -321

x = -123
# Output: -321

class Solution:
    def reverse(x):
        if x >= 0:
            val = int(str(x)[::-1])
        else:
            val = -(int(str(abs(x))[::-1]))

        if (val <= -2**31 or val >= 2**31 -1):
            return 0
        else:
            return val
        
        
    print(reverse(x))