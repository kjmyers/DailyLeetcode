class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        exist = set(nums)
        cur = k
        while cur in exist:
            cur += k
        return cur
