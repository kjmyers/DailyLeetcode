class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)

        one_cnt = c.get(1, 0)
        ret = one_cnt if one_cnt % 2 else one_cnt - 1
        c.pop(1, None)

        for num in nums:
            cur = 0
            x = num
            while x in c and c[x] > 1:
                cur += 2
                x *= x
            ret = max(ret, cur + (1 if x in c else -1))
        
        return ret
