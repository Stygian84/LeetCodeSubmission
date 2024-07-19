class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors = [colors[-1]]+colors+[colors[0]]
        
        count = 0
        print(colors)
        for i in range(1,len(colors)-1):
            if colors[i]!=colors[i-1] and colors[i]!=colors[i+1]:
                count+=1
                
        return count