class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        ls=[a,b,c]
        ls.sort()
        #minimum is either 0 , 1 , 2
        count=0
        flag=False
        for i in range(1,3):
            if ls[i]-ls[i-1]==1:
                count+=1
            if ls[i]-ls[i-1]==2:
                flag=True
        if flag and count==0:
            count=1
        minimum = count

        maximum = ls[-1]-ls[1] + ls[1]-ls[0]
        if minimum==maximum:
            return [0,0]
        if minimum==0:
            minimum=2
        return [minimum,maximum-2]