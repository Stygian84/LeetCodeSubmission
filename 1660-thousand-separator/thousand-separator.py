class Solution:
    def thousandSeparator(self, n: int) -> str:
        res=""
        num=str(n)
        count=0
        for item in num[::-1]:
            if count==3:
                count=0
                res+="."    
            res+=item    
            count+=1
        return res[::-1]