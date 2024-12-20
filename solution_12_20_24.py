# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        level = 0

        while q:
            curNodes = []
            for _ in range(len(q)):
                cur = q.popleft()
                curNodes.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            if level % 2 == 1:
                left = 0
                right = len(curNodes) - 1
                while left < right:
                    tmp = curNodes[left].val
                    curNodes[left].val = curNodes[right].val
                    curNodes[right].val = tmp
                    left += 1
                    right -= 1
            level += 1
        
        return root
