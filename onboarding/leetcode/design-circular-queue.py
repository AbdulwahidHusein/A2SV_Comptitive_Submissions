class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        # self.queue = [0]*k
        # self.start = -1
        # self.end = 0
        self.queue = deque()


    def enQueue(self, value: int) -> bool:
        # if not self.isEmpty():
        #     self.queue[self.end] = value
        #     self.end += 1
        #     if self.end == k:
        #         self.end = 0
        #     return True
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        # if not self.isEmpty():
        #     self.queue[self.start+1] = 0
        #     self.start += 1
        #     return True
        if self.queue:
            self.queue.popleft()
            return True
        return False

    def Front(self) -> int:
        # if not self.isEmpty():
        #     return self.queue[self.end]
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        # if not self.isEmpty():
        #     return self.queue[self.start+1]
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        # return self.start + 1 == self.end
        return len(self.queue) == 0

    def isFull(self) -> bool:
        # return self.end == self.start
        return len(self.queue) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()