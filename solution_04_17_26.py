class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = defaultdict(int)

        def reverse(val) -> int:
            return int(str(val)[::-1])

        ret = len(nums)
        for i, num in enumerate(nums):
            if num in d:
                ret = min(ret, i - d[num])
            d[reverse(num)] = i
        
        if ret == len(nums):
            return -1
        return ret
