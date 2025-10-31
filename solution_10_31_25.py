class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        seen = set()

        for num in nums:
            if num in seen:
                ret.append(num)
                if len(ret) == 2:
                    return ret
            else:
                seen.add(num)
