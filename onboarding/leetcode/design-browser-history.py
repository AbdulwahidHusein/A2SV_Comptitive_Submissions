class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward_url = []
        self.backward_url = [homepage]
    def visit(self, url: str) -> None:
        self.backward_url.append(url)
        self.forward_url.clear()

    def back(self, steps: int) -> str:
        while len(self.backward_url) > 1 and steps > 0:
            self.forward_url.append(self.backward_url.pop())
            steps -= 1
        return self.backward_url[-1]

    def forward(self, steps: int) -> str:
        while self.forward_url and steps > 0:
            self.backward_url.append(self.forward_url.pop())
            steps -= 1
        return self.backward_url[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)