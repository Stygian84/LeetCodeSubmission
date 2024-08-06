class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2==1:
            return []

        total = 0
        res = []
        for i in range(2,finalSum+1,2):
            if total+i > finalSum:
                total-=res.pop()
            
            total+=i
            res.append(i)
            if total == finalSum:
                return res
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