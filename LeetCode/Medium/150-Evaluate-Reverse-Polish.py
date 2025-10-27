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
    

'''
Bruteforce approach, we keep on modifying the input array whenever we come across a sign, until we have the contents of the array equals 1 element, our final answer
TC: O(N^2) because of the list slicing and concatenation going on each time
SC: O(N)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # bruteforce

        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    value1 = int(tokens[i-2])
                    value2 = int(tokens[i-1])
                    if tokens[i] == "+":
                        temp = value1 + value2
                    elif tokens[i] == "-":
                        temp = value1 - value2
                    elif tokens[i] == "*":
                        temp = value1 * value2
                    else:       
                        temp = int(value1 / value2)
                    tokens = tokens[:i-2] + [str(temp)] + tokens[i+1:]
                    break
        return int(tokens[0])