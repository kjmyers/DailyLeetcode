class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        ret = []
        limit = (len(nums)//3)+1 if len(nums)//3 > 0 else 1
        
        for n in nums:
            d[n] += 1
            if d[n] == limit:
                ret.append(n)
        
        return ret
