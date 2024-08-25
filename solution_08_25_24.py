# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ret = []
        if root.left:
            ret += self.postorderTraversal(root.left)
        if root.right:
            ret += self.postorderTraversal(root.right)
        ret.append(root.val)

        return ret
