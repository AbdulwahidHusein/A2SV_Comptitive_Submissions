class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        stack = []
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                inx = stack.pop()
                max_right[inx] = height[i]
            stack.append(i)
        stack2 = []
        for i in range(n-1, -1, -1):
            while stack and height[stack[-1]] < height[i]:
                inx = stack.pop()
                max_left[inx] = height[i]
            stack.append(i)
        max_so_far = 0
        for i in range(n-1, -1, -1):
            if max_right[i] < max_so_far:
                max_right[i] = max_so_far
            max_so_far = max(max_so_far, max_right[i])
        max_so_far = 0
        for i in range(n):
            if max_left[i] < max_so_far:
                max_left[i] = max_so_far
            max_so_far = max(max_so_far, max_left[i])

        ans = 0
        for i in range(n):
            ans += max(0, min(max_left[i], max_right[i]) - height[i])
        return ans
