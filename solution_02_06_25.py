class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                freq[nums[i] * nums[j]] += 1
        
        ret = 0

        for freq in freq.values():
            pairs = ( (freq - 1) * freq // 2 )
            ret += 8 * pairs

        return ret
