class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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