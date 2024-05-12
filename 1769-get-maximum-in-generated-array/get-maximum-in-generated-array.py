class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        ls=[]
        for i in range(n+1):
            if i ==0:
                ls.append(0)
            elif i==1:
                ls.append(1)
            elif i%2==0:
                ls.append(ls[i//2])
            else:
                ls.append(ls[(i-1)//2]+ls[(i-1)//2+1])
        print(ls)
        return (max(ls))