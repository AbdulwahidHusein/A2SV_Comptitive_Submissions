class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        curr_sum = 0
        left = 0
        right = 0
        curr_nums = set()
        while right < n:
            curr_sum += nums[right]
            if nums[right] in curr_nums:
                while nums[left] != nums[right]:
                    curr_sum -=  nums[left]
                    curr_nums.remove(nums[left])
                    left += 1
                curr_sum -=  nums[left]
                curr_nums.remove(nums[left])
                left += 1

            curr_nums.add(nums[right])
            ans = max(curr_sum, ans)

            right += 1
        ans = max(curr_sum, ans)
        return ans