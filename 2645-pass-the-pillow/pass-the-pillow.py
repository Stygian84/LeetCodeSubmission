class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        #n-1 n-3 n-2 n-1    1
        #n-1 n n-1 n-2 n-3  0
        if (time//(n-1))%2==1:
            return n-time%(n-1)
        else:
            return time%(n-1)+1