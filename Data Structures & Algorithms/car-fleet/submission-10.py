class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortee = sorted(zip(position, speed), reverse = True)
        stack = []
        for pos, sped in sortee:
            time = (target-pos) / sped
            if not stack:
                stack.append(time)
            elif stack[-1] < time:
                stack.append(time)
        return len(stack)