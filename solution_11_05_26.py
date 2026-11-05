class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ret = 0
        
        for target in arr1:
            i = bisect_left(arr2, target)
            
            if i == len(arr2) or abs(arr2[i] - target) > d:
                if i == 0 or abs(arr2[i-1] - target) > d:
                    ret += 1
        
        return ret
