class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # for i, n in enumerate(nums):
        #     nums[i], nums[n-1] = nums[n-1], nums[i]
        # print(nums)
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] != i+1:
        #         ans.append(i+1)
        # return ans
        return list(set(list(range(1, len(nums)+1))) - set(nums)) 