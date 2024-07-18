class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count=0

        end = -math.inf

        for a,b in intervals:
            if a>=end:
                end=b
            else:
                count+=1
        return count
        '''if len(intervals)<=1:
            return 0

        count = 0
        
        intervals.sort()
        a,b = intervals[0][0],intervals[0][1]

        for i in range(1,len(intervals)):
            c,d = intervals[i][0],intervals[i][1]

            if c>=b: 
                a,b=c,d
                continue
            if d<=b:
                count+=1
                a,b=c,d
                continue
            else:
                count+=1
                continue
        
        return count'''
