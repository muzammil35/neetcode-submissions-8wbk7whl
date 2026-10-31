class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        def dfs(i, cur):

            if i == len(nums):
                return
            
            if cur == target:
                res.append(subset.copy())
                return

            if cur > target:
                return
            #keep current index
            subset.append(nums[i])
            dfs(i, cur+nums[i])
            subset.pop()
            #skip to next one
            dfs(i+1, cur)
            
           

            

            
            
        dfs(0,0)
        return res
        