class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = list(Counter(arr).values())
        c.sort()
        cur = 0
        for i in range(k):
            c[cur] -= 1
            if c[cur] == 0:
                cur += 1

        return len(c) - cur
