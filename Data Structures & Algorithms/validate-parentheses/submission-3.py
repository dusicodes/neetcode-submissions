class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = "({["
        cl = ")]}"

        for p in s:
            if p in op:
                stack.append(p)
            else:
                if not stack:
                    return False
                peek = stack[-1]


                if peek == "(" and p == ")" or peek == "[" and p == "]" or peek == "{" and p =="}":
                    stack.pop()
                else:
                    stack.append(p)
        
        return len(stack) == 0





