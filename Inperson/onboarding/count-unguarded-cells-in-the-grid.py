class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        #how many cells each guard can keep?
        #for each guard add the vertices he can see    not efficient

        #mark each cells 1 if there is a gua
        walls = {(i,j) for (i, j) in walls}
        guards = {(i, j) for (i, j) in guards}
        guarded_cells = set()
        for x, y in guards:
            x0, y0 = x, y
            #up
            x-=1
            while x >= 0 and not (x, y) in walls and not (x, y) in guards:
                guarded_cells.add((x, y))
                x-=1
            #down
            x, y = x0, y0
            x += 1
            while x <= m-1 and not (x, y) in walls and not (x, y) in guards:
                guarded_cells.add((x, y))
                x += 1
            #left
            x, y = x0, y0
            y-= 1
            while y>= 0 and not (x, y) in walls and not (x, y) in guards:
                guarded_cells.add((x, y))
                y -= 1
            #right
            x, y = x0, y0
            y += 1
            while y <= n-1 and not (x, y) in walls and not (x, y) in guards:
                guarded_cells.add((x, y))
                y += 1

        print(guarded_cells)
        ans = m*n - len(guarded_cells) - len(walls) - len(guards)
        return ans