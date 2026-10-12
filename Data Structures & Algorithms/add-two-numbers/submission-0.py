# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = curr = ListNode()

        p1, p2 = l1, l2

        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            res = v1 + v2 + carry
            digit = res % 10 
            carry = res // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if carry:
            curr.next = ListNode(carry)
            

        return dummy.next


