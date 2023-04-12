class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        n = len(potions)
        
        for i in range(len(spells)):
            left = 0
            right = n

            while left < right:
                mid = (left+right)//2
                if spells[i] * potions[mid] < success:
                    left = mid+1
                else:
                    right = mid
            
            spells[i] = n - left
            print(left)

        return spells
