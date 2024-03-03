# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        findEnd = head
        length = 0
        while findEnd:
            findEnd = findEnd.next
            length += 1
        
        node_del = length - n
        if node_del == 0:
            return head.next
        
        i = 0
        cur = head
        while i < node_del - 1:
            i += 1
            cur = cur.next
        cur.next = cur.next.next

        return head
