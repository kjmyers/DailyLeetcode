class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0] * n
        skip = False
        indDeck = 0
        indRes = 0

        deck.sort()
        
        while indDeck < n:
            if result[indRes] == 0:
                if not skip:
                    result[indRes] = deck[indDeck]
                    indDeck += 1
                skip = not skip
            
            indRes = (indRes + 1) % n
        
        return result
