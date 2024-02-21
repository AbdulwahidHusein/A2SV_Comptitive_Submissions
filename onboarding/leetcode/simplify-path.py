class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        stack = []
        for sign in p:
            if sign == "..":
                if stack:
                    stack.pop()
            elif sign != "." and sign != "":
                stack.append(sign)
        
        return "/" + "/".join(stack)