class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # north , west, south , east
        directions =  [ (0,1), (-1,0), (0,-1), (1,0)]
        dir_idx = 0

        flag = False
        init = [0,0]
        for _ in range(4):

            for item in instructions:
                if item == "G":
                    x,y = directions[dir_idx]
                    init[0]+=x
                    init[1]+=y

                if item == "L":
                    dir_idx+=1
                    dir_idx%=4
                    flag = True

                elif item == "R":
                    dir_idx-=1
                    dir_idx%=4
                    flag = True
        
            if init == [0,0]:
                return True
                
        return False