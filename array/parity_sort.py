def pos(arr):
    odd = 0
    even = 0
    
    for n in arr:
        if n%2 == 0:
            odd += 1
        else:
            even += 1
    if odd%2 == 0 and even%2 ==0:
        print("YES")
    else:
        print("NO")

n = int(input())
for _ in range(n):
    input()
    arr = [int(i) for i in input().split()]
    pos(arr)