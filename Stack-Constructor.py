class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_list(self, value):
        temp = Node(value)
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_stack = Stack(4)
print('Top:', my_stack.top.value)
print('Height:', my_stack.height)


"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""