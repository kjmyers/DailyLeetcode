class Solution:
    def countVowelPermutation(self, n: int) -> int:
        map = {
            '.': ['a', 'e', 'i', 'o', 'u'],
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        @lru_cache(None)
        def dp(i, last):
            if i == n: return 1
            ans = 0
            for nxt in map[last]:
                ans = (ans + dp(i + 1, nxt)) % 1_000_000_007
            return ans

        return dp(0, '.')
