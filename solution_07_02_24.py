class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = defaultdict(int)
        for n in nums1:
            d[n] += 1
        
        ret = []
        for n in nums2:
            if n in d:
                d[n] -= 1
                if d[n] == 0:
                    del d[n]
                ret.append(n)
        
        return ret
