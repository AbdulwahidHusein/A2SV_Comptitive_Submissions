class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        carry1 = 1
        carry2 = 1
        mul = 0
        for i in num1[::-1]:
            
            carry2 = 1
            for j in num2[::-1]:
                mul += int(i)*carry1*int(j)*carry2
                carry2*=10
            carry1*=10
        return str(mul)

        