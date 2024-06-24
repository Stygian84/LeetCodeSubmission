class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        rows={}
        cols={}
        idx=[]
        res=0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                rows[x]=rows.get(x,0)+grid[x][y]
                cols[y]=cols.get(y,0)+grid[x][y]
                if grid[x][y]==1:
                    idx.append([x,y])
                    
        for item in idx:
            res+=(rows[item[0]]-1)*(cols[item[1]]-1)
       
        return res
        '''if len(grid)<=2 and len(grid[0])==1:
            return 0
        if len(grid)==1:
            return 0
        if len(grid[0])==1:
            return 0
        
        def check(arr,i,j):
            count=0
            try: 
                if arr[i][j]==1 and arr[i+1][j]==1 and arr[i][j+1]:
                    count+=1
            except:
                pass
            try: 
                if arr[i][j]==1 and arr[i][j+1]==1 and arr[i-1][j]:
                    count+=1
            except:
                pass
            try: 
                if arr[i][j]==1 and arr[i][j-1]==1 and arr[i-1][j]:
                    count+=1
            except:
                pass
            try: 
                if arr[i][j]==1 and arr[i][j-1]==1 and arr[i+1][j]:
                    count+=1
            except:
                pass
            return count
        total=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                total+=check(grid,i,j)
        return total'''