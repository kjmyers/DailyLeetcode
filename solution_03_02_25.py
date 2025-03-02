class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        ret = []

        while p1 < n1 and p2 < n2:
            if nums1[p1][0] == nums2[p2][0]:
                ret.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
            elif nums1[p1][0] < nums2[p2][0]:
                ret.append(nums1[p1])
                p1 += 1
            else:
                ret.append(nums2[p2])
                p2 += 1            
        
        while p1 < n1:
            ret.append(nums1[p1])
            p1 += 1
        while p2 < n2:
            ret.append(nums2[p2])
            p2 += 1

        return ret
