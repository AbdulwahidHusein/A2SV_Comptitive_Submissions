# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inbound(x, y):
            return 0 <= x < len(maze) and 0 <= y < len(maze[0] )
        visited = set()

        q = deque()
        rows = len(maze)
        cols = len(maze[0])
        for i in range(rows):
            if maze[i][0] == "." and [i, 0] != entrance:
                visited.add((i, 0))
                q.append((i, 0))
            if maze[i][cols-1] == "." and [i, cols-1] != entrance:
                q.append((i, cols-1))
                visited.add((i, cols-1))
        for j in range(cols):
            if maze[0][j] == "." and [0, j] != entrance:
                q.append((0, j))
                visited.add((0, j))
            if maze[rows-1][j] == "." and [rows-1, j] != entrance:
                visited.add((rows-1, j))
                q.append((rows-1, j))
        
        level = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                for dx, dy in dirs:
                    newx = x + dx
                    newy = y +dy
                    if [newx, newy] == entrance:
                        return level + 1
                    if inbound(newx, newy) and not (newx, newy) in visited and maze[newx][newy] == ".":
                        q.append((newx, newy))
                        visited.add((newx, newy))
            level += 1
        return -1

