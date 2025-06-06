class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        cur = 0
        right = len(nums)-1

        while cur <= right:
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:
                cur += 1
