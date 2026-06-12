class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                match i:
                    case '+': 
                        stack.append(num1 + num2)
                    case '-': 
                        stack.append(num1 - num2)
                    case '*': 
                        stack.append(num1 * num2)
                    case '/': 
                        if num2 != 0:
                            stack.append(int(num1 / num2))
                    case '_':
                        print("invalid")
                        return 0
            else: stack.append(int(i))
        return stack[-1]
        