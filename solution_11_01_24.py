class Solution:
    def makeFancyString(self, s: str) -> str:
        retL = [s[0]]

        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                if count < 3:
                    retL.append(s[i])
            else:
                count = 1
                retL.append(s[i])

        return "".join(retL)
