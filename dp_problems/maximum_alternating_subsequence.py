#group the array as a collection of +ve -ve +ve -ve
#for each group add the maxumun 

# 1 2 -3 -5 3 -7 --- [1,2,3] [-3,-5], [3], [-7]

#3,-3,3,-7

def max_alternating_subseq(arr: list, n):
    groups = []
    left = 0
    right = 0
    while right < n:
        if not arr[right]/arr[left] > 0:
            groups.append(arr[left:right])
            left = right
        right += 1
    groups.append(arr[left:right])
    count = 0
    for group in groups:
        count += max(group)
    return count

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(max_alternating_subseq(arr, n))