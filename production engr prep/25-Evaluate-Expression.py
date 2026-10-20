def calculate_evaluation(expression):
    def helper(index):
        stack = []
        num = 0
        prev_sign = "+"
        
        "2+3*5"
        
        while index < len(expression):
            char = expression[index]
            
            if char.isdigit():
                num = num * 10 + int(char)
                
            if  char == "(":
                num, index = helper(index + 1)
                
            if char in "+-*/)" or index == len(expression) - 1:
                if prev_sign == "+":
                    stack.append(num)
                elif prev_sign == "-":
                    stack.append(-num)
                elif prev_sign == "*":
                    stack.append(stack.pop() * num)
                elif prev_sign == "/":
                    stack.append(int(stack.pop / num))
                    
                prev_sign = char
                num = 0
                
                if char == ")":
                    return sum(stack), index
                
            index += 1
        return sum(stack), index
    result, _ = helper(0)
    return result

                
                
