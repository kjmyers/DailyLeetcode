class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        horz = defaultdict(int)
        for _, y in points:
            horz[y] += 1
        ret = 0
        total_sum = 0
        mod = 10**9 + 7
        for p_num in horz.values():
            edge = p_num * (p_num - 1) // 2
            ret = (ret + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod
        return ret
