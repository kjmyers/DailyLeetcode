class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        f = []
        r = []
        p = []
        for num in nums:
            if num < pivot:
                f.append(num)
            elif num > pivot:
                r.append(num)
            else:
                p.append(num)

        return f + p + r
