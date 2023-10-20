def value(arr, n, k):
    right = n-1
    left = 0
    val = 0
    
    while left < right:
        if arr[left] == 'R':
            val += n -1 - left
        elif arr[left] == 'L':
            if k>=1:
                k-=1
                val += n -1 - left   
            else:
                val += left
                
        if arr[right] == 'L':
            val += right
        elif arr[right] == 'R':
            if k >= 1:
                k-=1
                val += right
            else:
                val += n - 1- right
        left += 1
        right -=1
    if n %2 != 0:
        val += n//2
                
    return str(val)

tc = int(input())

for _ in range(tc):
    n = int(input())
    w = input().strip()
    arr = []
    for k in range(1, n+1):
        arr.append(value(w, n, k))
    
    print(' '.join(arr).strip())
        
            
        
    