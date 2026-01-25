class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        ret = float('inf')
        for l in range(len(nums)-k+1):
            r = l+k-1
            
            ret = min(ret, nums[r] - nums[l])
        
        return ret
