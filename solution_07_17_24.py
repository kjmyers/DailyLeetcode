# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del = set(to_delete)
        ret = []

        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_del:
                if node.left:
                    ret.append(node.left)
                if node.right:
                    ret.append(node.right)
                return None
            return node
        
        root = dfs(root)

        if root:
            ret.append(root)

        return ret
