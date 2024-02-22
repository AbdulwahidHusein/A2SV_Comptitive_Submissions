class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        left = [0] * len(arr)
        right = [0] * len(arr)
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else len(arr)
            stack.append(i)
        
        result = 0
        mod = 10**9 + 7
        
        for i in range(len(arr)):
            result += arr[i] * (i - left[i]) * (right[i] - i)
            result %= mod
        
        return result

