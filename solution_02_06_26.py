class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        r = 0
        ret = n
        for l in range(n):
            while r < n and nums[r] <= nums[l]*k:
                r += 1
            ret = min(ret, n-(r-l))
        
        return ret
