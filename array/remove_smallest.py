def is_sm(arr):
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]+1:
            print('NO')
            return
    print('YES')
    return

tc = int(input())
for _ in range(tc):
    n = int(input())
    
    arr = [int(i) for i in input().split()]
    
    arr.sort()
    is_sm(arr)

