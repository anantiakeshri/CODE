# Leet Code - Ques 84

def partition(self, head, x: int):
    dummy1, dummy2 = ListNode(0), ListNode(0)
    prev1 = dummy1
    prev2 = dummy2

    while head:
        if head.val < x:
            prev1.next = head
            prev1 = head
        else:
            prev2.next = head
            prev2 = head
        head = head.next

    # prev1.next = None
    prev2.next = None
    prev1.next = dummy2.next

    return dummy1.next