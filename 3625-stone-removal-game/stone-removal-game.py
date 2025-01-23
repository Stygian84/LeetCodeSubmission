class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        alice = True
        for i in range(10,-1,-1):
            alice = not alice
            n-=i
            if n<0:
                return alice