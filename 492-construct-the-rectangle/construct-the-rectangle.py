class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        for w in range(int(area**0.5),0,-1):
            l=area/w
            if l>=w and int(l)*int(w)==area:
                return [int(l),int(w)]
            