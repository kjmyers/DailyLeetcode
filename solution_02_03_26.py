class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        p = 1
        if nums[p] <= nums[p-1]:
            return False
        while p < n-1 and nums[p] > nums[p-1]:
            p += 1
        if p > n-2:
            return False
        
        while p < n-1 and nums[p] < nums[p-1]:
            p += 1
        if p == n:
            return False
        
        for i in range(p,n):
            if nums[i] <= nums[i-1]:
                return False
        
        return True
