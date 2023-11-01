# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        d = defaultdict(int)
        
        def dfs(node):
            d[node.val] += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        
        maxF = max(d.values())
        ret = []
        for k in d:
            if d[k] == maxF:
                ret.append(k)
        
        return ret
