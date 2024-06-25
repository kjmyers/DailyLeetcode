# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        total = 0
        def rec(node):
            nonlocal total
            if node.right:
                rec(node.right)
            
            node.val += total
            total = node.val

            if node.left:
                rec(node.left)
        
        rec(root)

        return root
