class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        len1 = len(str1)
        len2 = len(str2)
        if len2 > len1:
            return False
        
        p2 = 0
        
        def getNextLetter(letter):
            if letter == 'z':
                return 'a'
            return chr(ord(letter)+1)

        for p1 in range(len1):
            if str1[p1] == str2[p2] or getNextLetter(str1[p1]) == str2[p2]:
                p2 += 1
                if p2 == len2:
                    return True
        
        return False
