class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        total = 0
        for num in derived:
            total ^= num
        
        if total == 0:
            return True
        else:
            return False
