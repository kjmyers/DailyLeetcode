class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = Counter(words[0])
        for i in range(len(words)):
            s &= Counter(words[i])
        
        ret = []
        for l, c in s.items():
            ret += [l] * c

        return ret
