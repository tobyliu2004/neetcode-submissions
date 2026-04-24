class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i-last
            stack.append(i)
        return res