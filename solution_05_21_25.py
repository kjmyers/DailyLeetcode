class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zrows = set()
        zcols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zrows.add(i)
                    zcols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zrows or j in zcols:
                    matrix[i][j] = 0
