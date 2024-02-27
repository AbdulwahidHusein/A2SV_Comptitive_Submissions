class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        c = -float('inf')
        stack =[]
        for i in range(n-1, -1, -1):
            if nums[i] < c:
                return True
            while stack and stack[-1] < nums[i]:
                c = stack.pop()
            stack.append(nums[i])
        return False
