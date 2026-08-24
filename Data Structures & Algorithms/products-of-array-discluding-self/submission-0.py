class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counter = nums.count(0)

        # 2+ zeros
        if zero_counter > 1:
            return [0] * len(nums)

        # Exactly 1 zero
        if zero_counter == 1:
            product = 1

            for num in nums:
                if num != 0:
                    product *= num

            ret = []
            for num in nums:
                if num == 0:
                    ret.append(product)
                else:
                    ret.append(0)

            return ret

        # No zeros
        product = 1
        for num in nums:
            product *= num

        ret = []
        for num in nums:
            ret.append(product // num)

        return ret