class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret = []

        for num in nums:
            s = []
            while num > 9:
                s.append(num % 10)
                num = num//10
            ret.append(num)
            while s:
                ret.append(s.pop())
        
        return ret
