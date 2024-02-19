class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                stack.append("(")
            else:
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(")")
                else:
                    stack.append(")")
        return len(stack)