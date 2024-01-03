class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dc = {}
        for n in nums:
            dc[n] = ""
        count = 0
        for n in dc:
            nums[count] = n
            count += 1
        return count
