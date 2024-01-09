class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        n = len(s2)
        if n<window_size:
            return False

        left = 0
        right = window_size -1
        c1 = Counter(s1)
        c2 = Counter(s2[0:right])
        while right < n:
            if s2[right] in c2:
                c2[s2[right]] += 1
            else:
                c2[s2[right]] = 1
            if c1 == c2:
                return True
            if c2[s2[left]] > 1:
                c2[s2[left]] -= 1
            else:
                del c2[s2[left]]
            left += 1
            right += 1
        return False