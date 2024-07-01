class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        res=0
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j] and abs(i-j)>res:
                    res=abs(i-j)
        return res