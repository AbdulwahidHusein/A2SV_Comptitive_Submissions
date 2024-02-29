class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        power = set()
        ans = [[]]
        def backtrack(current, start):
            if len(current):
                if tuple(current) not in power:
                    power.add(tuple(current[:]))
                    ans.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(current, i+1)
                current.pop()  
        backtrack([], 0)
        return ans
            