# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        retHead = ListNode(0)
        ret = retHead
        total = 0
        while fast.next:
            fast = fast.next
            while fast.val != 0:
                total += fast.val
                fast = fast.next
            ret.next = ListNode(total)
            ret = ret.next
            total = 0
        return retHead.next
