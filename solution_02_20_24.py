class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)+1):
            s.add(i)
        
        for n in nums:
            s.remove(n)
        
        return s.pop()
