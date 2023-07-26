class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def possibleSpeed(speed):
            total = 0
            for d in dist:
                total = ceil(total)
                total += d/speed
                if total > hour:
                    return False
            return True


        l = 1
        r = 10**7
        
        while l < r:
            mid = l + (r-l)//2
            if possibleSpeed(mid):
                r = mid
            else:
                l = mid+1
        
        if possibleSpeed(l):
            return l
        else:
            return -1
