class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        d = defaultdict(list)
        for k,v in freq.items():
            d[v].append(k)
        
        l = []
        for k,v in d.items():
            l.append((k,v))
        l.sort()

        ret = []
        for f, values in l:
            values.sort(reverse=True)
            for v in values:
                ret += [v] * f

        return ret
