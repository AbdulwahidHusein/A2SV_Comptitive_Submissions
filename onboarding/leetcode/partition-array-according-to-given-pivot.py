class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        less = 0
        greater = 0
        equal = 0
        for m in nums:
            if m > pivot:
                greater += 1
            elif m < pivot:
                less += 1
            else:
                equal += 1

        ans = [0]*n
        li = 0
        ei = less
        gi = less + equal
        
        for i in range(n):
            if nums[i] < pivot:
                ans[li] = nums[i]
                li += 1
            elif nums[i] > pivot:
                ans[gi] = nums[i]
                gi += 1
            else:
                ans[ei] = nums[i]
                ei += 1
        return ans