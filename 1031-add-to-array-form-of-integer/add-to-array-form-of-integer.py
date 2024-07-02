class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ls=[]
        i=-1
        for digit in list(str(k))[::-1]:
            try:
                num[i]+=int(digit)
                i-=1
            except:
                ls=[int(digit)]+ls

        num=ls+num
        num1=0
        for i in range(len(num)):
            num1=num1*10+num[i]
            
        ls=[]
        while num1>=10:
            value=num1%10
            ls.append(value)
            num1//=10
        ls.append(num1)
        ls.reverse()
        return ls

    