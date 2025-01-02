class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        presum = [0] * (len(words)+1)
        ret = [0] * len(queries)

        vowels = 'aeiou'
        curSum = 0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                curSum += 1
            presum[i+1] = curSum
        
        for i,(start,end) in enumerate(queries):
            ret[i] = presum[end+1] - presum[start]

        return ret
