# Leet Code - Ques 83

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        hash = set()
        curr = head
        hash.add(head.val)

        while curr.next is not None:
            if curr.next.val in hash:
                curr.next = curr.next.next
            else:
                hash.add(curr.next.val)
                curr = curr.next
        
        return head