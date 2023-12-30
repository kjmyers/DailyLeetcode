class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = defaultdict(int)
        for w in words:
            for l in w:
                d[l] += 1
        
        n = len(words)
        for l in d.values():
            if (l % n) != 0:
                return False
        
        return True
