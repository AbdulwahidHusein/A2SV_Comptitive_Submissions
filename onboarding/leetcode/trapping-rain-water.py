class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        max_so_far = 0
        for i in range(n-1, -1, -1):
            if height[i] < max_so_far:
                max_right[i] = max_so_far
            max_so_far = max(max_so_far, height[i])
        max_so_far = 0
        for i in range(n):
            if height[i] < max_so_far:
                max_left[i] = max_so_far
            max_so_far = max(max_so_far, height[i])

        ans = 0
        for i in range(n):
            ans += max(0, min(max_left[i], max_right[i]) - height[i])
        return ans
