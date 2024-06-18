class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        def merge(intervals):
            res=[intervals[0]]
            if len(intervals)==1:
                return res
            intervals.sort()
            res=[intervals[0]]
            for item in intervals[1:]:
                if res[-1][-1]>=item[0]:
                    if item[1]>res[-1][1]:
                        res[-1]=[res[-1][0],item[1]]
                    else:
                        continue
                else:
                    res.append(item)
            return res
        meetings=merge(meetings)
        
        total=meetings[0][0]-1
        for idx in range(len(meetings)-1):
            total+=meetings[idx+1][0]-meetings[idx][1]-1
        total+=days-meetings[-1][-1]
        return total