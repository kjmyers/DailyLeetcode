class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)

        if length == 1 and not flowerbed[0]:
            return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n < 1:
                return True
        
        for i in range(1, length - 1):
            if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
                if n < 1:
                    return True
        
        if flowerbed[length-1] == 0 and flowerbed[length - 2] == 0:
            flowerbed[0] = 1
            n -= 1
            if n < 1:
                return True
        
        return False
