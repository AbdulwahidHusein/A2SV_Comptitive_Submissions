def countingSort(arr):
    # Write your code here
    counts = [0]*100
    for n in arr:
        counts[n] += 1
    return counts