class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num*2)
            if num % 2 == 0:
                seen.add(num//2)
        
        return False
