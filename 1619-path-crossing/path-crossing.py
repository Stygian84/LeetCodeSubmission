class Solution:
    def isPathCrossing(self, path: str) -> bool:
        origin=[0,0]
        dc={}
        for letter in path:
            dc[tuple(origin)]=0
            if letter=="N":
                origin[1]+=1
            elif letter=="S":
                origin[1]+=-1
            elif letter=="E":
                origin[0]+=1
            else:
                origin[0]+=-1
            if tuple(origin) in dc:
                return True
                
        return False