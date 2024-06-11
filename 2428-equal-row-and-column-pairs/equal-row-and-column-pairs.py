class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #collate all rows
        rows={}
        for row in grid:
            rows[tuple(row)]=rows.get(tuple(row),0)+1

        #collate all column
        column={}
        for i in range(len(grid)):
            temp_ls=[]
            for j in range(len(grid)):
                temp_ls.append(grid[j][i])
            column[tuple(temp_ls)]=column.get(tuple(temp_ls),0)+1

        #if exists in both, count+=freq1*freq2
        count=0
        for item in rows:
            if item in column:
                count+=rows[item]*column[item]
        print(rows)
        print(column)
        return count
