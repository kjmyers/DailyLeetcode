# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        left = {}
        self.ret = 0
        def dfs(node, level = 0, pos = 0):
            if node:
                if level not in left:
                    left[level] = pos
                
                self.ret = max(self.ret, pos - left[level] + 1)
                
                dfs(node.left, level + 1, pos * 2)
                dfs(node.right, level + 1, pos * 2 + 1)
        
        dfs(root)
        return self.ret
