class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(2):
            for j in range(2):
                if edges[0][i] == edges[1][j]:
                    return edges[0][i]
