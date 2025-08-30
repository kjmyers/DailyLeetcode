class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check Row
        for row in board:
            row = [ x for x in row if x != "."]
            if len(row) != len(set(row)):
                return False
        
        # Check Column
        for column in range(len(board)):
            col = []
            for row in range(len(board)):
                col.append(board[row][column])
            col = [ x for x in col if x != "."]
            if len(col) != len(set(col)):
                return False
        
        # Check boxes
        for rowa in range(0, 9, 3):
            for cola in range(0, 9, 3):
                group = []
                for c in range(3):
                    for r in range(3):
                        group.append(board[c + cola][r + rowa])
                group = [ x for x in group if x != "."]
                if len(group) != len(set(group)):
                    return False
        return True
