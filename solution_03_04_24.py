class Solution:
    
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        deque = collections.deque(tokens)
        ret = 0
        bns = 0
        
        while deque and (power >= deque[0] or bns):
            while deque and power >= deque[0]:
                power -= deque.popleft()
                bns += 1
            ret = max(ret, bns)
            
            if deque and bns:
                power += deque.pop()
                bns -= 1
        return ret
