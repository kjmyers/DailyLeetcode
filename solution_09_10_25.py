class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        cn = set()
        for p1,p2 in friendships:
            mp = {}
            c = False
            for l in languages[p1-1]:
                mp[l] = 1
            for l in languages[p2-1]:
                if l in mp:
                    c = True
                    break
            if not c:
                cn.add(p1-1)
                cn.add(p2-1)
        
        ret = 0
        cnt = [0] * (n+1)
        for f in cn:
            for l in languages[f]:
                cnt[l] += 1
                ret = max(ret, cnt[l])
        
        return len(cn) - ret
