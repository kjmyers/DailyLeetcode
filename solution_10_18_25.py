class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        nums[0] -= k
        for i in range(1,n):
            nums[i] = min(max(nums[i-1]+1, nums[i] - k), nums[i] + k)
        return len(set(nums))
