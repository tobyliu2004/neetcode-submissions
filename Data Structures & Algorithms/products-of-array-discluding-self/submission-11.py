class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [0] * len(nums)
        prefix = [0] * len(nums)

        prefix[0] = 1
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        postfix[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i+1]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = postfix[i]*prefix[i]
        return res