# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n,m, k = map(int, input().split())
armies = []
for _ in range(m+1):
    armies.append(int(input()))

fedor = armies.pop()
freinds = 0
for army in armies:
    xor = army ^ fedor
    count = 0
    while xor:
        if xor & 1:
            count += 1
        xor >>= 1
    if count <= k:
        freinds += 1
        
print(freinds)