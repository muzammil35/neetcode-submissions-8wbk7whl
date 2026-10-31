class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, subset):
            if i == len(candidates):
                return

            if cur == target:
                res.append(subset.copy())
                return
            prev = 0
            for j in range(i+1, len(candidates)):
                num = candidates[j]
                if  num == prev:
                    continue
                if num + cur <= target and j > i:
                    dfs(j, cur+num, subset + [num])
                prev = num
        
        dfs(-1, 0, [])
        return res