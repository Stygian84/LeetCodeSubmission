class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        directions = []

        for i in range(-1,2):
            for j in range(-1,2):
                directions.append((i,j))

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                dc = {}
                if not 1<=grid[i][j]<=9:
                    continue
                
                row = []
                for dx,dy in directions:
                    nx,ny = i+dx,j+dy
                    number = grid[nx][ny]
                    if not 1<=number<=9:
                        break
                    dc[number]=1

                    row.append(number)

                else: 
                    if len(dc)==9:
                        #check sum row
                        if sum(row[:3]) == sum(row[3:6]) == sum(row[6:]):
                            #check sum cols
                            if row[0]+row[3]+row[6] == row[1]+row[4]+row[7] == row[2]+row[5]+row[8]:
                                #check diagonal
                                if row[0]+row[4]+row[8] == row[2]+row[4]+row[6]:
                                    count+=1


        return count