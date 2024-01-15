class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        allPlayers = set()
        losers = set()
        loseTwice = set()

        for winner, loser in matches:
            allPlayers.add(winner)
            allPlayers.add(loser)
            if loser in losers:
                loseTwice.add(loser)
            losers.add(loser)
            
        
        ret = [[],[]]
        ret[0] = sorted(list(allPlayers - losers))
        ret[1] = sorted(list(losers - loseTwice))

        return ret
