class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = Counter(digits)
        ret = []
        for ones in range(0,10,2):
            for tens in range(10):
                for hunds in range(1,10):
                    cur = c.copy()
                    if cur[ones] > 0:
                        cur[ones] -= 1
                    else:
                        continue
                    if cur[tens] > 0:
                        cur[tens] -= 1
                    else:
                        continue
                    if cur[hunds] > 0:
                        cur[hunds] -= 1
                    else:
                        continue
                    ret.append(ones + tens*10 + hunds*100)
        return sorted(ret)
            
