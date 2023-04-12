# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        ret = []

        def dfs(node, cur):

            nonlocal ret

            cur = cur + str(node.val)

            if not node.left and not node.right:
                ret.append(int(cur))
            
            if node.left:
                dfs(node.left, cur)
            
            if node.right:
                dfs(node.right, cur)
        

        dfs(root, "")

        return sum(ret)
