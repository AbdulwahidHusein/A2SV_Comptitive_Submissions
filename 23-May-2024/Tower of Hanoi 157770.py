# Problem: Tower of Hanoi - https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1


class Solution:
    def toh(self, N, fromm, to, aux):
        self.toh2(N, fromm, to, aux)
        return (1 << N) - 1
        
    def toh2(self, N, fromm, to, aux):
        if N == 1:
            print("move disk " + str(N)+" from rod "+ str(fromm) + " to rod " + str(to))
            return
        self.toh(N-1, fromm, aux, to)
        print("move disk " + str(N)+" from rod "+ str(fromm) + " to rod " + str(to))
        self.toh(N-1, aux, to, fromm)

        