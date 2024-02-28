class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        
        def backtrack(path, curr_sum, start):
            nonlocal ans, n
            if curr_sum == target:
                ans.append(path.copy())
                return
            if curr_sum > target:  
                return
            for i in range(start, n):
                curr_sum += candidates[i]
                path.append(candidates[i])
                backtrack(path, curr_sum, i)  
                path.pop()
                curr_sum -= candidates[i]
        
        backtrack([], 0, 0)
        return ans