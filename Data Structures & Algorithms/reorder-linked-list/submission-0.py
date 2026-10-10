# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1, l2 = head, head

        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        temp = l1.next
        l1.next = None
        prev = None
        curr = temp
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2


        