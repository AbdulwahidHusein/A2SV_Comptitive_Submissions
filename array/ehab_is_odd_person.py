input()
arr = [int(i) for i in input().split()]

evc=  0
odc = 0

for n in arr:
    if n%2 == 0:
        evc += 1
    else:
        odc +=1

if evc == 0 or odc ==0:
    pr = ' '.join([str(y) for y in arr])
    print(pr.strip())
else:
    arr.sort()
    pr = ' '.join([str(y) for y in arr])
    print(pr.strip())