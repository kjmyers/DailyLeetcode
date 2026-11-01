class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_v = min(nums)
        ret = 0

        for num in nums:
            ret += num
            min_v = min(min_v, num)
        
        return ret - min_v * len(nums)
