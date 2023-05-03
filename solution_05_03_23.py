class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        ret = []
        ret.append((s1 - s2))
        ret.append((s2 - s1))

        return ret
