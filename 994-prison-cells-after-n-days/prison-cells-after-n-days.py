class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        n%=14
        if n==0:
            n=14
        for _ in range(n):
            new_cells=[0]
            for i in range(1,len(cells)-1):
                if cells[i-1]==cells[i+1]:
                    new_cells.append(1)
                else:
                    new_cells.append(0)
            new_cells+=[0]
            #print(new_cells)
            cells=new_cells
        return cells