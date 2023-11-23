class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret = []
        for i in range(len(l)):
            curRet = True
            cur = nums[l[i]:r[i]+1]
            cur.sort()
            diff = cur[1] - cur[0]
            for j in range(2,len(cur)):
                if (cur[j] - cur[j-1]) != diff:
                    curRet = False
                    break
            ret.append(curRet)
        
        return ret
