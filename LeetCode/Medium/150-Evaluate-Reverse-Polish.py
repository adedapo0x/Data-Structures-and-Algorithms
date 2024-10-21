class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for val in tokens:
            if val == "+":
                stack.append(stack.pop() + stack.pop())
            elif val == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif val == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif val == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(val))
        return stack[0]