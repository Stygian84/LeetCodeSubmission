class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        res = 0
        best_value = values[0]
        # find maximum values[i]+i and values[j]-j where i<j
        
        for i in range(1,n):
            pointer = values[i]+i
            curr_value = values[i]-i

            if curr_value + best_value>res:
                res = curr_value + best_value
            
            if pointer>best_value:
                best_value = pointer
            
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