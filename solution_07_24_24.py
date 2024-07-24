class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def convert(num):
            ret = ""
            for n in str(num):
                ret += str(mapping[int(n)])
            return int(ret)
        
        return sorted(nums, key=convert)
