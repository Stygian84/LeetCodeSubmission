class Solution:
    def magicalString(self, n: int) -> int:
        s="122"
        a,b="1","2"
        i=2
        one=1
        if n<=3:
            return 1

        while len(s)<n:
            multiplier = int(s[i])
            s+=a*multiplier
            
            if a=="1":
                one+=multiplier

            a,b=b,a
            i+=1
        
        if len(s)>n:
            one-=s[n:].count("1")
            
        return one