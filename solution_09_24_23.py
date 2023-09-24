class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        
        row = [poured]
        if query_row == 0:
            return 1 if row[query_glass] > 1 else row[query_glass]

        for i in range(1, query_row+1):
            new_row = [0] * (i+1)
            for r in range(len(row)):
                if (row[r]-1) > 0:
                    new_row[r] += (row[r]-1)/2
                    new_row[r+1] += (row[r]-1)/2
            if i == query_row:
                return 1 if new_row[query_glass] > 1 else new_row[query_glass]
            row = new_row
