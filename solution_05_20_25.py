class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)
        for l, r in queries:
            deltaArray[l] += 1
            deltaArray[r+1] -= 1
        operationCounts = []
        currentOperations = 0

        for i in range(len(deltaArray)-1):
            currentOperations += deltaArray[i]
            if currentOperations < nums[i]:
                return False
        return True
