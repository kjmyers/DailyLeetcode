class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nextVal = []
        heappush(nextVal,1)
        nums = []
        seen = set()
        while len(nums) != n:
            cur = heappop(nextVal)
            if cur not in seen:
                seen.add(cur)
                heappush(nextVal, cur*2)
                heappush(nextVal, cur*3)
                heappush(nextVal, cur*5)
                nums.append(cur)
        
        return nums[-1]
