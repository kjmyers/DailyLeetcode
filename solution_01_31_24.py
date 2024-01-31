class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            count = 1
            while s and temperatures[s[-1]] < temperatures[i]:
                p = s.pop()
                ans[p] = i - p
            s.append(i)
        
        return ans
