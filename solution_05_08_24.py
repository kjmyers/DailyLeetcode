class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        h = []

        for i, n in enumerate(score):
            heappush(h, (-n,i))
        
        count = 1
        while h:
            _ , place = heappop(h)
            if count == 1:
                score[place] = "Gold Medal"
            elif count == 2:
                score[place] = "Silver Medal"
            elif count == 3:
                score[place] = "Bronze Medal"
            else:
                score[place] = str(count)
            count += 1


        return score
