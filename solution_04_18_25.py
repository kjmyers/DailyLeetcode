class Solution:
    def countAndSay(self, n: int) -> str:
        def mapPairs(s):
            cur = 0
            count = 1
            ret = []
            
            for i in range(1,len(s)):
                if s[cur] != s[i]:
                    ret.append((int(s[cur]),count))
                    count = 1
                    cur = i
                else:
                    count += 1
            ret.append((int(s[cur]),count))
            
            return ret
        
        def makeInt(a):
            ret = ""
            for i,j in a:
                ret += str(j) + str(i)
            return ret
        
        cur = "1"
        for i in range(n-1):
            cur = makeInt(mapPairs(cur))
        return cur
