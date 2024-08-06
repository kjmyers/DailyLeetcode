class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)

        l = [(x[1],x[0]) for x in c.items()]
        l.sort(reverse=True)

        total = 0
        count = 0
        mult = 1
        for v,_ in l:
            total += mult * v
            count += 1
            if count >= 8:
                mult += 1
                count = 0

        return total
