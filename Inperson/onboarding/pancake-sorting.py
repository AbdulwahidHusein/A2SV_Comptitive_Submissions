class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1


        #lets bruteforce
        n = len(arr)
        ans = []
        for i in range(n-1, -1, -1):
            max_i = i
            for j in range(i, -1, -1):
                if arr[j] > arr[max_i]:
                    max_i = j
            if max_i != i:
                reverse(max_i)# to make sure at least the next laargest element is in its position
                reverse(i)
                ans.append(max_i + 1)
                ans.append(i + 1)
        return ans
