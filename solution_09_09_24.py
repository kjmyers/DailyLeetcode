# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        result = []
        matrix = [[-1] * n for _ in range(m)]
        i,j = 0,0
        cur_d = 0
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while head:
            matrix[i][j] = head.val
            newi = i + movement[cur_d][0]
            newj = j + movement[cur_d][1]

            if (min(newi, newj) < 0 or newi >= m or newj >= n or matrix[newi][newj] != -1):
                cur_d = (cur_d + 1) % 4
            i += movement[cur_d][0]
            j += movement[cur_d][1]

            head = head.next
        
        return matrix
