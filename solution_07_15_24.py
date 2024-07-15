# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        root = set()

        for parentVal, childVal, left in descriptions:
            if parentVal not in nodes:
                parent = TreeNode(parentVal)
                nodes[parentVal] = parent
                root.add(parent)
            else:
                parent = nodes[parentVal]
            if childVal not in nodes:
                child = TreeNode(childVal)
                nodes[childVal] = child
            else:
                child = nodes[childVal]
            if child in root:
                root.remove(child)
            
            if left:
                parent.left = child
            else:
                parent.right = child

        return root.pop()
