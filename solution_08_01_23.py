class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.ret = []
        self.cur = []

        def solve(valsLeft):
            start = self.cur[-1]+1 if self.cur else 1

            if valsLeft == 0:
                self.ret.append(self.cur[:])
                return

            
            for i in range(start, n+1):
                self.cur.append(i)
                solve(valsLeft-1)
                self.cur.pop()
        
        solve(k)
        return self.ret
