class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curB = 0
        for i in range(k):
            if blocks[i] == "B":
                curB += 1
        
        maxB = curB

        for right in range(k,len(blocks)):
            if blocks[right] == "B":
                curB += 1
            if blocks[right-k] == "B":
                curB -= 1
            maxB = max(curB, maxB)
        
        return k-maxB
