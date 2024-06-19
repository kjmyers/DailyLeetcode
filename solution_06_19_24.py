class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        def numBouquets(day):
            ret = 0
            curCount = 0
            for d in bloomDay:
                if d <= day:
                    curCount +=1
                    if curCount == k:
                        ret += 1
                        curCount = 0
                else:
                    curCount = 0
            return ret
        
        
        l = 0
        r = max(bloomDay)
        while l <= r:
            cur = (l + r)//2
            nb = numBouquets(cur)
            if nb >= m:
                r = cur - 1
            else:
                l = cur + 1
        
        return l
