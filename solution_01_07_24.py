class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = defaultdict(int)
        
        for i in range(1,n):
            for j in range(i):
                delta = nums[i] - nums[j]
                ans += cnt[(j, delta)]
                cnt[(i, delta)] += cnt[(j, delta)] + 1
        
        return ans
