# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal ret
            left = 1
            right = 1

            left = dfs(node.left)
            right = dfs(node.right)

            ret = max(ret, left+right)

            return max(left, right) + 1
        
        dfs(root)

        return ret
