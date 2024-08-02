class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = 0
        for num in nums:
            if num == 1:
                windowSize += 1
        
        windowZeros = 0
        for i in range(windowSize):
            if nums[i] == 0:
                windowZeros +=1
        
        minZeros = windowZeros
        for i in range(windowSize, len(nums)+windowSize):
            if nums[i - windowSize] == 0:
                windowZeros -= 1
            if i >= len(nums):
                ind = i - len(nums)
            else:
                ind = i
            if nums[ind] == 0:
                windowZeros += 1
            minZeros = min(minZeros, windowZeros)
        
        return minZeros
