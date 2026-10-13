"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = curr = Node(0)
        p1 = head
        copy = {}
        while p1:
            curr.next = Node(p1.val)
            copy[p1] = curr.next
            curr = curr.next
            p1 = p1.next

        p1 = head
        
        while p1:
            copy[p1].next = copy.get(p1.next)
            copy[p1].random = copy.get(p1.random)
            p1 = p1.next

        return dummy.next


