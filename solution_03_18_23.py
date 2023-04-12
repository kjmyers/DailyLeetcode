class BrowserHistory:

    def __init__(self, homepage: str):
        self.f = []
        self.b = []
        self.b.append(homepage)
        

    def visit(self, url: str) -> None:
        self.f = []
        self.b.append(url)
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.b) > 1:
                self.f.append(self.b.pop())
        
        print(self.b)
        print(self.f)
        if self.b:
            return self.b[-1]
        else:
            return None

        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.f:
                self.b.append(self.f.pop())
        if self.b:
            return self.b[-1]
        else:
            return None
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
