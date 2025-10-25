class Solution:
    def totalMoney(self, n: int) -> int:
        curStartAdd = 0
        ret = 0
        for i in range(n):
            if i % 7 == 0:
                curStartAdd += 1
            ret += curStartAdd + (i % 7)
        return ret
