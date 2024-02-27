class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] != ")":
                stack.append(s[i])
            else:
                n = 0
                while stack and stack[-1] != "(":
                    n += stack.pop()
                stack.pop()
                if n == 0:
                    stack.append(1)
                else:
                    stack.append(2 * n)
                    
        return sum(stack)

