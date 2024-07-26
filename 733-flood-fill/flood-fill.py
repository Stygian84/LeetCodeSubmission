class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        def dfs(grid,x,y,visited,color):
            if (x,y) in visited:
                return
            visited.add((x,y))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in directions:
                nx,ny = x+dx,y+dy

                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==original:
                    grid[nx][ny]=color
                    dfs(grid,nx,ny,visited,color)


            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            return
        
        visited = set()

        dfs(image,sr,sc,visited,color)
        image[sr][sc]=color
        return image