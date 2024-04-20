class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        ret = []
        seen = set()
        for i in range(len(land)):
            for j in range(len(land[0])):
                if (i,j) not in seen and land[i][j] == 1:
                    dj = j + 1
                    while dj < len(land[0]) and land[i][dj] == 1:
                        dj += 1
                    di = i + 1
                    while di < len(land) and land[di][j] == 1:
                        di += 1
                    ret.append([i,j,di-1,dj-1])
                    for ii in range(i,di):
                        for jj in range(j,dj):
                            seen.add((ii,jj))


        return ret
