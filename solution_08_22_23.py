class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ""

        while columnNumber > 0:
            columnNumber -= 1
            ret = ret + chr(columnNumber % 26 + 65)
            columnNumber //= 26
        
        ret = ret[::-1]
        return ret
