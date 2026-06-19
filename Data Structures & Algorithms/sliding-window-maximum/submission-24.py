class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        l = 0
        res = []
        for r in range(len(nums)):
            while stack and stack[-1][0] < nums[r]:
                stack.pop()
            stack.append([nums[r], r])
            if r >= k-1:
                res.append(stack[0][0])
                l+=1
                if stack[0][1] < l:
                    stack.pop(0)
        return res