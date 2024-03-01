class Solution:
    def valid(self, paranthesis):
        stack = []
        for i in range(len(paranthesis)):
            if paranthesis[i] == "(":
                stack.append("(")
            else:
                if not stack or stack[-1] == ")":
                    return False
                stack.pop()
        return True if not stack else False

    def generateParenthesis(self, n: int) -> List[str]:
        def generate(num, _max):
            b = bin(num)[2:].zfill(_max)
            paranth = []
            for ch in b:
                if ch == "0":
                    paranth.append("(")
                else:
                    paranth.append(")")
            return "".join(paranth)

        possible = 4**n
        ans = []
        for i in range(possible):
            paranth = generate(i, 2*n)
            if self.valid(paranth):
                ans.append(paranth)
        return ans
