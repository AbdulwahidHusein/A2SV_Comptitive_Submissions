class Solution:
    def spans(self, emelemts, n):
        span = [0] * n
        stack = [0]
        for i in range(1, len(emelemts)):
            while stack and emelemts[i] <= emelemts[stack[-1]]:
                stack.pop()
            if stack:
                span[i] = i - stack[-1] - 1
            else:
                span[i] = i
            stack.append(i)
        return span
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        span = [0] * n
        left_span = self.spans(heights, n)
        right_span = self.spans(heights[::-1], n)
        for i in range(n):
            span[i] += left_span[i] + right_span[n - 1 - i]+1
        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * span[i])
        return ans
