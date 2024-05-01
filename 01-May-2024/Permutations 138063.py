# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(curr, av):
            nonlocal n
            if len(curr) == n:
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if  (1 << i) & av == 0:
                    curr.append(nums[i])
                    av |= (1 << i)
                    backtrack(curr, av)
                    curr.pop()
                    av &= ~(1 << i)
                       
        backtrack([], 0)
        return ans