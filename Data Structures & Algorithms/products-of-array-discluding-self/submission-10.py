class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [0] * len(nums)
        prefix = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i+1] * nums[i+1]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = postfix[i] * prefix[i]
        return res