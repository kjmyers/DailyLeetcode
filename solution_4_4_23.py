class Solution:
    def partitionString(self, s: str) -> int:
        curLetters = set()

        ret = 0

        for l in s:
            if l in curLetters:
                curLetters = set()
                ret += 1
            curLetters.add(l)
        
        return ret + 1
