class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        def dfs(i, cur):

            if cur == target:
                res.append(subset.copy())
                return

            for j,n in enumerate(nums):
                if cur + n <= target and j>=i:
                    subset.append(n)
                    dfs(j,cur+n)
                    subset.pop()
                

            
        dfs(-1,0)
        return res
        