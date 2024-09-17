class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        # 00 0n-1 11 1n-2 3n-3
        n = len(grid)
        m = len(grid[0])

        freq = defaultdict(int)
        y_pos = defaultdict(int)
        count = 0
        for i in range(n):

            for j in range(m):
                if ((i,j)==(count,n-count-1) or (i,j)==(count,count)) and count<n//2:
                    y_pos[grid[i][j]]+=1
                else:
                    freq[grid[i][j]]+=1


            if count>=n//2:
                y_pos[grid[i][count]]+=1
                freq[grid[i][count]]-=1
            else:
                count+=1
        #for y-shape choose the one w highest freq in Y or 2nd highest
        #non y-shape choose the one w highest freq in non-Y 
                
        freq_ls = sorted(freq.items(),key = lambda x:-x[1])
        y_pos_ls = sorted(y_pos.items(),key = lambda x:-x[1])
        
        if len(y_pos_ls)==1 and len(freq_ls)==1:
            if y_pos_ls[0][0]==freq_ls[0][0]:
                return y_pos_ls[0][1]
            else:
                res = y_pos_ls[0][1] + freq_ls[0][1]
            return m*n - res

        if len(y_pos_ls)==1:
            
            if y_pos_ls[0][0]==freq_ls[0][0]:
                res = y_pos_ls[0][1] + freq_ls[1][1]
            else:
                res = y_pos_ls[0][1] + freq_ls[0][1]
            return m*n - res

        if len(freq_ls)==1:
            if y_pos_ls[0][0]==freq_ls[0][0]:
                res = y_pos_ls[1][1] + freq_ls[0][1]
            else:
                res = y_pos_ls[0][1] + freq_ls[0][1]
            return m*n-res

        non_y = freq_ls[0][0]
        y1 = y_pos_ls[0][0]
        y2 = y_pos_ls[1][0]

        if non_y==y1:
            if freq_ls[0][1]+y_pos_ls[1][1]>freq_ls[1][1]+y_pos_ls[0][1]:
                res = y_pos_ls[1][1] + freq_ls[0][1]
            else:
                res = freq_ls[1][1] + y_pos_ls[0][1]
        else:
            res = max(y_pos[y1] ,y_pos[y2]) + freq[non_y]

        return m*n - res