class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}  
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum in remainder_count:
                count += remainder_count[prefix_sum]
                remainder_count[prefix_sum] += 1
            else:
                remainder_count[prefix_sum] = 1

        return count