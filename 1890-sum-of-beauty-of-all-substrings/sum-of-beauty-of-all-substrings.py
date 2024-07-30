class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total=0
        for i in range(n):
            dc = {}
            for j in range(i,n):
                dc[s[j]] = dc.get(s[j],0)+1
                total += max(dc.values())-min(dc.values())
        return total

        '''n = len(s)
        prefix_sum = [[0]*26 for _ in range(n+1)]

        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            for j in range(26):
                prefix_sum[i+1][j] = prefix_sum[i][j]
            prefix_sum[i+1][char_idx]+=1
        
        total = 0
        
        for i in range(n):
            for j in range(i+1,n+1):
                maximum = -math.inf
                minimum = math.inf

                for k in range(26):
                    count = prefix_sum[j][k] - prefix_sum[i][k]
                    if count > 0: 
                        maximum = max(maximum, count)
                        minimum = min(minimum, count)

                if maximum != -math.inf and minimum != math.inf:
                    total += maximum - minimum
        return total'''