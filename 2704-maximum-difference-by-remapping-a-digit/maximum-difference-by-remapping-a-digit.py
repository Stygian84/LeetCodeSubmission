class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num=str(num)
        num1=""
        dc1={}
        

        for digit in str_num:
            if digit in dc1:
                num1 += dc1[digit]
            else:
                if len(dc1)<1 and digit!="9":
                    dc1[digit]="9"
                    num1+="9"
                else:
                    num1 += digit
        num1=int(num1)

        num2=""
        dc1={}
        dc1[str_num[0]]="0"

        for digit in str_num:
            if digit in dc1:
                num2 += dc1[digit]
            else:
                num2 += digit
        num2=int(num2)
        return num1-num2

                