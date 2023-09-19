# Coding Ninjas - 1.1.2 - Data Types

from typing import *

def dataTypes(type: str):

    if(type == "Long"): 
        return 8
    elif( type == "Double"): 
        return 8
    elif(type == "Character"):
        return 1
    elif(type == "Float"):
        return 4
    elif(type == "Integer"):
        return 4

result = dataTypes(type)
    
if result is not None:
    print(result)
