class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l = len(fruits)
        if l < 3:
            return l
        
        d = defaultdict(int)
        d[fruits[0]] += 1
        d[fruits[1]] += 1

        size = 2
        maxSize = size

        for i in range(2,l):
            if len(d.keys()) < 2 or fruits[i] in d:
                d[fruits[i]] += 1
                size += 1
                maxSize = max(size,maxSize)
            else:
                #remove all old fruit
                d[fruits[i]] += 1
                size += 1
                while len(d.keys()) > 2:
                    d[fruits[i-size+1]] -= 1
                    if d[fruits[i-size+1]] == 0:
                        del d[fruits[i-size+1]]
                    size -= 1
        
        return maxSize





