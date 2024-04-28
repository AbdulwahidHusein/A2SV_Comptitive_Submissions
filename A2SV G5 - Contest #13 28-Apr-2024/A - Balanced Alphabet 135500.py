# Problem: A - Balanced Alphabet - https://codeforces.com/gym/519135/problem/A

for _ in range(int(input())):
    n,k = map(int, input().split())
    res = []
    a = 0
    for i in range(n):
        res.append(chr(ord("a")+a%k))
        a += 1
    print("".join(res))