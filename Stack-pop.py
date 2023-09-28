class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_stack(self):
        temp = self.top
        while temp != None:
            print(temp.value)
            temp = temp.next
            
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node 
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
    def pop(self):
        temp = self.top
        if self.height == 0:
            return None
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    
my_stack = Stack(9)
my_stack.push(22)
my_stack.push(18)
my_stack.push(6)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    1
    2
    3
    4

    Popped node:
    1

    Stack after pop():
    2
    3
    4

"""