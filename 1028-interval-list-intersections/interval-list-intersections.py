class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        m,n=len(firstList),len(secondList)

        res=[]
        while i<m and j<n:
            firstFirst=firstList[i][0]
            secondFirst=firstList[i][1]
            firstSecond=secondList[j][0]
            secondSecond=secondList[j][1]

            temp_arr=[]
            if firstSecond<=secondFirst<=secondSecond:
                if firstFirst<=firstSecond:
                    temp_arr.append(firstSecond)
                else:
                    temp_arr.append(firstFirst)
                temp_arr.append(secondFirst)
                res.append(temp_arr)
                i+=1
                continue
            elif firstFirst<=secondSecond<=secondFirst:
                if firstSecond<=firstFirst:
                    temp_arr.append(firstFirst)
                else:
                    temp_arr.append(firstSecond)
                temp_arr.append(secondSecond)
                res.append(temp_arr)
                j+=1
                continue

            if secondSecond<firstFirst:
                j+=1
                continue
            if secondFirst<firstSecond:
                i+=1
                continue
        

        return res