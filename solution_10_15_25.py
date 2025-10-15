class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        cur = 1
        prev = 0
        ret = 0
        for i in range(1,n):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                prev = cur
                cur = 1
            ret = max(ret, min(prev,cur), cur//2)
        
        return ret
