class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        ret = 0
        cur = 0
        l = 0
        uni = set()

        for r in range(len(nums)):
            while nums[r] in uni:
                uni.remove(nums[l])
                cur -= nums[l]
                l += 1
            uni.add(nums[r])
            cur += nums[r]
            ret = max(cur, ret)
        
        return ret
