class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c = Counter(s)

        odds = 0
        evenpairs = 0
        for v in c.values():
            if v % 2 == 1:
                odds += 1
            evenpairs += v//2
                
        if odds > k or evenpairs*2 + odds < k:
            return False
        else:
            return True
