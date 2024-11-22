class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        def flip(x):
            return x^1
        
        n = len(matrix)
        m = len(matrix[0])
        # 000 xxx
        # 001 xx|x
        # 110 xx|x
        
        res = []
        for i in range(n):
            temp = ""
            prev = matrix[i][0]
            for j in range(m):
                if matrix[i][j]==prev:
                    temp+="x"
                else:
                    temp+="|x"
                    prev = matrix[i][j]
            res.append(temp)
        
        freq = defaultdict(int)

        for row in res:
            freq[row]+=1
        
        return max(freq.values())