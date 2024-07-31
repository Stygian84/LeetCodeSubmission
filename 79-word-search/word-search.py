class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        
        n,m = len(board),len(board[0])
        res = False
        def backtrack(x,y,path,visited):
            nonlocal res
            visited.add((x,y))
            if len(path) == len(word):
                res = True
                return 
            for dx,dy in direction:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited and board[nx][ny] == word[len(path)]:
                    path.append(word[len(path)])
                    backtrack(nx,ny,path,visited)
                    path.pop()
            visited.remove((x,y))
            return 
        
    
        
        for i in range(n):
            for j in range(m):
                visited = set()
                if board[i][j]==word[0]:
                    backtrack(i, j, [board[i][j]], visited)
                    if res:
                        return res
        return res