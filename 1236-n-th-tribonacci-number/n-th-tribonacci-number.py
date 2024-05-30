class Solution:
    def tribonacci(self, n: int) -> int:
        dc={}
        dc[0]=0
        dc[1]=1
        dc[2]=1
        if n<3:
            return dc[n]
        for i in range(3,n+1):
            dc[i]=dc[i-3]+dc[i-2]+dc[i-1]
        return dc[n]