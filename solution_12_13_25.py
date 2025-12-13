class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        d = {
            'electronics' : [],
            'grocery' : [],
            'pharmacy' : [],
            'restaurant' : []
        }

        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if not c:
                continue
            if not all([l.isalnum() or l == '_' for l in c]):
                continue
            if b not in ('electronics', 'grocery', 'pharmacy', 'restaurant'):
                continue
            d[b].append(c)
        
        d['electronics'].sort()
        d['grocery'].sort()
        d['pharmacy'].sort()
        d['restaurant'].sort()
        
        return d['electronics'] + d['grocery'] + d['pharmacy'] + d['restaurant']
