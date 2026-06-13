class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ret = []
        for word in words:
            total = 0
            for l in word:
                total += weights[ord(l)-97]
            total = total % 26
            
            ret.append(chr((26 - total) + 96))
        
        return "".join(ret)
