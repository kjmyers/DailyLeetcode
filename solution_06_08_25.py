class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []

        def rec(cur):
            if cur > n:
                return
            ret.append(cur)
            rec(cur*10)
            if (cur+1) % 10:
                rec(cur+1)
        
        rec(1)
        return ret
