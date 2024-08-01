class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ret = 0
        for d in details:
            if int(d[11:13]) > 60:
                ret += 1
        
        return ret
