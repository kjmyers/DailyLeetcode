class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nondiv = int(n*(n+1)/2)

        div = 0
        for i in range(m,n+1,m):
            div += i
            nondiv -= i
        
        return nondiv - div
