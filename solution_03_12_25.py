class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        leftzero = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
                leftzero = mid

        left, right = 0, len(nums) - 1
        rightzero = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
                rightzero = mid

        return max( leftzero, len(nums) - rightzero )
