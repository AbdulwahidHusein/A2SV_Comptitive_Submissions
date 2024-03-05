class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fset = set(forbidden)
        end = defaultdict(int)
        n = len(word)
        m = len(forbidden)
        for window in range(1, 11):
            if window <= n:
                left = 0
                right = window

                ch = [w for w in word[:window]]
                while right < n:
                    if "".join(ch) in fset:
                        end[right-1] = max( end[right-1],left)
                    ch.pop(0)
                    ch.append(word[right])
                    left += 1
                    right += 1
                if "".join(ch) in fset:
                    end[right-1] = max(end[right-1], left)
        ans = 0
        prev = 0
        for i in range(n):
            if i in end:
                prev = max(end[i]+1, prev)
            ans = max(ans, i - prev+1)
        return ans