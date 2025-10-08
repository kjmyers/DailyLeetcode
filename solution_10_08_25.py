class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        ret = []
        for spell in spells:
            #normalize and compare as normal for bisect
            ret.append(len(potions) - bisect_left(potions, (success + spell - 1) // spell))
        return ret
