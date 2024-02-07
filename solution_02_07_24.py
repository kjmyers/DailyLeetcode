class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        n = [(count, val) for val, count in c.items()]
        n.sort(reverse=True)
        ret = ""
        for num, l in n:
            ret += num * l
        return ret
