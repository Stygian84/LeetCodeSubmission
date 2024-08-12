class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.dc = {}
        self.n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dc[ grid[i][j] ] = (i,j)

    def adjacentSum(self, value: int) -> int:
        directions = [ (0,1),(1,0),(-1,0),(0,-1) ]
        n = self.n
        x,y = self.dc[value]
        total = 0
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                total+=self.grid[nx][ny]
        
        return total

    def diagonalSum(self, value: int) -> int:
        directions = [ (1,1),(-1,-1),(-1,1),(1,-1) ]
        n = self.n
        x,y = self.dc[value]
        total = 0
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                total+=self.grid[nx][ny]
        
        return total



# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)