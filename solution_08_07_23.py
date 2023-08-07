class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        firstCol = [x[0] for x in matrix]

        targetRow = bisect_right(firstCol, target) - 1
        targetInd = bisect_left(matrix[targetRow], target)

        return targetInd < len(matrix[0]) and target == matrix[targetRow][targetInd]
