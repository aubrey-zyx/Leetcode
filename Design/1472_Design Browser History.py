class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.cur, self.last = 0, 0

    def visit(self, url: str) -> None:
        self.cur += 1
        if len(self.stack) > self.cur:
            self.stack[self.cur] = url
        else:
            self.stack.append(url)
        self.last = self.cur

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.stack[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.last, self.cur + steps)
        return self.stack[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)