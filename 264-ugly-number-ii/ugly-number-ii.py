class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res=[0]*(n)
        res[0]=1
        if n==1:
            return 1
        
        a,b,c=0,0,0

        two=2
        three=3
        five=5

        for i in range(1,n):
            next_ugly=min(two,three,five)
            res[i]=next_ugly

            if next_ugly==two:
                a+=1
                two=res[a]*2
            if next_ugly==three:
                b+=1
                three=res[b]*3
            if next_ugly==five:
                c+=1
                five=res[c]*5
                
        return res[-1]

