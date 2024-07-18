class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i,j=0,len(s)-1
        ls=list(s)

        while i<j:
            if ls[i]!=ls[j]:
                if ls[i]<ls[j]:
                    ls[j]=ls[i]
                else:
                    ls[i]=ls[j]
            i+=1
            j-=1
        
        return "".join(ls)
        