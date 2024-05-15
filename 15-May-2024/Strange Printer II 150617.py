# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        boundary = defaultdict(lambda: [float('inf'),float('inf'),0,0])#minx miny maxx maxy
        rows, cols = len(targetGrid), len(targetGrid[0])
        for i in range(rows):
            for j in range(cols):
                boundary[targetGrid[i][j]][0] = min(j, boundary[targetGrid[i][j]][0])
                boundary[targetGrid[i][j]][1] = min(i, boundary[targetGrid[i][j]][1] )
                boundary[targetGrid[i][j]][2] = max(j, boundary[targetGrid[i][j]][2])
                boundary[targetGrid[i][j]][3] = max(i, boundary[targetGrid[i][j]][3] )
        attacks = defaultdict(list)
        idg = defaultdict(int)
        for state in boundary:
            for y in range(boundary[state][0],boundary[state][2]+1):
                for x in range(boundary[state][1],boundary[state][3]+1):
                    if targetGrid[x][y] != state:
                        attacks[targetGrid[x][y]].append(state)
                        idg[state] += 1
        q = deque()
        count = 0
        for bn in boundary:
            if idg[bn] == 0:
                q.append(bn)
        while q:
            st = q.popleft()
            count += 1
            for at in attacks[st]:
                idg[at] -= 1
                if idg[at] == 0:
                    q.append(at)

        return count == len(attacks)