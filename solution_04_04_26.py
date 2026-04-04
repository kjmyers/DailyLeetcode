class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        linelen = n // rows
        
        result = []

        for start_col in range(linelen):
            r, c = 0, start_col
            while r < rows and c < linelen:
                result.append(encodedText[r * linelen + c])
                r += 1
                c += 1
        
        while result and result[-1] == ' ':
            result.pop()
        
        return "".join(result)
