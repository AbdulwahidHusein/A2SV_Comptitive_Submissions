class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #lets brute force
        first = float("inf")
        second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
                