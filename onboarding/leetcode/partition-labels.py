class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        n = len(s)
        for i in range(n):
            last[s[i]] = i
        ans = []
        start = 0
        right = last[s[0]]
        for i in range(n):
            if right == i:
                ans.append(i - start + 1)
                if i == n-1:
                    break
                start = i + 1
                right  = last[s[start]]
            else:
                right = max(right, last[s[i]])
        if right > n-1:
            ans.append(n - start)
        return ans