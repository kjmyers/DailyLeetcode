class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)
        
        @functools.cache
        def solve(A):
            if len(A) == 1:
                return True
            return any(solve(cand) for cand in build(A, []))
        
        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)
