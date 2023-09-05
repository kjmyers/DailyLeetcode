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
        if not head:
            return None

        cur = head
        
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy
            cur = cur.next.next

        old = head
        new = head.next
        
        while old:
            if old.random:
                new.random = old.random.next
            
            old = new.next
            if old:
                new.next = old.next
                new = new.next
        
        return head.next
            
