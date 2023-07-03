class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        n = len(s)

        if n != len(goal):
            return False
        
        if s == goal:
            frequency = [0] * 26
            for ch in s:
                frequency[ord(ch) - ord('a')] += 1
                if frequency[ord(ch) - ord('a')] == 2:
                    return True
            return False
        

        firstIndex = -1
        secondIndex = -1

        for i in range(n):
            if s[i] != goal[i]:
                if firstIndex == -1:
                    firstIndex = i
                elif secondIndex == -1:
                    secondIndex = i
                else:
                    # We have at least 3 indices with different characters,
                    # thus, we can never make the strings equal with only one swap.
                    return False

        if secondIndex == -1:
            # We can't swap if the character at only one index is different.
            return False

        # All characters of both strings are the same except two indices.
        return s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]
