class Solution:
    def compressedString(self, word: str) -> str:
        ret = ""
        n = len(word)

        start = 0
        while start < n:
            end = start + 1
            while end < n and word[start] == word[end] and end - start < 9:
                end += 1
            ret += str(end - start) + word[start]
            start = end
        
        return ret
