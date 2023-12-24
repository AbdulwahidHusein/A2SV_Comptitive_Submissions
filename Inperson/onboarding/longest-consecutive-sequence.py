class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in Set:
                currentNum = num
                currans = 1

                while currentNum + 1 in Set:
                    currentNum += 1
                    currans += 1

                ans = max(ans, currans)

        return ans
            