# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum = sum(nums)
        if _sum % k != 0:
            return False
        
        target = _sum // k
        nums.sort(reverse=True)
        subsets = [0] * k
        
        def backtrack(idx):
            if idx == len(nums):
                return True
            for i in range(k):
                if subsets[i] + nums[idx] <= target:
                    subsets[i] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    subsets[i] -= nums[idx]
                if subsets[i] == 0:
                    break
            return False
        
        return backtrack(0)