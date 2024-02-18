class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{":"}", "[":"]", "(":")"}
        stack = []
        for i in range(len(s)):
            if s[i] in pairs:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if pairs[stack.pop()] != s[i]:
                    return False
        return True if not stack else False