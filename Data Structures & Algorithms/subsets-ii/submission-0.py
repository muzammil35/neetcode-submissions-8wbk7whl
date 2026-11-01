class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, subset):

            res.append(subset)

            if i == len(nums):
                return

            prev = None
            for j in range(i+1, len(nums)):
                if nums[j] == prev:
                    continue
                dfs(j, subset + [nums[j]])
                prev = nums[j]
        dfs(-1, [])
        return res
        