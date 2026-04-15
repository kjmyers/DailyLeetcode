class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ret = n + 1
        for i, word in enumerate(words):
            if word == target:
                ret = min(
                    ret,
                    abs(i - startIndex),
                    n - abs(i - startIndex))
        if ret == n + 1:
            return -1
        return ret
