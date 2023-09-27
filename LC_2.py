# Leet Code - Ques 2

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        ans = ListNode(0)
        curr = ans
        carry = 0

        while l1 or l2:
            sum_val = 0
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            sum_val += carry

            curr.next = ListNode(sum_val % 10)
            curr = curr.next
            carry = sum_val // 10

        if carry:
            curr.next = ListNode(carry)

        ans = ans.next
        return ans
