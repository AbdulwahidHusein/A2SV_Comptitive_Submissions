class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        l = len(p)
        pc = Counter(p)
        curr = defaultdict(int)
        left = 0
        right = 0
        ans = []
        while right < l:
            curr[s[right]] += 1
            right += 1
        if curr == pc:
            ans.append(left)
        while right < len(s)+1:
            if curr[s[left]] > 1:
                curr[s[left]] -= 1
            else:
                curr.pop(s[left])
            if right >= len(s):
                break
            curr[s[right]] += 1
            if curr == pc:
                ans.append(left+1)
            left += 1
            right += 1
        return ans