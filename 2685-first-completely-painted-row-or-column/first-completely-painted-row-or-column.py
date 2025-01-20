class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        location = defaultdict(tuple)

        for i in range(n):
            for j in range(m):
                location[mat[i][j]] = (i,j)

        row_freq = defaultdict(int)
        col_freq = defaultdict(int)

        for i in range(len(arr)):
            x,y = location[arr[i]]
            row_freq[x] += 1
            col_freq[y] += 1

            if row_freq[x]==m:
                return i
            elif col_freq[y]==n:
                return i
        
        return -1