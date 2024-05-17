# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def delete(node):

            if node.left and delete(node.left):
                node.left = None
            if node.right and delete(node.right):
                node.right = None
            
            if not node.left and not node.right and node.val == target:
                return True
            return False
        
        if delete(root):
            return None
        return root
