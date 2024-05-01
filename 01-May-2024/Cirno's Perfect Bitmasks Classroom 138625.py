# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A


for _ in range(int(input())):
    n = int(input())
    i = 0
    if n == 1:
        print(3)
    else:
        while n and 1<<i &n == 0:
            i+=1
        ans = 1 << i
        bits  = 0
        for j in range(32):
            if 1 << j & n:
                bits += 1
                
        if bits == 1:
            ans += 1
        print(ans)
    