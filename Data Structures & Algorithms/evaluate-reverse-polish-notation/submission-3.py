class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                if i == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1+num2)
                elif i == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1-num2)
                elif i == "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(int(num1/num2))
                elif i == "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1*num2)
        return stack[-1]