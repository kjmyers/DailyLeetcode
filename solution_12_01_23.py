class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:       
        w1, w2 = 0, 0
        p1, p2 = 0, 0

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][p1] != word2[w2][p2]:
                return False
            
            p1 += 1
            if p1 == len(word1[w1]):
                w1 += 1
                p1 = 0
            p2 += 1
            if p2 == len(word2[w2]):
                w2 += 1
                p2 = 0
        
        return w1 == len(word1) and w2 == len(word2)
