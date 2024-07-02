class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def convertToMin(time):
            hour=int(time[:2])
            minute=int(time[3:])
            return hour*60+minute
            

        res=math.inf
        for i in range(len(timePoints)-1):
            diff = convertToMin(timePoints[i+1]) - convertToMin(timePoints[i])
            if diff<res:
                res=diff
        
        circular_val = convertToMin(timePoints[0])+24*60-convertToMin(timePoints[-1]) 
    
        if circular_val<res:
            res = circular_val

        return res