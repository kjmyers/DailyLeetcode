class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        print(ret)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret[j][i] = matrix[i][j]
        
        return ret
