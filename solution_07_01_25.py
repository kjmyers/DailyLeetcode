class Solution:
    def possibleStringCount(self, word: str) -> int:
        ret = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                ret += 1
        
        return ret
