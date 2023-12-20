class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0]*(2*n)
        left = 0
        right = n
        i =0
        while i < 2*n:
            ans[i] = nums[left]
            i+=1
            ans[i] = nums[right]
            i+=1
            left += 1
            right += 1
        return ans