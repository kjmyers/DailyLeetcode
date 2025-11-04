class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)

        ret = []

        for i in range(n-k+1):
            c = Counter(nums[i:i+k])
            freq = sorted(c.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ret.append(xsum)
        return ret
