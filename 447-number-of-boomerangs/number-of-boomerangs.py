class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist(x1,y1,x2,y2):
            return (x2-x1)**2+(y2-y1)**2
        
        n = len(points)
        res = 0
        for i in range(n):
            dc = defaultdict(int)
            x1,y1=points[i]

            for j in range(n):
                if i!=j:
                    x2,y2=points[j]
                    distance = dist(x1,y1,x2,y2)
                    dc[distance]+=1

            for v in dc.values():
                if v>=2:
                    res += v * (v-1) 

        return res