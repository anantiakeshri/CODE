# Leet Code - Ques 316

s = "cbacdcbc"
# Output: "acdb"

def removeDuplicateLetters(s: str) -> str:
    # Initialize a stack to build the result.
    stack = []
    # Initialize a set to keep track of characters in the stack.
    hash = set()
    # Create a dictionary to store the last index of each character in the string.
    last_occ = {char: i for i, char in enumerate(s)}


    for i, char in enumerate(s):
        if char not in hash:
            # If the character is not in the stack and the last occurrence of the character
            # is greater than the current index, pop characters from the stack until conditions are met.
            while stack and char < stack[-1] and i < last_occ[stack[-1]]:
                hash.discard(stack.pop())
            # Add the current character to the stack and the set.
            hash.add(char)
            stack.append(char)
            
    # Convert the stack to a string to get the final result.
    return ''.join(stack)

print(removeDuplicateLetters(s))