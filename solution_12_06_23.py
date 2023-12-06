class Solution:
    def totalMoney(self, n: int) -> int:
        div, mod = divmod(n,7)
        ret = 28 * div
        ret += 7 * sum(range(div))
        ret += sum(range(div+1,div+mod+1))

        return ret
