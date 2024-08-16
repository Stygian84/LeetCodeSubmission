class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k = k%n

        res = [[0]*n for _ in range(len(mat))]
        
        for i in range(len(mat)):
            if i%2==0: #left shift 
                for j in range(n): 
                    res[i][j] = mat[i][(j+k)%n]
            else: #right shift
                for j in range(n): 
                    res[i][j] = mat[i][j-k]
        
        return res == mat