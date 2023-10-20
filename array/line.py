def choose(arr):
    mn = min(arr)
    mx = max(arr)
    if mn == mx:
        return 0
    
    mnc = arr.count(mn)
    mxc = arr.count(mx)
    
    return mnc*mxc*2


tc = int(input())

for _ in range(tc):
    input()
    arr = [int(i) for i in input().split()]
    print(str(choose(arr)))