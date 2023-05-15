# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        second = head
        n = 0
        while second:
            second = second.next
            n += 1
        # n is now length of list

        second = head
        for i in range(n - k):
            second = second.next
        
        first = head
        for i in range(k - 1):
            first = first.next
        
        first.val, second.val = second.val, first.val

        return head
