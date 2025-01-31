class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        zeroes = 0
        ones = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    zeroes+=1
                else:
                    ones+=1
        
        if zeroes == 0:
            return n*n
        if ones == 0:
            return 1


        seen = set() #traversed 1
        def bfs(x,y,label):
            queue = deque([(x,y)])
            grid[x][y]=label
            size = 1

            while queue:
                x,y = queue.popleft()
                seen.add((x,y))
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1 and (nx,ny) not in seen:
                        queue.append((nx,ny))
                        grid[nx][ny] = label
                        size+=1
            return size


        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        islands = defaultdict(int) #islands[x] = occupied grid
        

        x = 2 #unique key for islands dict
        maxSize = 0 #maximum size of an island
        zero_location = set() # location for zero

        for i in range(n):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in seen:
                    size = bfs(i,j,x)
                    islands[x]=size
                    if size>maxSize:
                        maxSize = size
                    x+=1
                elif grid[i][j] == 0:
                    zero_location.add((i,j))
                    
        res = maxSize
        for x,y in zero_location:
                
            total = 0
            connected_islands = set()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<n:
                    connected_islands.add(grid[nx][ny])
            
            for label in connected_islands:
                total+=islands[label]
            
            res = max(res,total)
                

        return res+1