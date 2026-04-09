class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse=True)
        for pos, speed in pairs:
            time = (target-pos)/speed
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)