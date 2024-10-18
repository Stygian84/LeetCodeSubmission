class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0]*n
        dp[0] = (values[0],0)

        res = 0
        best_value = (values[0],0)
        # find maximum values[i]+i and values[j]-j where i<j
        for i in range(1,n):
            pointer = values[i]+i
            curr_value = values[i]-i

            if curr_value + best_value[0]>res:
                res = curr_value + best_value[0]
            
            if pointer>best_value[0]:
                best_value = (pointer,i)
            
            #print(values[i]+i , values[i]-i)
        
        return res
        '''n = len(values)
        res = 0
        
        for i in range(n):
            for j in range(i+1,n):
                if i!=j:
                    score = values[i] + values[j] + i - j
                    res = max(res, score)
        
        return res'''