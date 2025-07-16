class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        # Even + even = even
        # Odd + odd = even
        evenCount = 0
        for num in nums:
            if num % 2 == 0:
                evenCount += 1
        ret = max(len(nums) - evenCount, evenCount)

        # Even + odd = odd
        
        count = 0
        parity = 0 #even
        for num in nums:
            if num % 2 == parity:
                count += 1
                parity = (parity + 1) % 2
        
        ret = max(ret, count)

        count = 0
        parity = 1 #odd
        for num in nums:
            if num % 2 == parity:
                count += 1
                parity = (parity + 1) % 2
        
        ret = max(ret, count)

        return ret
