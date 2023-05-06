class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        ret = 0
        n = len(nums)
        mod = 10 ** 9 + 7
        nums.sort()

        for l in range(n):
            r = bisect_right(nums, target - nums[l]) - 1
            if r >= l:
                ret += pow(2, r-l, mod)
        
        return ret % mod
