class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        n = len(nums)

        d = defaultdict(set)

        for j in range(n):
            for i in range(0, j):
                d[(j, nums[j] - nums[i])] = d.get((i, nums[j] - nums[i]), 1) + 1
        
        return max(d.values())
