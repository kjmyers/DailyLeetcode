# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, value):
            value += str(node.val)
            if not node.left and not node.right:
                return int(value)
            
            ret = 0
            if node.left:
                ret += dfs(node.left, value)
            if node.right:
                ret += dfs(node.right, value)

            return ret
        
        return dfs(root, "")
