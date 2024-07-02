class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def convertToMin(time):
            hour=int(time[:2])
            minute=int(time[3:])
            return hour*60+minute
            

        res=math.inf
        for i in range(len(timePoints)-1):
            res=min(convertToMin(timePoints[i+1]) - convertToMin(timePoints[i]) , res)
        
        res=min(convertToMin(timePoints[0])+24*60-convertToMin(timePoints[-1]) , res)

        return res