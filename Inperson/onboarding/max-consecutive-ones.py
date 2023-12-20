class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      ans = 0
      max_so_far = 0
      for n in nums:
        if n == 1:
              ans += 1
        else:
            max_so_far = max(max_so_far, ans)
            ans = 0
      max_so_far = max(max_so_far, ans)
      return max_so_far
    
