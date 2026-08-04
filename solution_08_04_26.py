class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxV = 0
        minV = 100

        vals = set() #defaultdict(int)
        for num in nums:
            if num < minV:
                minV = num
            if num > maxV:
                maxV = num
            vals.add(num)
        
        ret = []
        for i in range(minV, maxV+1):
            if i not in vals:
                ret.append(i)
        
        return ret
