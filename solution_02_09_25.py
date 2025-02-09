class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        badpairs = 0
        counter = defaultdict(int)

        for i in range(len(nums)):
            diff = i - nums[i]
            goodpairs = counter[diff]

            badpairs += i - goodpairs

            counter[diff] = goodpairs + 1
        
        return badpairs
