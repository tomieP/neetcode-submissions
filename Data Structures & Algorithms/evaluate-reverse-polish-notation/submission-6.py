class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if len(tokens) == 1: return int(tokens[0])
            if len(stack) > 1 and (i == '+' or i =='-' or i =='*'or i =='/'):
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                match i:
                    case '+': 
                        res =  num1 + num2
                    case '-': 
                        res = num1 - num2
                    case '*': 
                        res = num1 * num2
                    case '/': 
                        if num2 != 0:
                            res = int(num1 / num2)
                        else: return 0
                    case '_':
                        print("invalid")
                        return 0
                stack.append(res)
            else: stack.append(i)
        return res
