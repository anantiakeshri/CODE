# Leet Code - Question 82

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge case of an empty list or a list with a single node.
        if not head or not head.next:
            return head

        # Create a dummy node to simplify the code.
        dummy = ListNode(0)
        dummy.next = head
        # Initialize pointers for the current node and the previous node.
        prev = dummy
        curr = head
        while curr:
            # Check if the current node has a duplicate value.
            if curr.next and curr.val == curr.next.val:
                # Move curr to the next distinct value.
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  # Remove all duplicates.
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next