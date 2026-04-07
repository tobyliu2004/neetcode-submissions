class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ("[", "(", "{"):
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if i == ")" and top != "(":
                    return False
                elif i == "}" and top != "{":
                    return False
                elif i == "]" and top != "[":
                    return False
        if stack:
            return False
        return True