class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for i, word in enumerate(words):
            s = set(word)
            if x in s:
                ret.append(i)
        
        return ret
