# Striver 1.1 -  input 

userinput = input()

def character_case():
    if userinput.isupper():
        return 1
    elif userinput.islower():
        return 0
    else:
        return -1
    
print(character_case())