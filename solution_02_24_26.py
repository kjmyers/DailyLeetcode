# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curVal):
            curVal = (curVal << 1) + node.val
            total = 0
            if not node.left and not node.right:
                #leaf
                return curVal
            if node.left:
                total += dfs(node.left, curVal)
            if node.right:
                total += dfs(node.right, curVal)
            return total
        
        return dfs(root, 0)
