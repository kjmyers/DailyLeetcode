class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ret = 0
        n = len(pref)
        for word in words:
            if pref == word[:n]:
                ret += 1
            
        return ret
