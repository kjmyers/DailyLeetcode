class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        n1 = len(nums1)
        n2 = len(nums2)

        memo = {}

        def cross(i, j):
            if i <= 0 or j <= 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if nums1[i-1] == nums2[j-1]:
                memo[(i,j)] = 1 + cross(i-1, j-1)
            else:
                memo[(i,j)] = max(cross(i-1,j),cross(i, j-1))
            return memo[(i,j)]
        
        return cross(n1,n2)
