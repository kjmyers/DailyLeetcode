class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pre = 0
        ret = 0

        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            pre = (pre + num % k + k) % k

            ret += modGroups[pre]
            modGroups[pre] += 1
        
        return ret
