class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = float('inf')
        # get prefix sum for nums
        cum = [0] * len(nums) + [0]
        cum[0] = 0
        
        for i in range(1, len(cum)):
            cum[i] = cum[i-1] + nums[i-1]
        
        for le, v in enumerate(cum):
            # use binary search to locate 'ri' index
            ri = bisect.bisect_left(cum, v + target)
            if ri < len(cum):
                ret = min(ret, ri - le)
        
        return 0 if ret == float('inf') else ret 
