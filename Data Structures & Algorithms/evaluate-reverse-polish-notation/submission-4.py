class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        opStack = []

        for token in tokens:
            if token in operators:
                b = opStack.pop()
                a = opStack.pop()
                match token:
                    case "+":
                        opStack.append(a + b)
                    case "*":
                        opStack.append(a * b)
                    case "-":
                        opStack.append(a - b)
                    case "/":
                        opStack.append(int(a / b))

                     
            else:
                opStack.append(int(token))
            
        return opStack[-1]


        