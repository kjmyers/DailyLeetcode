class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        c = Counter(letters)
        ret = 0

        def backtrack(i, total):
            nonlocal ret
            if i >= len(words):
                #print(ret, total)
                ret = max(ret, total)
                return
            
            #Don't use word
            backtrack(i+1, total)
            
            # Check if we can use this word
            cur_c = Counter(words[i])
            for l, count in cur_c.items():
                if c[l] - count < 0:
                    return # Can't use this word
            
            # We can use it:
            for l, count in cur_c.items():
                c[l] -= count
                total += (score[ord(l) - 97] * count)
                #print(total)
            
            backtrack(i+1, total)

            for l, count in cur_c.items():
                c[l] += count
            

        backtrack(0,0)
        return ret
