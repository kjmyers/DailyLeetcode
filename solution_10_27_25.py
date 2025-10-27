class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ret = 0
        prev = 0
        
        for i in range(len(bank)):
            cur = (Counter(bank[i]))["1"]
            if cur != 0:
                ret += cur * prev
                prev = cur
        
        return ret
