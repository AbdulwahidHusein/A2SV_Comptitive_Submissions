class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        
        stack = []

        for token in tokens:
            if not token in operators:
                stack.append(token)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                index = operators.index(token)
                value = 0
                if index == 0:
                    value = num1+num2
                elif index == 1:
                    value = num2 - num1
                elif index == 2:
                    value = num1*num2
                else:
                    value = num2/num1
                stack.append(value)
        return int(stack[-1])

