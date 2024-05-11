class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dc={"R":0,"U":0}
        for item in moves:
            if item == "R":
                dc["R"]+=1
            elif item =="L":
                dc["R"]-=1
            elif item=="U":
                dc["U"]+=1
            elif item=="D":
                dc["U"]-=1
        for values in dc.values():
            if values!=0:
                return False
        return True
        