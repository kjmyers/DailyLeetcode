class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)

        # compare versions
        for i in range(max(n1, n2)):
            i1, i2 = 0, 0
            if i < n1:
                i1 = int(nums1[i])
            
            if i < n2:
                i2 = int(nums2[i])
            
            if i1 != i2:
                if i1 > i2:
                    return 1
                else:
                    return -1

        # The versions are equal
        return 0
