class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [ [0] * 26 for _ in range(rows+1) ]

    def getXY(self, s):
        col = ord(s[0]) - 65
        row = int(s[1:])
        return (row,col)

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.getXY(cell)
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.getXY(cell)
        self.sheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        def val(s):
            if 65 <= ord(s[0]) <= 90:
                row, col = self.getXY(s)
                return self.sheet[row][col]
            else:
                return int(s)
        
        A, B = formula[1:].split("+")
        return val(A) + val(B)
        
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
