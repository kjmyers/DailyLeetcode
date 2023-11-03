class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur = 1
        ret = []
        
        for t in target:
            ret += ["Push", "Pop"] * (t - cur)
            ret.append("Push")
            cur = t+1
        
        return ret
