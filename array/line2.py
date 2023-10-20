def wp(arr):
    pos = {}
    for index ,n in enumerate(arr):
        try:
            pos[n].append(index)
        except:
            pos[n] = [index]
    arr.sort(reverse=True)
    
    arrr = [0]*len(arr)
    n = 1
    id = 0
    while id < len(arr):
        curr = arr[id]
        for index in pos[arr[id]]:
                arrr[index] = str(n)
                n+=1
        while id<len(arr) and curr == arr[id]:
            id += 1

            
    return arrr

tc = int(input())

for _ in range(tc):
    input()
    arr = [int(i) for i in input().split()]
    print(' '.join(wp(arr)).strip())
    
    
    
    
    
    