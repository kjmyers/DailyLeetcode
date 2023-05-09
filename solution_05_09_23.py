class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0) # top row

            if matrix and matrix[0]:
                for line in matrix:
                    result.append(line.pop()) #right side

            if matrix:
                result += matrix.pop()[::-1] #Bottom

            if matrix and matrix[0]:
                for line in matrix[::-1]:
                    result.append(line.pop(0))
        return result
