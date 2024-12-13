class Solution:
    def findScore(self, nums: List[int]) -> int:
        h = []
        marked = set()
        n = len(nums)
        for i in range(n):
            marked.add(i)

        for i, num in enumerate(nums):
            heappush(h, (num,i))
        score = 0
        while marked:
            num, i = heappop(h)
            if i in marked:
                marked.discard(i)
                score += num
                if i-1 >= 0:
                    marked.discard(i-1)
                if i+1 < n:
                    marked.discard(i+1)
        
        return score
