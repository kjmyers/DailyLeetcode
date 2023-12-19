class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        delta = (-1, 0, 1)

        m = len(img)
        n = len(img[0])

        ret = [ [0] * n for _ in range(m) ]

        for i in range(m):
            for j in range(n):

                total = 0
                count = 0

                for di in delta:
                    for dj in delta:
                        if (-1 < i + di < m) and (-1 < j + dj < n):
                            count += 1
                            total += img[i+di][j+dj]
                ret[i][j] = total//count
        
        return ret
                        
