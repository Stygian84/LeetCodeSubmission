class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size= len(grid)-2
        max_ls=[]
        #find max every 3 items in a row
        for row in range(len(grid)):
            for idx in range(len(grid[row])):
                if idx+3>len(grid[row]):
                    break
                max_value=max(grid[row][idx:idx+3])
                max_ls.append(max_value)
        print(max_ls)
        max_ls2=[]
        #8->4 15->9
        #find max every 3x3 items (every +size index)
        for idx in range(len(max_ls)-size*2):
            temp_ls=[]
            temp_ls.append(max_ls[idx])
            temp_ls.append(max_ls[idx+size])
            temp_ls.append(max_ls[idx+2*size])
            max_ls2.append(max(temp_ls))
        print(max_ls2)
        temp_ls2=[]
        result=[]
        for i in range(len(max_ls2)):
            if len(temp_ls2)<size:
                temp_ls2.append(max_ls2[i])
            else:
                result.append(temp_ls2)
                temp_ls2=[max_ls2[i]]
        result.append(temp_ls2)


        return result
