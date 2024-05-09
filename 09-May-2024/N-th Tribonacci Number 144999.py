# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        t0, t1, t2 = 0,1,1
        tri_fibs = [0]*(n+1)
        tri_fibs[0] = 0
        tri_fibs[1] = tri_fibs[2] = 1
        for i in range(3, n+1):
            tri_fibs[i] = tri_fibs[i-1]+tri_fibs[i-2]+tri_fibs[i-3]
        return tri_fibs[-1]
