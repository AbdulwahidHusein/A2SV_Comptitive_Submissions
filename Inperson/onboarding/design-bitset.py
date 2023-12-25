class Bitset:
    def __init__(self, size: int):
        self._bitset = [0]*size
        self.ones = 0
        self.size = size
        self.flips = 0
    def fix(self, idx: int) -> None:
        if self.flips%2==0:#not flipped
            if self._bitset[idx] == 0:
                self.ones += 1
            self._bitset[idx] = 1
        else:
            if self._bitset[idx] == 1:
                self.ones -= 1
            self._bitset[idx] = 0
            
    def unfix(self, idx: int) -> None:
        if self.flips%2==0:#not flipped
            if self._bitset[idx] == 1:
                self.ones -= 1
            self._bitset[idx] = 0
        else:#unflipper state
            if self._bitset[idx] == 0:
                self.ones += 1
            self._bitset[idx] = 1

    def flip(self) -> None:
        self.flips += 1
        
    def all(self) -> bool:
        if self.flips %2 == 0:
            return self.ones == self.size
        return self.ones == 0

    def one(self) -> bool:
        if self.flips %2 == 0:
            return True if self.ones >=1 else False
        return  not self.ones == self.size

    def count(self) -> int:
        if self.flips %2 == 0:
            return self.ones
        return self.size - self.ones

    def toString(self) -> str:
        if self.flips %2 == 0:
            return "".join([str(i) for i in self._bitset])
        return "".join([str(int(not i)) for i in self._bitset])
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()