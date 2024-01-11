class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s = sum(cardPoints)

        left = 0
        right = n - k
        curr_sum = sum(cardPoints[:right])
        ans = s - curr_sum
        left += 1
        right += 1

        while right <= n:
            curr_sum -= cardPoints[left-1]
            curr_sum += cardPoints[right-1]
            ans = max(ans, s - curr_sum)
            left += 1
            right += 1
        return ans
