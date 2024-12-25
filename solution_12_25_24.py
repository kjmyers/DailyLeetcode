# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ret = [root.val]

        while q:
            maxVal = float('-inf')
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    maxVal = max(maxVal, cur.left.val)
                    q.append(cur.left)
                if cur.right:
                    maxVal = max(maxVal, cur.right.val)
                    q.append(cur.right)
            if maxVal != float('-inf'):
                ret.append(maxVal)

        return ret
