class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rowCheck = []
        for row in board:
            cur = set()
            for col in row:
                if col != ".":
                    cur.add(col)
            rowCheck.append(cur)
        
        colCheck = []
        for col in range(n):
            cur = set()
            for row in range(n):
                if board[row][col] != ".":
                    cur.add(board[row][col])
            colCheck.append(cur)
        
        squareCheck = []
        for rowa in range(0, n, 3):
            curRow = []
            for cola in range(0, n, 3):
                cur = set()
                for c in range(3):
                    for r in range(3):
                        if board[r + rowa][c + cola] != ".":
                            cur.add(board[r + rowa][c + cola])
                curRow.append(cur)
            squareCheck.append(curRow)
        
        def checkValid(num, r, c):
            numS = str(num)
            if numS in colCheck[c]:
                return False
            if numS in rowCheck[r]:
                return False
            if numS in squareCheck[r//3][c//3]:
                return False
            return True
        
        def place_number(num, row, col):
            rowCheck[row].add(num)
            colCheck[col].add(num)
            squareCheck[row//3][col//3].add(num)
            board[row][col] = str(num)
        
        def remove_number(num, row, col):
            rowCheck[row].remove(num)
            colCheck[col].remove(num)
            squareCheck[row//3][col//3].remove(num)
            board[row][col] = "."
        
        def place_next_numbers(row, col):
            nonlocal sudoku_solved
            if col == n - 1 and row == n - 1:
                sudoku_solved = True
            else:
                if col == n - 1:
                    bt(row + 1, 0)
                else:
                    bt(row, col + 1)
        
        def bt( r, c ):
            nonlocal sudoku_solved
            if board[r][c] == ".":
                for int_num in range(1,10):
                    num = str(int_num)
                    if checkValid(num, r, c):
                        place_number(num, r, c)
                        place_next_numbers(r, c)
                        if sudoku_solved:
                            return
                        remove_number(num, r, c)
            else:
                place_next_numbers(r, c)
        
        sudoku_solved = False
        bt(0,0)

