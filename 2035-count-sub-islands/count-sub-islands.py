class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= len(grid2) or y < 0 or y >= len(grid2[0]) or grid2[x][y] == 0:
                return True
            grid2[x][y] = 0
            
            is_sub_island = grid1[x][y] == 1
            
            is_sub_island &= dfs(x + 1, y)
            is_sub_island &= dfs(x - 1, y)
            is_sub_island &= dfs(x, y + 1)
            is_sub_island &= dfs(x, y - 1)
            
            return is_sub_island
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        
        return count