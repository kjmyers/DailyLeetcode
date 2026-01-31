class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        n = len(letters)-1
        lo = 0
        hi = n

        while lo < hi:
            mid = (lo + hi)//2
            
            if ord(target) >= ord(letters[mid]):
                lo = mid+1
            else:
                hi = mid
        
        if (lo == 0 and ord(target) < ord(letters[lo])) or (lo == n and ord(target) >= ord(letters[lo])):
            return letters[0]

        return letters[lo]
