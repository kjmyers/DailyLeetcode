# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.ret = float('inf')

        def dfs(node, mini, maxi):
            self.ret = min(self.ret, node.val - mini, maxi - node.val)
            if node.left:
                dfs(node.left, mini, node.val)
            if node.right:
                dfs(node.right, node.val, maxi)
        
        if root.left:
            dfs(root.left, float('-inf'), root.val)
        if root.right:
            dfs(root.right, root.val, float('inf'))

        return self.ret
