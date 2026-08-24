class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0] * len(nums)
        prefix_prod = 1
        postfix_prod = 1
        for i in range(len(nums)):
            prefix.append(prefix_prod)
            prefix_prod *= nums[i]

        for j in reversed(range(len(nums))):
            postfix[j] = postfix_prod
            postfix_prod *= nums[j]


        ret = []
        for i in range(len(nums)):
            pre = prefix[i] if i>0 else 1
            post = postfix[i] if i<len(nums)-1 else 1

            ret.append(pre*post)
        return ret


