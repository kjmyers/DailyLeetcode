# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        nextQ = deque()

        ret = [root.val]

        while q or nextQ:
            cur = q.popleft()
            
            if cur.left:
                nextQ.append(cur.left)
            if cur.right:
                nextQ.append(cur.right)
            
            if not q and nextQ:
                tot = 0
                for i in nextQ:
                    tot += i.val
                ret.append(tot)
                q.extend(nextQ)
                nextQ = deque()
        return ret.index(max(ret)) + 1
