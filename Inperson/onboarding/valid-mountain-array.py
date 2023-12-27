class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # first = float("inf")
        # second = -float("inf")

        # for num in arr:
        #     if num < second and second > -10**4+1:
        #         return True
        #     if num <= first:
        #         first = num
        #     elif num >= second:
        #         second = num
        # return False
        n = len(arr)
        increasing = False
        decr = False
        if n <= 2:
            return False
        i = 1
        if arr[i] > arr[i-1]:
            increasing = True
        while i < n:
            if arr[i] == arr[i-1]:
                return False
            if not increasing and arr[i] > arr[i-1]:
                return False
            if increasing and arr[i] < arr[i-1]:
                increasing = False
                decr = True
            i += 1
        if not decr or arr[1] <= arr[0]:
            return False
        return True
            
