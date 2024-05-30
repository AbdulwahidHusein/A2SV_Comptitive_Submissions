# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

import sys
def solve():
    n, sm = map(int, input().split())
    _max = ""
    _min = ""
    if sm == 0:
        if n == 1:
            print(0 ,0)
        else:
            print(-1, -1)
        sys.exit()
    for i in range(n):
        less = min(9, sm)
        _max += str(less)
        sm -= less

    for i in range(n - 1, -1, -1):
        _min += _max[i]
    _min = list(_min)
    if sm > 0:
        print(-1,-1)
        sys.exit(0)
    if _min[0] == '0':
        for i in range(len(_min)):
            if _min[i] != '0':
                _min[i] = str(int(_min[i])-1)
                _min[0] = '1'
                break
    
    

    print("".join(_min),_max)

solve()
