class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[1])
        if len(points)==1:
            return 1

        n = len(points)
        count = 0
        i = 0

        while i<n:
            a,b = points[i]

            while i<n-1 and b>=points[i+1][0] :
                i+=1
            count+=1
            i+=1
        return count
        '''res=[points[0]]
        if len(points)==1:
            return res
        points.sort()
        res=[points[0]]
        for item in points[1:]:
            if res[-1][-1]>=item[0]:
                if item[1]>res[-1][1]:
                    res[-1]=[res[-1][0],item[1]]
                else:
                    continue
            else:
                res.append(item)
        return len(res)'''