class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            d = set()
            for i in range(1,floor(sqrt(num))+1):
                if num % i == 0:
                    d.add(num//i)
                    d.add(i)
                if len(d) > 4:
                    break
            if len(d) == 4:
                ret += sum(d)
        
        return ret
            
