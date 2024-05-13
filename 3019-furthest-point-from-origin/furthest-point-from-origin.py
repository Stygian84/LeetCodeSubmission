class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        origin=0
        count=0
        for letter in moves:
            if letter=="L":
                origin-=1
            elif letter=="R":
                origin+=1
            else:
                count+=1
        return abs(origin)+count
        
        