# Leet Code - 20

# s = '{)'
# #Output - True

s = '({[]})'
# # return True

def isValid(s: str) -> bool:
    stk = []
    for ch in s:
        if not stk:
            stk.append(ch)
        elif stk[-1] == '(' and ch == ')':
            stk.pop()
        elif stk[-1] == '{' and ch == '}':
            stk.pop()
        elif stk[-1] == '[' and ch == ']':
            stk.pop()
        else:
            stk.append(ch)
    if not stk:
        return True
    return False

print(isValid(s))

"""
Approach for this Problem :

1 - Initialize an empty stack called "stk".
2 - Iterate through each character "ch" in the input string "s".
3 - If the stack is empty, push the current character "ch" onto the stack.
4 - If the top of the stack is an opening parenthesis and the current character "ch" is a corresponding closing parenthesis 
    (i.e. '(' and ')' or '{' and '}' or '[' and ']'), pop the top of the stack.
5 - If neither of the above conditions are met, push the current character "ch" onto the stack.
6 - After the iteration, if the stack is empty, return true as all parenthesis have been matched and balanced. 
    If the stack is not empty, return false as there are unmatched parenthesis.

"""