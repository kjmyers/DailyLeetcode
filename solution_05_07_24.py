# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recurse(node):
            ret = node.val * 2
            if node.next:
                ret += recurse(node.next)
            if ret >= 10:
                node.val = ret - 10
                return 1
            node.val = ret
            return 0
        
        extra = recurse(head)
        if extra:
            newNode = ListNode(extra, head)
            return newNode
        return head
