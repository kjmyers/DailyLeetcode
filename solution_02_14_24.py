class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
            
        i = 0
        while nums[i] < 0:
            i += 1
        posPoint = i
        i = 0
        while nums[i] > 0:
            i += 1
        negPoint = i
        
        for cur in range(0,n,2):
            ret[cur] = nums[posPoint]
            ret[cur+1] = nums[negPoint]
            posPoint += 1
            negPoint += 1
            while posPoint < n and nums[posPoint] < 0:
                posPoint += 1
            while negPoint < n and nums[negPoint] > 0:
                negPoint += 1
            


        return ret
