n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

x = arr[k-1]

if k < len(arr) and arr[k] == x:
    print(-1)
else:
    print(x)