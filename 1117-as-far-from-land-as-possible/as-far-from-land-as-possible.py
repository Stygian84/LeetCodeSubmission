class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 0 = water, 1 = land
        # further distance from water to land
        queue = deque([])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((i,j))
        max_distance = -1
        while queue:
            x,y = queue.popleft()
            dist = 2
            seen = set()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                    grid[nx][ny] = grid[x][y] + 1 
                    queue.append((nx, ny))
                    max_distance = max(max_distance, grid[nx][ny] - 1)
        
        return max_distance
        


        '''
        ones = 0
        zeroes = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    ones+=1
                else:
                    zeroes+=1
        if ones==0 or zeroes==0:
            return -1

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(x,y,seen):
            queue = deque([(x,y)])
            
            original_x = x
            original_y = y

            max_distance = 0
            while queue:
                x,y = queue.popleft()
                seen.add((x,y))
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                        break 
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and (nx,ny) not in seen:
                        queue.append((nx,ny))
                        max_distance = max(max_distance,abs(original_x-nx)+abs(original_y-ny))
                     
            return max_distance
        

        res = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    res = max(res,bfs(i,j,set()))
        return res'''