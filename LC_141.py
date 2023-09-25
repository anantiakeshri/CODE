# Leet Code - Ques 141

""" TC 1 """
head = [3,2,0,-4]
pos = 1
# Output: true

""" Approach 1 """
def hasCycle(head):
    s = set()
    temp = head
    while(temp):
        if (temp in s):
            return True
        s.add(temp)
        temp = temp.next
    return False


""" Approach 2 """
def hasCycle(head):
    slow = head
    fast = head
    while (slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
