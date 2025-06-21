class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = Counter(word)
        ret = len(word)
        
        for a in c.values():
            delete = 0
            for b in c.values():
                if a > b:
                    delete += b
                elif b > a + k:
                    delete += b - (a+k)
            ret = min(ret, delete)
        
        return ret
