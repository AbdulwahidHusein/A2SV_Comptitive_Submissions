class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        pref = [0] * (n+1)
        for i in range(1, n+1):
            pref[i] = pref[i-1] + nums[i-1]

        def rec(i, j):
            if i == j:
                score = nums[i]
                return score
            elif i == j-1:
                score = max(nums[i], nums[j])
                return score
            score = max(-rec(i+1, j) + nums[i] - pref[i+1] + pref[j+1], -rec(i, j-1)+nums[j] + pref[j] - pref[i])
            return score

        score = rec(0, n-1)
        if score >= pref[-1] / 2:
            return True
        return False