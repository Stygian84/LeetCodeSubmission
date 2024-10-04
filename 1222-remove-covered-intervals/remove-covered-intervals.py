class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]-x[0])
        n = len(intervals)
        print(intervals)
        count = n
        for i in range(n-1):
            a,b = intervals[i]
            diff = b-a
            for j in range(i+1,n):
                c,d = intervals[j]
                diff2 = d-c
                if diff2<diff:
                    continue
                else:
                    if c<=a and b<=d:
                        count-=1
                        break
        return count
                
