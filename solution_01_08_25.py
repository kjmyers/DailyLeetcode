class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(s1, s2):
            n = len(s1)
            if s1 == s2[:n] and s1 == s2[-n:]:
                return True
            return False
        
        ret = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if i != j and isPrefixAndSuffix(words[i], words[j]):
                    ret += 1
        

        return ret
