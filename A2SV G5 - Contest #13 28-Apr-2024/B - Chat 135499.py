# Problem: B - Chat - https://codeforces.com/gym/519135/problem/B

from heapq import *
n,k, q = map(int, input().split())
t = list(map(int, input().split()))
onlines = set()
disp = []


for i in range(q):
    typ, id = map(int, input().split())
    if typ == 2:
        if not id in onlines:
            print("NO")
        elif disp[0] > t[id-1]:
            print("NO")
        else:
            print("YES")
    else:
        onlines.add(id)
        if len(disp) >= k and disp[0] < t[id-1]:
            heapreplace(disp, t[id-1])
        elif len(disp) < k:
            heappush(disp, t[id-1])
