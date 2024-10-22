# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        q = deque()
        rowSums = []
        q.append(root)

        while(q):
            curRowSum = 0
            for _ in range(len(q)):
                cur = q.popleft()
                curRowSum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            heappush(rowSums,-curRowSum)
        
        if k > len(rowSums):
            return -1
        for _ in range(k-1):
            heappop(rowSums)

        return -heappop(rowSums)
