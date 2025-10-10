class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        p = energy

        for i in range(n-k-1, -1, -1):
            p[i] += p[i+k]
        
        return max(p)
