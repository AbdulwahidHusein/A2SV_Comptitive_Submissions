# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

#User function Template for python3
from sys import exit
class Solution:
    def findOrder(self,alien_dict, N, K):
        s = alien_dict
        n = N
        mat = [[0] * 30 for _ in range(30)]
        visited = [0] * 30
        N = 0
        use = [0] * 30
        ans = [''] * 30
        cycle = False
        
        def build(x, y):
            l1 = len(s[x])
            l2 = len(s[y])
            for i in range(min(l1, l2)):
                if s[x][i] != s[y][i]:
                    mat[ord(s[x][i]) - ord('a')][ord(s[y][i]) - ord('a')] = 1
                    return True
            return l1 <= l2
        
        def dfs(s):
            nonlocal cycle, N
            if visited[s] == 1:
                cycle = True
                return
            if visited[s] == 2:
                return
            visited[s] = 1
            for t in range(26):
                if mat[s][t]:
                    dfs(t)
            visited[s] = 2
            ans[N] = chr(s + ord('a'))
            N += 1
        
        for i in range(n - 1):
            if not build(i, i + 1):
                print("Impossible")
                exit(0)
        
        for i in range(26):
            if not visited[i]:
                dfs(i)
        

        res = []
        for i in range(N - 1, -1, -1):
            res.append(ans[i])
            use[ord(ans[i]) - ord('a')] = 1
        for i in range(26):
            if not use[i]:
                res.append(chr(i + ord('a')))
        # print(res)
        return "".join(res[-K:])