class Solution:
    def isHappy(self, n: int) -> bool:
        sum_value=n
        while True:
            numb=str(sum_value)
            sum_value=0
            for digit in numb:
                sum_value+=int(digit)**2
            if int(numb)==1:
                return True
            elif int(numb)==4:
                return False
            print(numb,sum_value)
        #if sum_value%10==0:
        #    return True
        #return False