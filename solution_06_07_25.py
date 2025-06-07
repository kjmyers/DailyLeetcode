class Solution:
    def clearStars(self, s: str) -> str:

        h = []
        ret = list(s)
        
        for i, c in enumerate(s):
            if h and c == '*':
                _, cur = heappop(h)
                ret[-cur] = ''
                ret[i] = ''
            else:
                heappush(h, (c,-i))
        return ''.join(ret)
