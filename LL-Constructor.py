class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
my_LL = LinkedList(5)

print('Head:', my_LL.head.value)
print('Tail:', my_LL.tail.value)
print('Length:', my_LL.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 5
    Tail: 5
    Length: 1
    
"""

                                                                                                                    