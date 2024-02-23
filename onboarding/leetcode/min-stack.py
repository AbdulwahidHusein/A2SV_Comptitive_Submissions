class MinStack:

    def __init__(self):
        self.stack = []
        self.min_indexs = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_indexs.append(0)
        self.stack.append(val)
        if val <= self.stack[self.min_indexs[-1]]:
            self.min_indexs.append(len(self.stack)-1)
    def pop(self) -> None:
        top = self.stack[-1] 
        if top == self.stack[self.min_indexs[-1]]:
            self.min_indexs.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #print(self.min_indexs)
        return self.stack[self.min_indexs[-1]]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()