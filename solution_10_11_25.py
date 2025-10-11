class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        vec = [(-(10**9), 0)]
        for k in sorted(count.keys()):
            vec.append((k, count[k]))
        n = len(vec)
        f = [0] * n
        max_val = 0
        j = 1
        for i in range(1, n):
            while j < i and vec[j][0] < vec[i][0] - 2:
                max_val = max(max_val, f[j])
                j += 1
            f[i] = max_val + vec[i][0] * vec[i][1]
        return max(f[-3:])
