class Solution:
    def countLargestGroup(self, n: int) -> int:
        g = defaultdict(int)

        for num in range(1,n+1):
            curSum = sum([int(dig) for dig in str(num)])
            g[curSum] += 1
        
        maxValue = max(g.values())
        c = Counter(g.values())
        return c[maxValue]
