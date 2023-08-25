class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = {}
        def solve(p1, p2, p3):

            if (p1, p2, p3) in dp:
                return dp[(p1, p2, p3)]

            if p1 == len(s1):
                if s3[p3:] == s2[p2:]:
                    dp[(p1, p2, p3)] = True
                else:
                    dp[(p1, p2, p3)] = False
                return dp[(p1, p2, p3)]
            
            if p2 == len(s2):
                if s3[p3:] == s1[p1:]:
                    dp[(p1, p2, p3)] = True
                else:
                    dp[(p1, p2, p3)] = False
                return dp[(p1, p2, p3)]
            
            if p3 == len(s3):
                dp[(p1, p2, p3)] = False
                return False

            if s1[p1] != s3[p3] and s2[p2] != s3[p3]:
                dp[(p1, p2, p3)] = False
                return False
            
            ret = False
            if s1[p1] == s3[p3]:
                ret = ret or solve(p1+1,p2,p3+1)
            
            if s2[p2] == s3[p3]:
                ret = ret or solve(p1,p2+1,p3+1)
            
            dp[(p1, p2, p3)] = ret
            return ret
        
        return solve(0,0,0)
