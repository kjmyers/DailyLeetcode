# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.ret = 0

        def dfs(node, left, count):
            if node:
                self.ret = max(self.ret, count)
                if left:
                    dfs(node.left, False, count + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, count + 1)
        
        dfs(root, False, 0)
        dfs(root, True, 0)
        return self.ret
