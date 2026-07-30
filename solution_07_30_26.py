class Solution:
    def minimumPushes(self, word: str) -> int:
        # c = Counter(word)
        # l = sorted([(count, k) for k,count in c.items()])
        # print(l)
        n = len(word)
        ret = 0
        cur = 1
        while n > 8:
            n -= 8
            ret += 8 * cur
            cur += 1
        ret += n * cur
        return ret
