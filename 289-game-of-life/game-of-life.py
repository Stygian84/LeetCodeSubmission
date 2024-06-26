class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0-1 dies, 2-3 lives, >3 dies

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),   
            (-1, -1), (-1, 1), (1, -1), (1, 1)  
        ]
        if not board:
            return
        
        m,n=len(board),len(board[0])
        i,j=0,0

        while i<m and j<n:
            count=0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if board[ni][nj]%2==1:
                        count+=1
                        
            if board[i][j]==1:
                if count==2 or count==3:
                    board[i][j]+=2
            elif board[i][j]==0:
                if count==3:
                    board[i][j]+=2

            if j<n-1:
                j+=1
            else:
                i+=1
                j=0

        i,j=0,0

        while i<m and j<n:

            board[i][j]//=2
                
            if j<n-1:
                j+=1
            else:
                i+=1
                j=0