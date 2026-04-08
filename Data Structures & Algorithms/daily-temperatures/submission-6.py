class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for r in range(len(temperatures)):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = r-i
            stack.append(r)
        return res