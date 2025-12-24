class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        cur = 0
        ret = 0
        capacity.sort(reverse=True)
        for c in capacity:
            cur += c
            ret += 1
            if cur >= total:
                return ret
        return ret
