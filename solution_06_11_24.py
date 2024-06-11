class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)

        ret = []
        for num in arr2:
            ret += [num] * c[num]
            del c[num]
        
        rem = []
        for k,v in c.items():
            rem += [k] * v
        rem.sort()
        
        return ret + rem
