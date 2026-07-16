class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        prefixGcd = [0] * n
        curMax = 0
        for i in range(n):
            curMax = max(curMax, nums[i])
            prefixGcd[i] = gcd(nums[i], curMax)
        
        prefixGcd.sort()
        ret = 0
        for i in range(n//2):
            ret += gcd(prefixGcd[i], prefixGcd[n-i-1])
        
        return ret
