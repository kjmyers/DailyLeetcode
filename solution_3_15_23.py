# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        foundNone = False

        while q:
            cur = q.popleft()

            if not cur:
                foundNone = True
            else:
                if foundNone:
                    return False
                q.append(cur.left)
                q.append(cur.right)
        
        return True
