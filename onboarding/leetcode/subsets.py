class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power = [[]]
        def backtrack(current, start, power):
            if len(current):
                power.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(current, i+1, power)
                current.pop()
        backtrack([], 0,power)
        return power
            