class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        costs.sort(key = lambda x:x[0]-x[1])
        
        n = len(costs)

        for i in range(n):
            if i<n//2:
                res+=costs[i][0]
            else:
                res+=costs[i][1]
        return res