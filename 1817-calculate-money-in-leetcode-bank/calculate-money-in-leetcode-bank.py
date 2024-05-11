class Solution:
    def totalMoney(self, n: int) -> int:
        mon=1
        total=0
        for i in range(0,n):
            if i%7==0 and i!=0:
                mon+=1
            total+=i%7+mon
            print(total,mon,i%7,mon+i%7)
        return total
        