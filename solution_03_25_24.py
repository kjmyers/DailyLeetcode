class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = set()
        ret = []
        for n in nums:
            if n in d:
                ret.append(n)
            else:
                d.add(n)
        
        return ret
