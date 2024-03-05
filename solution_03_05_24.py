class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        left = 0
        right = n-1

        while left < right and s[left] == s[right]:
            while left < n-1 and s[left] == s[left+1]:
                left += 1
            while right >= -1 and s[right] == s[right-1]:
                right -= 1
            left += 1
            right -= 1
        if left > right:
            return 0
        return right - left + 1
