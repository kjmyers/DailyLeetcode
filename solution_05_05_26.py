# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        n = 1
        while cur.next:
            n += 1
            cur = cur.next

        rem = n - k % n
        if rem == 0:
            return head
        
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = head
        
        cur = head
        for _ in range(rem-1):
            cur = cur.next
        ret = cur.next
        cur.next = None

        return ret
