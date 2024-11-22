class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set()

        for a,b in points:
            s.add( (a,b) )

        print(s)
        n = len(points)

        res = math.inf
        for i in range(n-1):
            a,b = points[i]
            for j in range(i+1,n):
                c,d = points[j]

                if (a,d) in s and (c,b) in s:
                    area = (c-a)*(d-b)
                    if area!=0:
                        res = min(abs(area),res)
        
        if res == math.inf:
            return 0
        return res