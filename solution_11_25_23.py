class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = sum(nums[1:])
        ret = [0] * n

        for i in range(n):
            ret[i] += i * nums[i] - left
            ret[i] += right - (n-i-1) * nums[i]
            left += nums[i]
            if i < n-1:
                right -= nums[i+1]

        return ret
