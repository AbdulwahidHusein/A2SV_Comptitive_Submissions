# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(a, b, c):
            if a == "1" and b == "1" and c == "1":
                return ("1", "1")
            elif (a == "1" and b == "1") or (a == "1" and c == "1") or (b == "1" and c == "1"):
                return ("0", "1")
            elif (a == "1" and b == "0" and c == "0") or (a == "0" and b == "1" and c == "0") or (a == "0" and b == "0" and c == "1"):
                return ("1", "0")
            else:
                return ("0", "0")

        n = len(a)
        m = len(b)
        max_l = max(n, m)
        a = "0" * (max_l - n) + a  # Pad the shorter number with leading zeros
        b = "0" * (max_l - m) + b  # Pad the shorter number with leading zeros
        ans = []
        carry = "0"
        for i in range(max_l-1, -1, -1):
            s, carry = add(a[i], b[i], carry)
            ans.append(s)
        if carry == "1":
            ans.append(carry)
        return "".join(ans[::-1])  