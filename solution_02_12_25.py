class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        freq = defaultdict(list)

        for num in nums:
            total = 0
            for c in str(num):
                total += int(c)
            heappush(freq[total], -num)
        
        ret = -1
        for heap in freq.values():
            if len(heap) > 1:
                cur = 0
                for _ in range(2):
                    cur += -heappop(heap)
                ret = max(ret,cur)

        return ret
