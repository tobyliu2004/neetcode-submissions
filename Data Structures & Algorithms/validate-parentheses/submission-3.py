class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        yea = {"{": "}", "(": ")", "[": "]"}
        for char in s:
            if char in yea:
                stack.append(char)
            else:
                if not stack or yea[stack.pop()]!=char:
                    return False
        return len(stack) == 0