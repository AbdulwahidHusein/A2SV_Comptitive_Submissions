class Solution: 
        # code here 
    def selectionSort(self, arr,n):
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        s = " ".join([str(m) for m in arr])
        return 