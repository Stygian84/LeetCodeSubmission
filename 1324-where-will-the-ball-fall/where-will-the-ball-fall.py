class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def getBallDestination(col: int) -> int:
            n, m = len(grid), len(grid[0])
            for row in range(n):
                direction = grid[row][col]
                next_col = col + direction
                if next_col < 0 or next_col >= m or grid[row][next_col] != direction:
                    return -1
                
                col = next_col
            
            return col
        
        m = len(grid[0])
        result = []
        
        for col in range(m):
            result.append(getBallDestination(col))
        
        return result




        '''result=[0]*len(grid[0])
        for row_idx in range(len(grid)):
            for idx in range(1,len(grid[0])):
                if grid[row_idx][idx]!=grid[row_idx][idx-1]:
                    result[idx]=-1
                    result[idx-1]=-1
                if result[idx-1]!=-1:
                    if grid[row_idx][idx-1]==1:
                        result[idx-1]+=1
                    if grid[row_idx][idx-1]==-1:
                        result[idx-1]-=1
            if row_idx==0 and grid[row_idx]==-1:
                result[0]=-1
                continue
            if row_idx==len(grid)-1 and grid[row_idx]==1:
                result[-1]=-1

        return result'''