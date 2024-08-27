class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        seen = set()
        res = []
        n,m = len(land),len(land[0])

        directions = [(0,1),(1,0)]
        
        def dfs(x,y,bounds):
            seen.add((x, y))
            bounds[2] = max(bounds[2], x)
            bounds[3] = max(bounds[3], y)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and land[nx][ny] == 1:
                    dfs(nx, ny, bounds)

        
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and (i, j) not in seen:
                    bounds = [i, j, i, j]
                    dfs(i, j, bounds)
                    res.append(bounds)

        return res
        '''seen = set()
        res = set()
        n,m = len(land),len(land[0])

        directions = [(0,1),(1,0)]
        
        def dfs(x,y,path):
            nonlocal res,n,m,seen
            path.append([x,y])
            seen.add((x,y))

            count = 0
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and land[nx][ny]==1:
                    dfs(nx,ny,path)
                else:
                    count+=1
            
            if count==2:
                temp = []
                temp.append(path[0][0])
                temp.append(path[0][1])
                temp.append(path[-1][0])
                temp.append(path[-1][1])
                res.add(tuple(temp))
                return

        
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and land[i][j]==1:
                    dfs(i,j,[])

        result = []
        for item in res:
            result.append(list(item))
        return result'''