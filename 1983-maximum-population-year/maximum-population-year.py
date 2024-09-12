class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        year = [0]*101

        for b,d in logs:
            for i in range(b,d):
                year[i-1950]+=1
            
        idx = year.index(max(year))
        return idx+1950