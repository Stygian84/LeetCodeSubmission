class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        #check if possible
        freq_board = defaultdict(int)
        freq_word = Counter(word)
        for i in range(n):
            for j in range(m):
                freq_board[board[i][j]]+=1
        for key in freq_word:
            if key not in freq_board:
                return False
            else:
                if freq_word[key]>freq_board[key]:
                    return False

        #backtrack
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        
        res = False

        def backtrack(x,y,path,visited):
            nonlocal res
            if res:
                return
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