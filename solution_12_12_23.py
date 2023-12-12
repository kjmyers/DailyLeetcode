class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = 0

        for n in nums:
            if n  > first:
                second = first
                first = n
            elif n > second:
                second = n
        
        print(first, second)
        return (first - 1) * (second - 1)
