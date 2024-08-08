class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a,b):
            x1,y1=a
            x2,y2=b

            return math.sqrt((x2-x1)**2+(y2-y1)**2)

        ls = [p1,p2,p3,p4] 
        ls.sort()

        a,b,c,d = ls

        # check all sides length
        if dist(a,b) == dist(a,c) == dist(c,d) == dist(b,d):
            #check angle
            diagonal1 = dist(b, c)
            diagonal2 = dist(a, d)
            side = dist(a,b)
            if side == 0:
                return False
            if math.isclose(diagonal1, side * math.sqrt(2)) and math.isclose(diagonal2, side * math.sqrt(2)):
                return True
        return False 