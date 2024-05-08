# Problem: E - XOR Fan - https://codeforces.com/gym/522079/problem/E

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    xor_ps = [0] * (n+1)
    ones = 0
    zeros = 0
    s = input()
        
    for i in range(1, n+1):
        xor_ps[i] ^= nums[i-1] ^ xor_ps[i-1]
        if s[i-1] == '0':
            zeros  ^=  nums[i-1]
        else:
            ones ^= nums[i-1]

    q = int(input())
    res = []
    for _ in range(q):
        cmd = input().split()
        if len(cmd) == 2:
            g = cmd[1]
            if g == "1":
                res.append(ones)
            else:
                res.append(zeros)
        else:
            l, r = int(cmd[1]), int(cmd[2])
            zeros ^= xor_ps[l-1] ^ xor_ps[r]
            ones ^= xor_ps[l-1] ^ xor_ps[r]
            
    print(*res)
for _ in range(int(input())):
    solve()