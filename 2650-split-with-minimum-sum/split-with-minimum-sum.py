class Solution:
    def splitNum(self, num: int) -> int:
        ls=[]
        for i in str(num):
            ls.append(int(i))
        ls.sort()
        num1=0
        num2=0
        while ls:
            num1=num1*10+ls[0]
            ls.pop(0)
            if ls:
                num2=num2*10+ls[0]
                ls.pop(0)
        return num1+num2

        