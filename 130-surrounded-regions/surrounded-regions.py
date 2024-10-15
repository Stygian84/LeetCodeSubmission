class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        #dfs 
        # get all connected O, if not on edge, replace all with X

        n = len(board)
        m = len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(x,y,seen):
            nonlocal temp
            seen.add((x,y))
            temp.append((x,y))

            flag = True
            
            if x==0 or x==n-1 or y==0 or y==m-1:
                flag = False    

            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if (nx,ny) not in seen and 0<=nx<n and 0<=ny<m and board[nx][ny]=="O":
                    flag = dfs(nx,ny,seen) and flag
                
            return flag            
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    temp = []
                    flag = dfs(i,j,set())
                    
                    if flag:
                        for x,y in temp:
                            board[x][y]="X"
        '''
        visited = set()

        def dfs(x,y,visited):
            if (x,y) in visited:
                return []
            visited.add((x,y))
            cells=[(x,y)]

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dx,dy in directions:
                nx,ny = x+dx , y+dy
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and (nx,ny) not in visited:
                    if board[nx][ny] == "X":
                        return ls
                    else:
                        ls.append((nx,ny))
                        return dfs(nx,ny,visited)

                else:
                    ls=[]
                    return ls

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited:
                    res.extend(dfs(i,j,visited))

        print(res)'''