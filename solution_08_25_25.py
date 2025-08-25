class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        result = []

        # For all cells on two sides of rectangle
        for d in range(m + n - 1):
            if d < m:
                r = 0
                c = d
            else:
                r = d - m + 1
                c = m - 1
            
            inter = []
            # slide down the diagonal
            while r < n and c > -1:
                inter.append(mat[r][c])
                r += 1
                c -= 1
            
            # Reverse if needed
            if d % 2 == 0:
                result += inter[::-1]
            else:
                result += inter
        
        return result
