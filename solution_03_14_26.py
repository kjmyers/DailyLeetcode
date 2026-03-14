class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        
        allstr = []
        def back(s, l):
            if len(s) == l:
                allstr.append(s)
                return
            if not s or s[-1] != 'a':
                back(s+'a', l)
            if not s or s[-1] != 'b':
                back(s+'b', l)
            if not s or s[-1] != 'c':
                back(s+'c', l)
        
        back('', n)
        allstr.sort()

        if k > len(allstr):
            return ""

        return allstr[k-1]
