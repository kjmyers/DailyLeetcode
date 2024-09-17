class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = defaultdict(int)
        for w in s1.split():
            c[w] += 1
        for w in s2.split():
            c[w] += 1
        
        ret = []
        for k,v in c.items():
            if v == 1:
                ret.append(k)

        return ret
