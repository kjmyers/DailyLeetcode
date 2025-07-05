class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)

        ret = -1
        for k,v in c.items():
            if k == v:
                ret = max(ret, k)
        
        return ret
