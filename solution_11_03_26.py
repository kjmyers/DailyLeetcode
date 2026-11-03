class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_v = max(nums)
        ret = 0
        for num in nums:
            ret += max_v - num
        
        return ret
