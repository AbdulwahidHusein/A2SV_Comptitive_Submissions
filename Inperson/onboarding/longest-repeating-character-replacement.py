class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def chars_to_be_changed(counter):
            max_f = max(counter.values())
            s = sum(counter.values())
            return s - max_f

        n = len(s)
        left = 0
        right = 0
        ans = 0

        c = Counter()
        while right < n:
            c[s[right]] += 1
            if chars_to_be_changed(c) > k:
                c[s[left]] -= 1
                left += 1
            ans = max(ans, right-left + 1)
            right += 1
        return ans