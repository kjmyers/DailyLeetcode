class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        lim = len(arr)/4
        ret = 0
        for i in c:
            if c[i] > lim:
                return i
