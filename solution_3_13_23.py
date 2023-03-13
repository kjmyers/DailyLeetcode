# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False


        left = []
        right = []
        
        def dfsL(node):
            left.append(node.val)
            if node.left:
                dfsL(node.left)
            else:
                left.append(None)
            if node.right:
                dfsL(node.right)
            else:
                left.append(None)
        
        def dfsR(node):
            right.append(node.val)
            if node.right:
                dfsR(node.right)
            else:
                right.append(None)
            if node.left:
                dfsR(node.left)
            else:
                right.append(None)
        
        dfsL(root.left)
        dfsR(root.right)

        #print(left)
        #print(right)

        return left == right
            
