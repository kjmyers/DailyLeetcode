class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        print(w1.values(), w2.values())
        print(w1.keys(), w2.keys())

        return sorted(w1.values()) == sorted(w2.values()) and sorted(w1.keys()) == sorted(w2.keys())
        
