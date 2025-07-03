class Solution:
    def kthCharacter(self, k: int) -> str:
        
        def rec(word, k):
            if len(word) > k:
                return word[k-1]
            
            addedChars = []
            for l in word:
                if l == 'z':
                    addedChars.append('a')
                else:
                    addedChars.append(chr(ord(l)+1))
            return rec(word + "".join(addedChars), k)
        
        return rec('a', k)
