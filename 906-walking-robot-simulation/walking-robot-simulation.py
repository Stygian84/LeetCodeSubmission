class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def dist(x):
            return x[0]**2 + x[1]**2

        max_dist=0
        
        dc = set(map(tuple, obstacles))

        coord=[0,0]
        
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        
        i=0
        
        for c in commands:
            if c>0:
                #move
                x,y = direction[i]

                for _ in range(c):
                    coord[0]+=x
                    coord[1]+=y
                    if tuple(coord) in dc:
                        coord[0]-=x
                        coord[1]-=y
                        break

            elif c==-1:
                i+=1
                i%=4

            elif c==-2:
                i-=1
                i%=4
                
            max_dist=max(dist(coord),max_dist)


        return max_dist
