class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        longest = -1

        for i in range(n):
            curLen = 1
            curVal = nums[i] ** 2
            while curVal <= nums[-1]:
                nextInd = bisect_left(nums, curVal)
                if nums[nextInd] != curVal:
                    break
                else:
                    curVal = curVal ** 2
                    curLen += 1
            if curLen > 1:
                longest = max(longest, curLen)
        
        return longest
