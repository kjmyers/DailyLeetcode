class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ret = n * [0]
        if k == 0:
            return ret
        
        elif k > 0:
            for cur in range(n):
                for i in range(cur+1,cur+1+k):
                    if i >= n:
                        ret[cur] += code[i-n]
                    else:
                        ret[cur] += code[i]
            return ret
        else:
            for cur in range(n):
                for i in range(cur-1,cur-1+k,-1):
                    if i < 0:
                        ret[cur] += code[i+n]
                    else:
                        ret[cur] += code[i]
            return ret
