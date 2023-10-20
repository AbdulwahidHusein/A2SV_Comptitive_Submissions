
def not_working(st, leng):
    arr = [st[0]]
    
    for i in range(1, len(st)):
        if arr:
            if st[i] == arr[-1]:
                arr.pop()
            else:
                arr.append(st[i])
            
    s = set(arr)
    return "".join([w for w in sorted(s)])
        

tc = int(input())
            
for _ in range(tc):
    st = input()
    leng = len(st)
    print(not_working(st, leng))
    