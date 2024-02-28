class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        ans = []
        
        def backtrack(path, start):
            if len(path) == k:
                ans.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)  
                path.pop()

        backtrack([], 0)
        return ans