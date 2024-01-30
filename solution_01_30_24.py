class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []

        for token in tokens:
            
            if token in ("+","-","*","/"):
                first = s.pop()
                second = s.pop()
                if token == "+":
                    s.append((second + first))
                elif token == "-":
                    s.append((second - first))
                elif token == "*":
                    s.append((second * first))
                elif token == "/":
                    s.append(int(second / first))
            else:
                s.append(int(token))        
        
        return s.pop()
