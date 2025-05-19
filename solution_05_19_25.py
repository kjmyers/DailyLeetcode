class Solution:
    def triangleType(self, nums: List[int]) -> str:
        d = defaultdict(int)

        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return "none"

        for side in nums:
            d[side] += 1
        
        if len(d) == 3:
            return "scalene"
        elif len(d) == 2:
            return "isosceles"
        else:
            return "equilateral"
