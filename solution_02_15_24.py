class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        prev = 0
        ret = -1
        for num in nums:
            if num < prev:
                ret = num + prev
            prev += num
        
        return ret
