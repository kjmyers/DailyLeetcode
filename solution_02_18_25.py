class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ret = []
        stack = []

        for i in range(len(pattern)+1):
            stack.append(i+1)

            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    ret.append(str(stack.pop()))
        
        return "".join(ret)
