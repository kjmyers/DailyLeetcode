# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ret = 0

        def dfs(node):
            nonlocal ret
            count = 1
            sumNodes = node.val
            if node.left:
                temp = dfs(node.left)
                count += temp[0]
                sumNodes += temp[1]
            if node.right:
                temp = dfs(node.right)
                count += temp[0]
                sumNodes += temp[1]
            if math.floor(sumNodes / count) == node.val:
                ret += 1
            return (count, sumNodes)

        dfs(root)

        return ret
