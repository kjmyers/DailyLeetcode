# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfsStart(node, lhead):
            if node is None:
                return False
            if dfs(node, lhead):
                return True

            return dfsStart(node.left, lhead) or dfsStart(node.right, lhead)
        
        def dfs(node, cur):
            if cur is None:
                return True
            if node is None:
                return False
            if node.val != cur.val:
                return False
            return dfs(node.left, cur.next) or dfs(node.right, cur.next)
        if root is None:
            return False
        return dfsStart(root,head)
