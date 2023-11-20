class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # dCount = {
        #     "M": 0,
        #     "P": 0,
        #     "G": 0
        # }
        ret = 0
        dLast = {
            "M": 0,
            "P": 0,
            "G": 0
        }
        
        for i,h in enumerate(garbage):
            for l in h:
                ret += 1
                dLast[l] = i
        
        for c in dLast.values():
            ret += sum(travel[:c])

        return ret
                
