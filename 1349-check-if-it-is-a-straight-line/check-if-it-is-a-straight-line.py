class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def gradient(coord1,coord2): 
            return (coord2[1]-coord1[1])/(coord2[0]-coord1[0]) if (coord2[0]-coord1[0])  != 0 else math.inf
        first_gradient=gradient(coordinates[0],coordinates[-1])
        for idx in range(len(coordinates)-1):
            if gradient(coordinates[idx],coordinates[idx+1])!=first_gradient:
                return False
        return True
        
        