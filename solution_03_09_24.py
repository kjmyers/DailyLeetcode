class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)

        sf = s1.intersection(s2)

        if sf:
            return min(list(sf))
        return -1
