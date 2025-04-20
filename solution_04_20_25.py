class Solution(object):
    def numRabbits(self, answers):
        count = Counter(answers)
        ret = 0
        for k, v in count.items():
            ret += -v % (k+1) + v 
        
        return ret
