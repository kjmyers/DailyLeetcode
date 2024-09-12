class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)

        ret = 0
        for w in words:
            null_set = set()
            if set(w) - s == null_set:
                ret += 1
        
        return ret
