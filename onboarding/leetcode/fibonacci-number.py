class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f0 = 0
        f1 = 1
        for _ in range(n-1):
            c = f1
            f1 += f0
            f0 = c
        return f1