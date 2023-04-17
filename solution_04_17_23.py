class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)

        n = len(candies)

        ret = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= m:
                ret[i] = True

        return ret
