class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        comb = list(zip(heights,names))
        comb.sort(reverse=True)

        return [n for _,n in comb]
