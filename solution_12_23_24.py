# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinSwaps(self, original: list) -> int:
        swaps = 0
        target = sorted(original)

        # Map to track current positions of values
        pos = {val: idx for idx, val in enumerate(original)}

        # For each position, swap until correct value is placed
        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1

                # Update position of swapped values
                cur_pos = pos[target[i]]
                pos[original[i]] = cur_pos
                original[cur_pos] = original[i]

        return swaps
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        ret = 0

        while q:
            vals = []
            n = len(q)
            
            for _ in range(n):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret += self.getMinSwaps(vals)
        
        return ret
