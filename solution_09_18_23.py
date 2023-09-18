class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        z = sorted(list(zip([sum(r) for r in mat],[i for i in range(len(mat))])))
        return [z[i][1] for i in range(k)]
