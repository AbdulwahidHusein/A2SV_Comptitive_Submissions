class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dir = "East"
        self.moves = 0
    def step(self, num: int) -> None:
        self.moves += num

    def getPos(self) -> List[int]:
        has_prev = self.moves >  0
        rem = self.moves %(2*self.width + 2*self.height - 4)
        if rem <= self.width-1:
            self.dir = "East"
            if has_prev and rem == 0:
                self.dir = "South"
            return [rem, 0]
        elif rem <= self.width + self.height -2:
            self.dir = "North"
            return [self.width-1, rem - self.width + 1]
            
        elif rem <= 2 * self.width - 2 + self.height-1:
            self.dir = "West"
            return [self.width - rem +self.width + self.height - 3 , self.height-1]
            
        else:
            self.dir = "South"
            return [0, self.height - rem + 2*self.width - 4 + self.height]
            
    def getDir(self) -> str:
        self.getPos()
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()