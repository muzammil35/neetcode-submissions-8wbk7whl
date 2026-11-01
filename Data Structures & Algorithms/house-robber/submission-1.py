class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = [0] * len(nums)
        houses[0] = nums[0]

        if len(nums)==1:
            return nums[0]
        houses[1] = max(nums[1], nums[0])

        for k in range(2, len(houses)):
            houses[k] = max(houses[:k-1]) + nums[k]

        return max(houses)