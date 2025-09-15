class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ret = 0
        broken = set(brokenLetters)
        words = text.split()
        for word in words:
            for l in word:
                if l in broken:
                    ret += 1
                    break
        
        return len(words) - ret
