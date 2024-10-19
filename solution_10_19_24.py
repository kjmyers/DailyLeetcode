class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def rec(s, l):
            if l == 0:
                return s
            inv = "".join(["1" if c == "0" else "0" for c in s])
            news = s + "1" + inv[::-1]
            return rec(news, l-1)
        
        ret = rec("0",n-1)
        return ret[k-1]
