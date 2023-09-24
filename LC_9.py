# Leet Code - Ques 9

x = -121
# Output: false

""" Approach 1 """
def isPalindrome(x):
    if x < 0:
        return False
    else:
        x_str = str(x)
        i = 0
        j = len(x_str) - 1
        while(i < j):
            if x_str[i] != x_str[j]:
                return False
            i = i + 1
            j = j - 1
        return True
    
# """ Approach 2 """
# def isPalindrome(x):
#     x = str(x)
#     n = x[::-1]
#     if x == n:
#         return True
#     else:
#         False
    
print(isPalindrome(x))