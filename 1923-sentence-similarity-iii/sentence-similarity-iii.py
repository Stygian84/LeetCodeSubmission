class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        ls1 = sentence1.split()
        ls2 = sentence2.split()
        if len(ls1)>len(ls2):
            ls1,ls2=ls2,ls1
        #ls1<=ls2
        #check if there is insertion in middle, start, end
        n = len(ls2)
        m = len(ls1)
        if ls2[-m:]==ls1 or ls2[:m]==ls1:
            return True
        j=0
        idx=[]
        start,end=False,False

        for i in range(n):
            if j>=m:
                break
            if ls2[i]==ls1[j]:
                j+=1
                idx.append(i)
                
        if ls1[0]==ls2[0]:
            start=True
        if ls1[-1]==ls2[-1]:
            end=True

        #not all ls1 in ls2
        if j<=m-1:
            return False
        if not start or not end:
            return False
        gap = False

        for i in range(1,len(idx)):
            if gap and idx[i]-idx[i-1]>1:
                return False
            if idx[i]-idx[i-1]>1:
                gap=True
        return True
        
        