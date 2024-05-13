# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            right = i + questions[i][1]
            dp[i] = dp[i+1]
            if right + 1< len(questions):
                dp[i] = max(dp[i], questions[i][0] + dp[right + 1])
            else:
                dp[i] = max(dp[i], questions[i][0])
        return dp[0]