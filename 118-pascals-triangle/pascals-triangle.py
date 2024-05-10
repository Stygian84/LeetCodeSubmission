class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fact(x):
            if x==0 or x==1:
                return 1
            else:
                return x*fact(x-1)
        ls=[]
        def combination(n,r):
            return int(fact(n)/(fact(r)*fact(n-r)))
        
        for i in range(numRows):
            ls2=[]
            if i !=0:
                ls2.append(1)
            for x in range(1,i):
                ls2.append(combination(i,x))
            ls2.append(1)
            ls.append(ls2)
        return ls
