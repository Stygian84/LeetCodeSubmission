class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        pos = [0,0]
        for c in commands:
            if c == "DOWN": pos[0]+=1
            elif c == "UP": pos[0]-=1
            elif c == "RIGHT": pos[1]+=1
            elif c == "LEFT": pos[1]-=1
        
        return pos[0]*n + pos[1]