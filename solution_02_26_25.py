class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minPre = 0
        maxPre = 0
        pre = 0

        for num in nums:
            pre += num

            minPre = min(minPre, pre)
            maxPre = max(maxPre, pre)
        
        return maxPre - minPre
