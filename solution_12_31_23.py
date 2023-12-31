class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        start = [-1] * 26
        longest = -1

        for i in range(len(s)):
            val = ord(s[i]) - 97
            if start[val] != -1:
                longest = max( longest, i - start[val] - 1 )
            else:
                start[val] = i
        
        return longest
