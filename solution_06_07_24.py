class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            curT = trie
            for l in word:
                if l not in curT:
                    curT[l] = {}
                curT = curT[l]
            curT['end'] = word
        # print(trie)

        def checkTrie(tr, word, i):
            if 'end' in tr:
                return (True, tr['end'])
            if i < len(word) and word[i] in tr:
                return checkTrie(tr[word[i]], word, i+1)
            return (False, '')
        
        #checkTrie(trie, "att", 0)
        ret = ""
        for w in sentence.split(' '):
            b, sub = checkTrie(trie, w, 0)
            if b:
                ret += sub + " "
            else:
                ret += w + " "

        
        return ret[:-1]
