class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        maximum=0
        res=[]

        def backtrack(start,total,path,arrow):
            nonlocal res
            nonlocal maximum

            if start == 0 or arrow==0:
                if total>maximum:
                    maximum = total
                    res = path[:]
                    if arrow>0:
                        res[0]=arrow
                return

            for i in range(start,-1,-1):
                backtrack( i-1, total, path, arrow)

                arrowSpent = aliceArrows[i]+1

                if arrow-arrowSpent<0:
                    continue

                path[i]=arrowSpent
                backtrack( i-1, total+i, path, arrow-arrowSpent)
                path[i]=0


        ls = [0]*12
        backtrack(11,0,ls,numArrows)
        return res