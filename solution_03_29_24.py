class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        max_element = max(nums)
        ans = 0
        start = 0
        maxEl = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                maxEl += 1
            while maxEl == k:
                if nums[start] == max_element:
                    maxEl -= 1
                start += 1
            ans += start
        return ans
