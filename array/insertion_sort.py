def insertionSort1(n, arr):
    target = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] <= target:
            arr[i+1] = target
            print(" ".join([str(m) for m in arr]))
            return
        arr[i+1] = arr[i]
        print(" ".join([str(o) for o in arr]))
    # Write your code here