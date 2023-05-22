class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = list(c.items())
        l.sort(key=lambda tup: tup[1], reverse=True)

        ret = []

        for i in range(k):
            ret.append(l[i][0])


        return ret
