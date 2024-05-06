# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dummy = None
        ret = None

        def solve(node):
            nonlocal ret
            if not node:
                return 0
            
            forwardMax = solve(node.next)
            if forwardMax > node.val:
                return forwardMax
            
            node.next = ret
            ret = node
            return node.val
        
        solve(head)

        return ret
