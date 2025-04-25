class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        pre = 0
        ret = 0
        g = defaultdict(int)
        g[0] += 1
        for num in nums:
            if num % modulo == k:
                pre += 1
            ret += g[(pre - k + modulo) % modulo]
            g[pre % modulo] += 1     
        
        return ret
