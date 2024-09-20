class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def dist(a,b,c,d):
            return abs(c-a)**2+abs(d-b)**2
        #a^2<=r^2-b^2

        res = []

        for a,b,r in queries:
            maximum = r**2
            count = 0

            for x,y in points:
                distance = dist(a,b,x,y)
                if distance<=maximum:
                    count+=1

            res.append(count)
        return res