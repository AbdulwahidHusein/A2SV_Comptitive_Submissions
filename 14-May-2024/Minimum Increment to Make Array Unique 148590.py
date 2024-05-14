# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums.sort()
        ans = 0
        aggrigate = []
        nums.append(2*nums[-1] + 2)

        for i in range(len(nums)-1):
            j = nums[i]+1
            while j < nums[i+1] and aggrigate:
                num = aggrigate[-1]
                if c[num] == 1:
                    aggrigate.pop()
                else:
                    c[num] -= 1
                    ans += j - num
                    j += 1
            if c[nums[i]] > 1:
                if not aggrigate or (aggrigate and aggrigate[-1] != nums[i]):
                    aggrigate.append(nums[i])

        return ans
