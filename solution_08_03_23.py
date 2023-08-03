class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        n = len(digits)

        digitMap = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        ret = []
        def solve(i, combo):
            if i == n-1:
                for l in digitMap[digits[i]]:
                    ret.append(combo + l)
                return

            for l in digitMap[digits[i]]:
                solve(i+1, combo + l)        
        
        solve(0,"")
        return ret
