class Solution:
    def doesAliceWin(self, s: str) -> bool:
        if any([ v in s for v in 'aeiou']):
            return True
        return False
