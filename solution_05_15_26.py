class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1 or nums[r] > nums[l]:
            return nums[l]
        while l < r:
            m = (l + r) // 2
            if nums[l] < nums[m]:
                l = m
            else:
                r = m
        return nums[l+1]
