class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=int(len(s)/2)
        count=0
        ls=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(n):
            if s[:n][i] in ls:
                count+=1
            if s[n:][i] in ls:
                count-=1
        if count==0:
            return True
        
        return False
        