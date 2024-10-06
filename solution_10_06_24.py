class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        f = 0
        r = 1

        while f < len(s1) and f < len(s2) and s1[f] == s2[f]:
            f += 1
        while (len(s1) - r) > -1 and (len(s2) - r) > -1 and s1[len(s1) - r] == s2[len(s2) - r]:
            r += 1
        
        if f > (len(s1) - r) or f > (len(s2) - r):
            return True
        return False
