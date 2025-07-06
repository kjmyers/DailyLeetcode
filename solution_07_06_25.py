class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n2 = Counter(nums2)
        self.nums1 = nums1
        self.nums2 = nums2
        

    def add(self, index: int, val: int) -> None:
        self.n2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.n2[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        ret = 0
        for n in self.nums1:
            if tot - n in self.n2:
                ret += self.n2[tot - n]
        
        return ret


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
