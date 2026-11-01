class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        def dfs(i,j):
            if (i,j) in visited:
                return
            if grid[i][j] == "1":
                visited.add((i, j))
                if i>0:
                    dfs(i-1, j)
                if j > 0:
                    dfs(i, j-1)
                if j < len(grid[0])-1:
                    dfs(i, j+1)
                if i< len(grid)-1:
                    dfs(i+1, j)
            else:
                return
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        return islands

        


