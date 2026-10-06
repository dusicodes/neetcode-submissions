class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}" : "{", ")" : "(", "]" : "["}
        if len(s) == 1:
            return False

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack[-1] != mapping[char]:
                    return False
                else:
                    stack.pop()

            
        return not stack



