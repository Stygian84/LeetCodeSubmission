class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(a,b,x,y):
            return abs(y-b)+abs(x-a)
        x,y = target
        minimum = dist(0,0,x,y)

        for a,b in ghosts:
            if dist(a,b,x,y)<=minimum:
                return False
        return True
