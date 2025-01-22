class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 0 = land, 1 = water
        # if water, height must be 0
        # any adjacent cells height difference is at most 1

        # start from water , set to 0, +1 till meets water / meet +1 height

        # 0 ->
        n = len(isWater)
        m = len(isWater[0])
        res = [ [-1]*m for _ in range(n)]
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        queue = deque()

        for i in range(n):
            for j in range(m):
                if isWater[i][j]==1:
                    queue.append((i,j))
                    res[i][j]=0

        while queue:
            x,y = queue.popleft()

            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and res[nx][ny]==-1:
                    queue.append((nx,ny))
                    res[nx][ny] = res[x][y]+1 

        return res