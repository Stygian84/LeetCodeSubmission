class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        pointer=1
        forward=True

        for i in range(time):
            if forward and pointer<n:
                pointer+=1
            elif pointer==n:
                forward=False
                pointer-=1
            elif not forward and pointer>1:
                pointer-=1
            else:
                forward=True
                pointer+=1

        return pointer