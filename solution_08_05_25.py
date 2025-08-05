class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ret = 0
        for fruit in fruits:
            notfound = 1
            for i,basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[i] = 0
                    notfound = 0
                    break
            ret += notfound
        
        return ret
