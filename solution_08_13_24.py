class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        
        def func(i, curMem, total):
            if total > target:
                return 0
            if total == target:
                ret.append(curMem[:])
                return
            
            for ind in range(i, len(candidates)):
                if ind > i and candidates[ind] == candidates[ind - 1]:
                    continue
                func(ind+1, curMem + [candidates[ind]], total + candidates[ind])
        func(0,[],0)

        return ret
