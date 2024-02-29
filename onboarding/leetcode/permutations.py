class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def swap(i, j, arr):
            arr[i], arr[j] = arr[j], arr[i]

        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                swap(start, i, nums)
                backtrack(start+1, end)
                swap(start, i, nums)

        backtrack(0, len(nums))
        return ans