# Leet Code - QUes 19

class Solution:
    def removeNthFromEnd(self, head, n):
        curr=head
        count=0
        if curr == None:
            return head
        
        while(curr != None):
            curr = curr.next
            count += 1

        if count == n:
            head = head.next
            return head
            
        x = count-n-1
        curr = head

        for _ in range(0, x):
            curr = curr.next
        temp = curr.next
        curr.next = temp.next
        temp.next = None
        return head

