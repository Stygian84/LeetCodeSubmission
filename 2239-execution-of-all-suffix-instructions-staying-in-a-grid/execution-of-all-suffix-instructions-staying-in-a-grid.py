class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res=[]
        

        for i in range(len(s)):
            
            count=0 
            y,x = startPos       
            for letter in s[i:]:
                if letter=="R": x+=1
                if letter=="L": x-=1
                if letter=="U": y-=1
                if letter=="D": y+=1

                if x<0 or x>n-1 or y<0 or y>n-1:
                    break
                count+=1
            res.append(count)
        return res