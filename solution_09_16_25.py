class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
        for num in nums:
            s.append(num)
            while len(s) > 1 and gcd(s[-1],s[-2]) > 1:
                s.append(lcm(s.pop(), s.pop()))
            
        return s
