class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        s = Counter()
        l = 0
        ret = 0
        for r in range(len(nums)):
            s[nums[r]] += 1
            while len(s) == distinct:
                s[nums[l]] -= 1
                if s[nums[l]] == 0:
                    del s[nums[l]]
                l += 1
            ret += l
        return ret
