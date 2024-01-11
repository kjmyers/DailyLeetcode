# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, maxSeen, minSeen):
            if not node:
                return 0
            if node.val > maxSeen:
                maxSeen = node.val
            elif node.val < minSeen:
                minSeen = node.val
            
            if not node.left and not node.right:
                return maxSeen - minSeen
            
            return max(dfs(node.left, maxSeen, minSeen), dfs(node.right, maxSeen, minSeen))
        
        return dfs(root, root.val, root.val)
