class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        def dfs(i,j):
            if (i,j) not in visited and grid[i][j]==1:
 
                top = 0
                bottom = 0
                left = 0
                right = 0
                visited.add((i,j))
                if i>0:
                    top = dfs(i-1, j)
                if j>0:
                    left = dfs(i, j-1)
                if i < len(grid)-1:
                    bottom = dfs(i+1, j)
                if j < len(grid[0])-1:
                    right = dfs(i, j+1)
                return 1 + top + bottom + left + right
            else:
                return 0



            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea
                