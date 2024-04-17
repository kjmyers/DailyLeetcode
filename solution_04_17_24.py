# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, s):
            if not node.left and not node.right:
                return chr(node.val + 97) + s
            

            if node.left and not node.right:
                ret = dfs(node.left, chr(node.val + 97) + s)
            elif node.right and not node.left:
                ret = dfs(node.right, chr(node.val + 97) + s)
            else:
                ret = min(dfs(node.left, chr(node.val + 97) + s), dfs(node.right, chr(node.val + 97) + s))


            return ret
        
        return dfs(root,"")
