# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque()
        q.append(root)
        evenNums = False

        while q:
            if evenNums:
                prevVal = float('inf')
            else:
                prevVal = 0
            
            for _ in range(len(q)):
                cur = q.popleft()
                if evenNums:
                    if cur.val % 2 != 0 or cur.val >= prevVal:
                        return False
                else:
                    if cur.val % 2 == 0 or cur.val <= prevVal:
                        return False
                prevVal = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            evenNums = not evenNums
        return True
