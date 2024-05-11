class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            num2=0
            for digit in str(num):
                num2+=int(digit)
            num=num2
        return num
        