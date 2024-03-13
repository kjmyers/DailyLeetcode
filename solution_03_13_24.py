class Solution:
    def pivotInteger(self, n: int) -> int:
        
        lpre = 1
        rpre = n
        li = 1
        ri = n

        if n == 1:
            return n

        while li < ri:
            if lpre < rpre:
                li += 1
                lpre += li
            else:
                ri -= 1
                rpre += ri
            if lpre == rpre and li + 1 == ri - 1:
                return li + 1
        return -1
