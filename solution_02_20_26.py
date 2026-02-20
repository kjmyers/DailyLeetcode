class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return s
        mounts = []
        anchor = 0
        bal = 0
        for i, x in enumerate(s):
            if x == '1':
                bal += 1
            else: # '0'
                bal -= 1
            if bal == 0:
                mounts.append("1{}0".format(
                    self.makeLargestSpecial(s[anchor+1: i])))
                anchor = i+1
        
        mounts.sort(reverse=True)
        return "".join(mounts)
