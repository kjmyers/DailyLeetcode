class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        balls = []
        n = len(boxes)
        for i in range(n):
            if boxes[i] == '1':
                balls.append(i)
        
        ret = [0] * n

        for i in range(n):
            for b in balls:
                ret[i] += abs(b - i)

        return ret
