class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)

        countA = defaultdict(int)
        countB = defaultdict(int)

        res = [0]
        for i in range(n):
            count = 0

            countA[A[i]] += 1
            countB[B[i]] += 1

            if A[i] == B[i]:
                count+=1
            else:
                if A[i] in countB:
                    count+=1
                if B[i] in countA:
                    count+=1
            
            res.append(res[-1]+count)
        
        return res[1:]
        '''
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
        
        return res'''