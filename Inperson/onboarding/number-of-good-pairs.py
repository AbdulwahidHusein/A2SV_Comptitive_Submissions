class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts[n] = 0
        for n in nums:
            counts[n] += 1
        
        good_pairs = 0

        for count in counts.values():
            good_pairs += count*(count-1)//2
        return good_pairs