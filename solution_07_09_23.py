class Solution:
    def largestVariance(self, s: str) -> int:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        
        globalMax = 0

        for i in range(26):
            for j in range(26):
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue

                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                majorCount = 0
                minorCount = 0

                restMinor = counter[j]

                for c in s:
                    if c == major:
                        majorCount += 1
                    if c == minor:
                        minorCount += 1
                        restMinor -= 1
                    
                    if minorCount > 0:
                        globalMax = max(globalMax, majorCount - minorCount)
                    
                    if majorCount < minorCount and restMinor > 0:
                        majorCount = 0
                        minorCount = 0
        
        return globalMax
