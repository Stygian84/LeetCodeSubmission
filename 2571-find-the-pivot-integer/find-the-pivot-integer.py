class Solution:
    def pivotInteger(self, n: int) -> int:
        total=0
        for i in range(1,n+1):
            total+=i
        second_total=0
        result=-1
        for j in range(n,0,-1):
            second_total+=j
            if second_total==total:
                result=j
                break
            total-=j
        return result