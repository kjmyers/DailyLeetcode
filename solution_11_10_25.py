class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        ret = 0

        for n in nums:
            if n != 0:
                if not s or n > s[-1]:
                    s.append(n)
                    ret += 1
                else:
                    while s and s[-1] > n:
                        s.pop()
                    if not s or n > s[-1]:
                        s.append(n)
                        ret += 1
            else:
                s = []
        
        return ret
