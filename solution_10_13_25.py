class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ret = [words[0]]
        prev = "".join(sorted(words[0]))
        for i in range(1, len(words)):
            cur = "".join(sorted(words[i]))
            if cur != prev:
                ret.append(words[i])
            prev = cur
        
        return ret
