class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = 0
        ret = 0
        current_streak = 0
        for num in nums:
            if max_val < num:
                max_val = num
                ret = 0
                current_streak = 1
            elif max_val == num:
                current_streak += 1
            else:
                current_streak = 0

            ret = max(ret, current_streak)
        return ret
