class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = Counter(nums)
        n = len(nums)
        for m in counter:
            if counter[m] > n/2:
                return m