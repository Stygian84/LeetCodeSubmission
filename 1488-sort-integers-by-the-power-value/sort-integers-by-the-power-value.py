class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def findPower(x):
            count=0
            while x!=1:
                count+=1
                if x%2==0:
                    x=x/2
                else:
                    x=3*x+1
            return count
        ls=[]
        for i in range(lo,hi+1):
            ls.append(i)
        ls.sort(key=lambda x:findPower(x))
        return ls[k-1]