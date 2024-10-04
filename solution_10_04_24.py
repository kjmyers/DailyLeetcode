class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        tcount = n//2

        chem = [1] * tcount
        tskill = [0] * tcount

        for i in range(tcount):
            chem[i] = skill[i] * skill[n-i-1]
            tskill[i] = skill[i] + skill[n-i-1]
            if i > 0 and tskill[i] != tskill[i-1]:
                return -1
        
        return sum(chem)
