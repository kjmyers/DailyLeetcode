class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = []

        def backtrack(i, cur, ret):
            if i >= len(nums):
                ret.append(cur[:])
                return
            
            cur.append(nums[i])
            backtrack(i+1, cur, ret)
            
            cur.pop()
            backtrack(i+1, cur, ret)

        backtrack(0, [], ret)
        return ret
