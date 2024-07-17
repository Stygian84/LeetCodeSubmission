class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        res=[]

        count=0

        dcA={}
        dcB={}
        for a,b in zip(A,B):
            if a==b:
                count+=1
            else:
                if a in dcB:
                    count+=1
                if b in dcA:
                    count+=1

            dcA[a]=0
            dcB[b]=0
            res.append(count)
        
        return res