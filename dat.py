arr = [1,3,3,3, 6, -6, 2, 9, 0, -6, 9, 15, 1, 5]
target = 9

#1, 3, 6
def find_elements(arr, k):
    result = []
    seen = set()
    for num in arr:
        diff = k - num
        if diff in seen: 
            result.append([num, diff])
        seen.add(num)

    return result
print(find_elements(arr, target))