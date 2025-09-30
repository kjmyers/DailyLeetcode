class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        a = [0] * (n-1)

        for step in range(n-1):
            for i in range(n-step-1):
                a[i] = (nums[i] + nums[i+1]) % 10
            nums = a
        
        return nums[0]
