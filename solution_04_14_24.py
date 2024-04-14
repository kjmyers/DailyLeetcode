# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        ret = 0
        
        def dfs(node, left):
            nonlocal ret

            if not node.left and not node.right and left:
                ret += node.val
            
            if node.left:
                dfs(node.left, True)
            if node.right:
                dfs(node.right, False)
        
        dfs(root, False)
        return ret
