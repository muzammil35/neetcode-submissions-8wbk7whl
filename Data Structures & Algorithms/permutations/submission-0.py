class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur):
            
            if len(cur) == len(nums):
                res.append(cur)
                return
            for num in nums:
                if num not in cur:
                    dfs(cur + [num])
        dfs([])
        return res


        