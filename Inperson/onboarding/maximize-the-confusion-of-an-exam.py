class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        left = 0
        right = 0
        c = {"T":0, "F":0}  # Initialize counts for 'T' and 'F' respectively
        curr_max = 0
        n = len(answerKey)
        while right < n:
            answer = answerKey[right]
            c[answer] += 1
            curr_max = max(curr_max, c[answer])
            if right - left + 1 - curr_max > k:
                c[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans