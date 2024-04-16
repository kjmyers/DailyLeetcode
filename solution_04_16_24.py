# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root: Optional[TreeNode], val: int, depth: int):
        if root == None:
            return
        
        if depth - 2 == 0:
            temp = root.left
            root.left = TreeNode(val)
            root.left.left = temp
            
            temp = root.right
            root.right = TreeNode(val)
            root.right.right = temp
            
        else:
            self.insert(root.left, val, depth-1)
            self.insert(root.right, val, depth-1)
        
        return root
    
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            t = TreeNode(val)
            t.left = root
            return t
        
        self.insert(root, val,depth)
        return root
        
