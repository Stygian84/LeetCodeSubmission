class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if n == 1:
            if intervals[0][0]==intervals[0][1]:
                return [0]
            return [-1]
        res = []

        ends = {} #store end=index
        i=0
        maximum = -math.inf
        for a,b in intervals:
            ends[a] = i
            i+=1
            maximum = max(maximum,b)
            
        ls = sorted(ends.keys()) # to find closest key
        for a,b in intervals:
            if b == maximum:
                res.append(-1)
            elif b in ends:
                res.append(ends[b])
            else:
                index = bisect_right(ls, b)
                if index == len(ls):
                    res.append(-1)
                else:
                    res.append(ends[ls[index]])

        return res
        
        