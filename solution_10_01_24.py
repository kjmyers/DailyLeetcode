class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        s = defaultdict(int)

        for v in arr:
            rem = v % k
            if rem == 0 and 0 in s:
                s[0] -= 1
                if s[0] == 0:
                    del s[0]
            elif k - rem in s:
                s[k-rem] -= 1
                if s[k-rem] == 0:
                    del s[k-rem]
            else:
                s[rem] += 1
        return s == {}
