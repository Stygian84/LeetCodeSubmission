class Solution:
    def minSwaps(self, s: str) -> int:
        
        n = len(s)
        ls = list(s)

        one = ls.count("1")
        zero = ls.count("0")
        if abs(zero-one)>1:
            return -1
        
        s1=[]
        s2=[]

        for i in range(n):
            if i%2==0:
                s1.append("1")
                s2.append("0")
            else:
                s2.append("1")
                s1.append("0")
        
        count1=0
        count2=0
        for x,a,b in zip(ls,s1,s2):
            if x!=a:
                count1+=1
            if x!=b:
                count2+=1
        

        if count1%2==1:
            count1=math.inf
        else:
            count1//=2
        
        if count2%2==1:
            count2=math.inf
        else:
            count2//=2

        return min(count1,count2)