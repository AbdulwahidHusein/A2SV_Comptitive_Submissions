# Problem: E - Seamless Flow - https://codeforces.com/gym/519135/problem/E

from collections import deque, defaultdict
def topSort(graph, indegree):
    queue = deque()
    for node in range(n):
        if not indegree[node]:
            queue.append(node)
    top_order = []

    while queue:
        cur = queue.popleft()
        top_order.append(cur)
        for neigh in graph[cur]:
            indegree[neigh] -= 1

            if not indegree[neigh]:
                queue.append(neigh)
    return top_order


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    directed = []
    undirected = []
    for i in range(m):
        direction, x, y = map(int, input().split())
        x -= 1 
        y -= 1
        if direction:
            directed.append((x, y))
        else:
            undirected.append((x, y))
    graph = [[] for node in range(n)]
    indegree = defaultdict(int)
    for x, y in directed:
        graph[x].append(y)
        indegree[y] += 1
    order= topSort(graph, indegree)

    if len(order) < n:
        print("NO")
    
    else:
        temp = {node: idx for idx, node in enumerate(order)}
        print('YES')
        for x, y in undirected:
            if temp[x] < temp[y]:
                print(x + 1, y + 1)
                
            else:
                print(y + 1, x + 1)

        for x, y in directed:
            print(x + 1, y + 1)