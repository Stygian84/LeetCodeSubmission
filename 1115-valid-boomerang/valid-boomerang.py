class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def gradient(coord1,coord2): 
            return (coord2[1]-coord1[1])/(coord2[0]-coord1[0]) if (coord2[0]-coord1[0])  != 0 else math.inf
        if points[0]==points[1] or points[1]==points[2] or points[0]==points[2]:
            return False
        return gradient(points[2],points[1])!=gradient(points[1],points[0])