class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        
        max_sum = 0   
        n = len(heights)
        

        for peak in range(n):
            temp = heights[:]

            for i in range(peak-1,-1,-1):
                temp[i]=min(temp[i],temp[i+1])

            for j in range(peak+1,n):
                temp[j]=min(temp[j],temp[j-1])
            max_sum = max(max_sum,sum(temp))
        return max_sum
        