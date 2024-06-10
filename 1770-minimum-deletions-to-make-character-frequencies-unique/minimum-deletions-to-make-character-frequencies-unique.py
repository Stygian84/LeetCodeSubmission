class Solution:
    def minDeletions(self, s: str) -> int:
        dc={}
        for letter in s:
            dc[letter]=dc.get(letter,0)+1
        count=0
        
        dc1={}
        
        for key,values in dc.items():
            value=values
            while value in dc1 and value>0:
                count+=1
                value-=1
            dc1[value]=0
            
        return count