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
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            num[i] += carry
            if num[i] >= 10:
                carry = num[i] // 10
                num[i] %= 10
            else:
                carry = 0
        
        if carry > 0:
            num = list(map(int, str(carry))) + num

        return num

    