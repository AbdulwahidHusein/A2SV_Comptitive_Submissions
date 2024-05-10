# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        candidates = happiness[:k]
        steps = 0
        res = 0
        for i in range(k):
            res += max(0, candidates[i] - steps)
            steps += 1
        return res

            