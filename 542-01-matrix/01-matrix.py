class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat), len(mat[0])


        dp = [[math.inf]*m for _ in range(n)]


        directions = [(-1,0),(0,-1)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    for dx,dy in directions:
                        nx,ny = i+dx,j+dy
                        if 0<=nx<n and 0<=ny<m:
                            dp[i][j] = min(dp[i][j], dp[nx][ny] + 1)

        directions = [(0,1),(1,0)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                for dx,dy in directions:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<n and 0<=ny<m:
                        dp[i][j] = min(dp[i][j], dp[nx][ny] + 1)
            

        return dp