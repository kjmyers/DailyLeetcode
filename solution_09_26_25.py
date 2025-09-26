class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ret = 0
        print(nums)
        for first in range(n-2):
            third = first + 2
            if nums[first] != 0:
                for second in range(first+1,n-1):
                    while third < n and ((nums[first] + nums[second]) > nums[third]):
                        third += 1
                    ret += third - second - 1
        
        return ret
