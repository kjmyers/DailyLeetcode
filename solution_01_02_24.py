class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = dict(Counter(nums))
        ret = []

        while any(v > 0 for v in c.values()):
            cur = []
            for k in c.keys():
                if c[k] > 0:
                    cur.append(k)
                    c[k] -= 1
            ret.append(cur)
            
            
        

        return ret
