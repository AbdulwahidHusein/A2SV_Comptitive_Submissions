# Problem:  King Escape - https://codeforces.com/problemset/problem/1033/A

n = int(input())
x, y = map(int, input().split())
a, b = map(int, input().split())
c,d = map(int, input().split())

coord1 = int(x > a) + 2*(int(y > b))
coord2 = int(x > c)  + 2*(int(y > d))

if coord1 == coord2:
    print("YES")
else:
    print("NO")