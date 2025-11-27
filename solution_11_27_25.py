class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = 0
        ret = float("-inf")
        kSum = [float("inf")] * k
        kSum[k-1] = 0
        for i in range(n):
            pre += nums[i]
            ret = max(ret, pre - kSum[i%k])
            kSum[i%k] = min(kSum[i%k], pre)
        return ret
