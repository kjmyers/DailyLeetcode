class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def bt(start, subs):
            if start == len(s):
                return 0
            ret = 0
            for end in range(start+1,len(s)+1):
                if s[start:end] not in subs:
                    subs.add(s[start:end])
                    ret = max(ret, 1+ bt(end,subs))
                    subs.remove(s[start:end])
            return ret
        
        return bt(0,set())
            
