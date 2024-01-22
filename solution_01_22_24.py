class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        for i in range(1,n+1):
            s.add(i)
        
        ret = [0,0]

        for num in nums:
            if num not in s:
                ret[0] = num
            else:
                s.remove(num)
        
        ret[1] = list(s)[0]

        return ret
