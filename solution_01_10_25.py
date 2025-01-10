class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ret = []

        letters = defaultdict(int)

        for word in words2:
            curLet = defaultdict(int)
            for l in word:
                curLet[l] += 1
            
            for k in curLet.keys():
                letters[k] = max(letters[k], curLet[k])
                
        for word in words1:
            c = Counter(word)
            addWord = True
            for k,v in letters.items():
                if c[k] < v:
                    addWord = False
                    break
            if addWord:
                ret.append(word)

        return ret
