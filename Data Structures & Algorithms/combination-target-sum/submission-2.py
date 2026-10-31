class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        def dfs(i, cur, subset):

            if cur == target:
                res.append(subset)
                return

            for j,n in enumerate(nums):
                if cur + n <= target and j>=i:
                    dfs(j,cur+n, subset + [n])

                

            
        dfs(-1,0, [])
        return res
        