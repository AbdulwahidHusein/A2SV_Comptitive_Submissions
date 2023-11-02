def shortest_possible(st, leng):
    left = 0
    right = leng -1
    
    while st[left] != st[right]:
        if left == right +2:
                return 1
        if left >= right -1:
                return 0
        right -=1
        left += 1 
    return right - left + 1

tc = int(input())

for _ in range(tc):
    leng = int(input())
    st = input()
    print(shortest_possible(st, leng))
    