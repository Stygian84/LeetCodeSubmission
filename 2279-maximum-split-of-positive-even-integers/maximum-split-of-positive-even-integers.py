class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2==1:
            return []

        current = 2
        res = []
        while finalSum>=current:
            res.append(current)
            finalSum-=current
            current+=2

        if finalSum > 0:
            res[-1] += finalSum
            
        return res
        '''if finalSum%2==1:
            return []

        if finalSum==2:
            return [2]
        
        res = []
        def backtrack(total,path,start): 
            nonlocal res
            if len(path)>len(res) and total == finalSum:
                res = path[:]
                return



            for i in range(start,finalSum,2):
                if total+i<=finalSum:
                    path.append(i)
                    backtrack(total+i,path,i+2)
                    path.pop()

        backtrack(0,[],2)

        return res'''